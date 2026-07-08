from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ...schemas.rbac import (
    RoleRequestCreate, RoleRequestResponse,
    ApproveRequest, RejectRequest, RevokeRequest,
    RoleResponse, UserRoleResponse,
)

router = APIRouter(prefix="/rbac", tags=["RBAC"])

@router.post("/request", response_model=RoleRequestResponse)
async def request_role(body: RoleRequestCreate):
    return RoleRequestResponse(
        id=1, user_id=body.user_id, role_id=body.role_id,
        status="pending", justification=body.justification,
        created_at="2026-07-08T00:00:00Z",
    )

@router.post("/approve", response_model=RoleRequestResponse)
async def approve_request(body: ApproveRequest):
    return RoleRequestResponse(
        id=body.request_id, user_id=1, role_id=1,
        status="approved", justification="",
        created_at="2026-07-08T00:00:00Z",
        reviewed_by=body.reviewer_id,
        reviewed_at="2026-07-08T00:00:00Z",
    )

@router.post("/reject", response_model=RoleRequestResponse)
async def reject_request(body: RejectRequest):
    return RoleRequestResponse(
        id=body.request_id, user_id=1, role_id=1,
        status="rejected", justification="",
        created_at="2026-07-08T00:00:00Z",
        reviewed_by=body.reviewer_id,
        reviewed_at="2026-07-08T00:00:00Z",
    )

@router.post("/revoke")
async def revoke_role(body: RevokeRequest):
    return {"status": "revoked", "user_id": body.user_id, "role_id": body.role_id}

@router.get("/requests", response_model=List[RoleRequestResponse])
async def list_requests(status: str = "pending"):
    return [
        RoleRequestResponse(
            id=1, user_id=2, role_id=3,
            status=status, justification="Need access for project",
            created_at="2026-07-08T00:00:00Z",
        )
    ]

@router.get("/users/{user_id}/roles", response_model=List[UserRoleResponse])
async def get_user_roles(user_id: int):
    return [
        UserRoleResponse(user_id=user_id, role_id=1, role_name="Developer", assigned_at="2026-07-08T00:00:00Z"),
    ]

@router.get("/roles", response_model=List[RoleResponse])
async def list_roles():
    return [
        RoleResponse(id=1, name="Admin", description="Full access"),
        RoleResponse(id=2, name="Developer", description="Read/write repos"),
        RoleResponse(id=3, name="Auditor", description="Read logs"),
        RoleResponse(id=4, name="Read-Only", description="Read repos"),
        RoleResponse(id=5, name="HR-Manager", description="HR system access"),
        RoleResponse(id=6, name="Finance", description="Finance system access"),
    ]
