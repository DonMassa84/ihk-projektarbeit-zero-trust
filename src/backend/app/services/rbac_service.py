from typing import Optional, Dict, Any, List
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, or_, delete
from sqlalchemy.orm import selectinload
from app.models.models import User, Role, UserRoleAssignment, RoleRequest, AuditLog
from app.services.audit_service import AuditService
import structlog

logger = structlog.get_logger()


class RBACService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.audit = AuditService(db)

    async def request_role(
        self,
        user_id: str,
        role_id: str,
        justification: str,
        ip_address: Optional[str] = None,
    ) -> dict:
        user = await self.db.get(User, user_id)
        role = await self.db.get(Role, role_id)
        if not user or not role:
            raise ValueError("User or role not found")

        existing = await self.db.execute(
            select(RoleRequest).where(
                and_(
                    RoleRequest.user_id == user_id,
                    RoleRequest.role_id == role_id,
                    RoleRequest.status == "pending",
                )
            )
        )
        if existing.scalar_one_or_none():
            raise ValueError("Pending request already exists for this role")

        request = RoleRequest(
            user_id=user_id,
            role_id=role_id,
            justification=justification,
            status="pending",
        )
        self.db.add(request)
        await self.db.commit()
        await self.db.refresh(request)

        await self.audit.log(
            user_id=user_id,
            action="ROLE_REQUESTED",
            resource_type="role_request",
            resource_id=request.id,
            details={"role_id": role_id, "justification": justification},
            ip_address=ip_address,
        )

        return {"request_id": request.id, "status": "pending", "role": role.name}

    async def approve_request(
        self,
        request_id: str,
        reviewer_id: str,
        comment: Optional[str] = None,
    ) -> dict:
        request = await self.db.get(RoleRequest, request_id)
        if not request:
            raise ValueError("Request not found")
        if request.status != "pending":
            raise ValueError("Request already processed")

        request.status = "approved"
        request.reviewed_by = reviewer_id
        request.review_comment = comment
        request.updated_at = datetime.utcnow()

        assignment = UserRoleAssignment(
            user_id=request.user_id,
            role_id=request.role_id,
            granted_by=reviewer_id,
        )
        self.db.add(assignment)
        await self.db.commit()

        await self.audit.log(
            user_id=reviewer_id,
            action="ROLE_APPROVED",
            resource_type="role_assignment",
            resource_id=assignment.id,
            details={
                "request_id": request_id,
                "target_user": request.user_id,
                "role_id": request.role_id,
                "comment": comment,
            },
        )

        return {"status": "approved", "assignment_id": assignment.id}

    async def reject_request(
        self,
        request_id: str,
        reviewer_id: str,
        reason: str,
    ) -> dict:
        request = await self.db.get(RoleRequest, request_id)
        if not request:
            raise ValueError("Request not found")
        if request.status != "pending":
            raise ValueError("Request already processed")

        request.status = "rejected"
        request.reviewed_by = reviewer_id
        request.review_comment = reason
        request.updated_at = datetime.utcnow()
        await self.db.commit()

        await self.audit.log(
            user_id=reviewer_id,
            action="ROLE_REJECTED",
            resource_type="role_request",
            resource_id=request_id,
            details={"reason": reason, "target_user": request.user_id},
        )

        return {"status": "rejected", "reason": reason}

    async def revoke_role(
        self,
        assignment_id: str,
        revoker_id: str,
        reason: str,
    ) -> dict:
        assignment = await self.db.get(UserRoleAssignment, assignment_id)
        if not assignment:
            raise ValueError("Assignment not found")

        assignment.grant_end = datetime.utcnow()
        assignment.revoke_reason = reason
        await self.db.commit()

        await self.audit.log(
            user_id=revoker_id,
            action="ROLE_REVOKED",
            resource_type="role_assignment",
            resource_id=assignment_id,
            details={"reason": reason, "target_user": assignment.user_id},
        )

        return {"status": "revoked"}

    async def get_user_roles(self, user_id: str) -> List[dict]:
        stmt = (
            select(UserRoleAssignment)
            .options(selectinload(UserRoleAssignment.role))
            .where(
                and_(
                    UserRoleAssignment.user_id == user_id,
                    or_(
                        UserRoleAssignment.grant_end.is_(None),
                        UserRoleAssignment.grant_end > datetime.utcnow(),
                    ),
                )
            )
        )
        result = await self.db.execute(stmt)
        assignments = result.scalars().all()

        return [
            {
                "id": a.id,
                "role_id": a.role_id,
                "role_name": a.role.name,
                "granted_at": a.grant_start.isoformat() if a.grant_start else None,
                "expires_at": a.grant_end.isoformat() if a.grant_end else None,
            }
            for a in assignments
        ]

    async def get_pending_requests(self) -> List[dict]:
        stmt = (
            select(RoleRequest)
            .options(selectinload(RoleRequest.user), selectinload(RoleRequest.role))
            .where(RoleRequest.status == "pending")
        )
        result = await self.db.execute(stmt)
        requests = result.scalars().all()

        return [
            {
                "id": r.id,
                "user": r.user.display_name if r.user else None,
                "role": r.role.name if r.role else None,
                "justification": r.justification,
                "created_at": r.created_at.isoformat() if r.created_at else None,
            }
            for r in requests
        ]