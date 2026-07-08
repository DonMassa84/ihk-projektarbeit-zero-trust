from fastapi import APIRouter
from typing import List
from ...schemas.audit import AuditLogCreate, AuditLogResponse, AuditStatsResponse

router = APIRouter(prefix="/audit", tags=["Audit"])

@router.post("/log", response_model=AuditLogResponse)
async def create_log(body: AuditLogCreate):
    return AuditLogResponse(
        id=1, timestamp="2026-07-08T00:00:00Z",
        action=body.action, resource=body.resource,
        user_id=body.user_id, details=body.details, result=body.result,
    )

@router.get("/logs", response_model=List[AuditLogResponse])
async def get_logs(skip: int = 0, limit: int = 50):
    return [
        AuditLogResponse(
            id=1, timestamp="2026-07-08T00:00:00Z",
            action="role_requested", resource="rbac",
            user_id=1, details="Requested Developer role", result="pending",
        )
    ]

@router.get("/stats", response_model=AuditStatsResponse)
async def get_stats():
    return AuditStatsResponse(
        total_entries=42,
        actions_by_type={"role_requested": 20, "role_approved": 15, "role_revoked": 7},
        recent_activity=[],
    )
