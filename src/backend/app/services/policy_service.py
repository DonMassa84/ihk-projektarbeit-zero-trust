from typing import Dict, Any, List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.models import Role, AccessRequest, RequestStatus


PolicyResult = Dict[str, Any]


class PolicyService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def check_create_request(
        self,
        requester_reference: str,
        target_user_reference: str,
        requested_role_id: str,
        justification: str,
    ) -> PolicyResult:
        role = await self.db.get(Role, requested_role_id)
        if not role:
            return {"allowed": False, "policy_id": "POL-ROLE-EXISTS", "reason": "Role not found", "severity": "error", "remediation": "Verify role ID"}
        if not role.active:
            return {"allowed": False, "policy_id": "POL-ROLE-ACTIVE", "reason": "Role is inactive", "severity": "error", "remediation": "Activate role first"}

        if not justification or len(justification.strip()) < 10:
            return {"allowed": False, "policy_id": "POL-JUSTIFICATION", "reason": "Justification too short (min 10 chars)", "severity": "error", "remediation": "Provide detailed justification"}

        if not requester_reference:
            return {"allowed": False, "policy_id": "POL-REQUESTER", "reason": "Requester reference is required", "severity": "error", "remediation": "Specify requester"}

        if not target_user_reference:
            return {"allowed": False, "policy_id": "POL-TARGET", "reason": "Target user reference is required", "severity": "error", "remediation": "Specify target user"}

        if role.risk_level in ("high", "critical"):
            return {"allowed": True, "policy_id": "POL-HIGH-RISK", "reason": "High-risk role requires elevated approval", "severity": "warning", "remediation": "Ensure senior approver"}

        return {"allowed": True, "policy_id": "POL-CREATE-OK", "reason": "All checks passed", "severity": "info", "remediation": None}

    async def check_approve(
        self,
        request: AccessRequest,
        approver_reference: str,
    ) -> PolicyResult:
        if request.status != RequestStatus.SUBMITTED:
            return {"allowed": False, "policy_id": "POL-STATUS", "reason": f"Cannot approve request in status {request.status.value}", "severity": "error", "remediation": "Submit request first"}

        if approver_reference == request.requester_reference:
            return {"allowed": False, "policy_id": "POL-SELF-APPROVE", "reason": "Self-approval is not allowed", "severity": "error", "remediation": "Assign different approver"}

        role = await self.db.get(Role, request.requested_role_id)
        if role and role.risk_level in ("high", "critical") and not approver_reference:
            return {"allowed": False, "policy_id": "POL-APPROVER-REQUIRED", "reason": "High-risk roles require named approver", "severity": "error", "remediation": "Specify an authorized approver"}

        return {"allowed": True, "policy_id": "POL-APPROVE-OK", "reason": "Approval policy passed", "severity": "info", "remediation": None}

    async def check_reject(
        self,
        request: AccessRequest,
        reason: str,
    ) -> PolicyResult:
        if request.status != RequestStatus.SUBMITTED:
            return {"allowed": False, "policy_id": "POL-STATUS", "reason": f"Cannot reject request in status {request.status.value}", "severity": "error", "remediation": "Submit request first"}

        if not reason or len(reason.strip()) < 5:
            return {"allowed": False, "policy_id": "POL-REJECT-REASON", "reason": "Rejection reason too short (min 5 chars)", "severity": "error", "remediation": "Provide detailed rejection reason"}

        return {"allowed": True, "policy_id": "POL-REJECT-OK", "reason": "Rejection policy passed", "severity": "info", "remediation": None}

    async def check_provision(
        self,
        request: AccessRequest,
    ) -> PolicyResult:
        if request.status == RequestStatus.PROVISIONED:
            return {"allowed": True, "policy_id": "POL-PROV-IDEMPOTENT", "reason": "Already provisioned (idempotent)", "severity": "info", "remediation": None}
        if request.status != RequestStatus.APPROVED:
            return {"allowed": False, "policy_id": "POL-PROV-STATUS", "reason": f"Cannot provision request in status {request.status.value}. Must be APPROVED.", "severity": "error", "remediation": "Approve request first"}

        role = await self.db.get(Role, request.requested_role_id)
        if not role:
            return {"allowed": False, "policy_id": "POL-PROV-ROLE", "reason": "Assigned role no longer exists", "severity": "error", "remediation": "Recreate role or cancel request"}

        return {"allowed": True, "policy_id": "POL-PROV-OK", "reason": "Provisioning policy passed", "severity": "info", "remediation": None}
