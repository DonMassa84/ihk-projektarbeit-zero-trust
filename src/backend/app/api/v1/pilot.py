import uuid
from typing import List, Optional
from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from app.core.database import get_db
from app.models.models import (
    UserReference, Role, AccessRequest, ApprovalDecision,
    AuditEvent, ProvisioningAttempt, RequestStatus,
    ProvisioningMode,
)
from app.schemas.pilot import (
    UserReferenceCreate, UserReferenceResponse,
    RoleCreate, RoleResponse,
    AccessRequestCreate, AccessRequestSubmit,
    AccessRequestApprove, AccessRequestReject,
    AccessRequestResponse, AccessRequestListResponse,
    AuditEventResponse, AuditVerifyResponse,
    ProvisioningAttemptResponse,
    ErrorResponse,
)
from app.services.audit_chain_service import AuditChainService
from app.services.policy_service import PolicyService
from app.services.provisioning_service import ProvisioningService

router = APIRouter(tags=["Pilot"])


@router.post("/users", response_model=UserReferenceResponse, status_code=201)
async def create_user(payload: UserReferenceCreate, db: AsyncSession = Depends(get_db)):
    existing = await db.execute(
        select(UserReference).where(UserReference.external_reference == payload.external_reference)
    )
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=409, detail="User already exists")
    user = UserReference(
        external_reference=payload.external_reference,
        display_name=payload.display_name,
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


@router.get("/users", response_model=List[UserReferenceResponse])
async def list_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(UserReference).order_by(UserReference.external_reference))
    return list(result.scalars().all())


@router.post("/roles", response_model=RoleResponse, status_code=201)
async def create_role(payload: RoleCreate, db: AsyncSession = Depends(get_db)):
    existing = await db.execute(select(Role).where(Role.name == payload.name))
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=409, detail="Role already exists")
    role = Role(
        name=payload.name,
        description=payload.description,
        risk_level=payload.risk_level,
        github_team_slug=payload.github_team_slug,
    )
    db.add(role)
    await db.commit()
    await db.refresh(role)
    return role


@router.get("/roles", response_model=List[RoleResponse])
async def list_roles(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Role).order_by(Role.name))
    return list(result.scalars().all())


@router.post("/access-requests", response_model=AccessRequestResponse, status_code=201)
async def create_access_request(payload: AccessRequestCreate, db: AsyncSession = Depends(get_db)):
    policy = PolicyService(db)
    check = await policy.check_create_request(
        requester_reference=payload.requester_reference,
        target_user_reference=payload.target_user_reference,
        requested_role_id=payload.requested_role_id,
        justification=payload.justification,
    )
    if not check["allowed"]:
        raise HTTPException(status_code=422, detail=check["reason"])

    request = AccessRequest(
        requester_reference=payload.requester_reference,
        target_user_reference=payload.target_user_reference,
        requested_role_id=payload.requested_role_id,
        justification=payload.justification,
        status=RequestStatus.DRAFT,
        correlation_id=str(uuid.uuid4()),
    )
    db.add(request)
    await db.commit()
    await db.refresh(request)

    audit = AuditChainService(db)
    await audit.log_event(
        event_type="ACCESS_REQUEST_CREATED",
        actor_reference=payload.requester_reference,
        object_type="access_request",
        object_id=request.id,
        payload={"role_id": payload.requested_role_id, "target": payload.target_user_reference},
        correlation_id=request.correlation_id,
    )
    return _request_to_response(request)


@router.get("/access-requests/{request_id}", response_model=AccessRequestResponse)
async def get_access_request(request_id: str, db: AsyncSession = Depends(get_db)):
    request = await db.get(AccessRequest, request_id)
    if not request:
        raise HTTPException(status_code=404, detail="Access request not found")
    return _request_to_response(request)


@router.get("/access-requests", response_model=AccessRequestListResponse)
async def list_access_requests(
    status: Optional[str] = Query(None),
    limit: int = Query(50, le=100),
    offset: int = Query(0, ge=0),
    db: AsyncSession = Depends(get_db),
):
    stmt = select(AccessRequest).order_by(AccessRequest.requested_at.desc())
    if status:
        stmt = stmt.where(AccessRequest.status == status)
    count_stmt = select(func.count()).select_from(stmt.subquery())
    total_result = await db.execute(count_stmt)
    total = total_result.scalar() or 0
    stmt = stmt.limit(limit).offset(offset)
    result = await db.execute(stmt)
    requests = list(result.scalars().all())
    return AccessRequestListResponse(
        requests=[_request_to_response(r) for r in requests],
        total=total,
    )


@router.post("/access-requests/{request_id}/submit", response_model=AccessRequestResponse)
async def submit_access_request(request_id: str, db: AsyncSession = Depends(get_db)):
    request = await db.get(AccessRequest, request_id)
    if not request:
        raise HTTPException(status_code=404, detail="Access request not found")
    if request.status != RequestStatus.DRAFT:
        raise HTTPException(status_code=422, detail=f"Cannot submit request in status {request.status.value}")
    request.status = RequestStatus.SUBMITTED
    await db.commit()
    await db.refresh(request)
    audit = AuditChainService(db)
    await audit.log_event(
        event_type="ACCESS_REQUEST_SUBMITTED",
        actor_reference=request.requester_reference,
        object_type="access_request",
        object_id=request.id,
        correlation_id=request.correlation_id,
    )
    return _request_to_response(request)


@router.post("/access-requests/{request_id}/approve", response_model=AccessRequestResponse)
async def approve_access_request(request_id: str, payload: AccessRequestApprove, db: AsyncSession = Depends(get_db)):
    request = await db.get(AccessRequest, request_id)
    if not request:
        raise HTTPException(status_code=404, detail="Access request not found")
    policy = PolicyService(db)
    check = await policy.check_approve(request, payload.approver_reference)
    if not check["allowed"]:
        raise HTTPException(status_code=422, detail=check["reason"])
    decision = ApprovalDecision(
        request_id=request.id,
        decision="APPROVED",
        approver_reference=payload.approver_reference,
        comment=payload.comment,
    )
    db.add(decision)
    request.status = RequestStatus.APPROVED
    request.decided_at = datetime.now(timezone.utc)
    request.decided_by = payload.approver_reference
    await db.commit()
    await db.refresh(request)
    audit = AuditChainService(db)
    await audit.log_event(
        event_type="ACCESS_REQUEST_APPROVED",
        actor_reference=payload.approver_reference,
        object_type="access_request",
        object_id=request.id,
        correlation_id=request.correlation_id,
    )
    return _request_to_response(request)


@router.post("/access-requests/{request_id}/reject", response_model=AccessRequestResponse)
async def reject_access_request(request_id: str, payload: AccessRequestReject, db: AsyncSession = Depends(get_db)):
    request = await db.get(AccessRequest, request_id)
    if not request:
        raise HTTPException(status_code=404, detail="Access request not found")
    policy = PolicyService(db)
    check = await policy.check_reject(request, payload.reason)
    if not check["allowed"]:
        raise HTTPException(status_code=422, detail=check["reason"])
    decision = ApprovalDecision(
        request_id=request.id,
        decision="REJECTED",
        approver_reference=payload.approver_reference,
        comment=payload.reason,
    )
    db.add(decision)
    request.status = RequestStatus.REJECTED
    request.decided_at = datetime.now(timezone.utc)
    request.decided_by = payload.approver_reference
    await db.commit()
    await db.refresh(request)
    audit = AuditChainService(db)
    await audit.log_event(
        event_type="ACCESS_REQUEST_REJECTED",
        actor_reference=payload.approver_reference,
        object_type="access_request",
        object_id=request.id,
        correlation_id=request.correlation_id,
    )
    return _request_to_response(request)


@router.post("/access-requests/{request_id}/provision", response_model=AccessRequestResponse)
async def provision_access_request(
    request_id: str,
    mode: str = Query("dry_run"),
    db: AsyncSession = Depends(get_db),
):
    request = await db.get(AccessRequest, request_id)
    if not request:
        raise HTTPException(status_code=404, detail="Access request not found")
    policy = PolicyService(db)
    check = await policy.check_provision(request)
    if not check["allowed"]:
        raise HTTPException(status_code=422, detail=check["reason"])
    prov_mode = ProvisioningMode.DRY_RUN if mode == "dry_run" else ProvisioningMode.TEST_API
    prov = ProvisioningService(db)
    await prov.provision(request, mode=prov_mode)
    await db.refresh(request)
    return _request_to_response(request)


@router.get("/access-requests/{request_id}/attempts", response_model=List[ProvisioningAttemptResponse])
async def get_provisioning_attempts(request_id: str, db: AsyncSession = Depends(get_db)):
    prov = ProvisioningService(db)
    attempts = await prov.get_attempts(request_id)
    return [
        ProvisioningAttemptResponse(
            id=a.id,
            request_id=a.request_id,
            attempt_number=a.attempt_number,
            mode=a.mode.value if a.mode else "UNKNOWN",
            result=a.result.value if a.result else None,
            response_code=a.response_code,
            error_message=a.error_message,
        )
        for a in attempts
    ]


@router.get("/audit/events", response_model=List[AuditEventResponse])
async def get_audit_events(
    limit: int = Query(50, le=200),
    offset: int = Query(0, ge=0),
    event_type: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
):
    audit = AuditChainService(db)
    events = await audit.get_events(limit=limit, offset=offset, event_type=event_type)
    return [
        AuditEventResponse(
            id=e.id,
            event_type=e.event_type,
            actor_reference=e.actor_reference,
            object_type=e.object_type,
            object_id=e.object_id,
            timestamp=e.timestamp,
            payload_json=e.payload_json,
            previous_hash=e.previous_hash,
            event_hash=e.event_hash,
            correlation_id=e.correlation_id,
        )
        for e in events
    ]


@router.get("/audit/verify", response_model=AuditVerifyResponse)
async def verify_audit_chain(db: AsyncSession = Depends(get_db)):
    audit = AuditChainService(db)
    result = await audit.verify_chain()
    return AuditVerifyResponse(**result)


def _request_to_response(r: AccessRequest) -> AccessRequestResponse:
    return AccessRequestResponse(
        id=r.id,
        requester_reference=r.requester_reference,
        target_user_reference=r.target_user_reference,
        requested_role_id=r.requested_role_id,
        justification=r.justification,
        status=r.status.value if r.status else "UNKNOWN",
        correlation_id=r.correlation_id,
        requested_at=r.requested_at,
        decided_at=r.decided_at,
        decided_by=r.decided_by,
        provisioned_at=r.provisioned_at,
        failure_reason=r.failure_reason,
    )
