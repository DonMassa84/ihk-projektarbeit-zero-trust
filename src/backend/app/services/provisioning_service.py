import time
import structlog
from datetime import datetime, timezone
from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select as sel, func
from app.models.models import (
    AccessRequest, ProvisioningAttempt, ProvisioningMode,
    ProvisioningResult, RequestStatus, Role as RoleModel,
)
from app.services.audit_chain_service import AuditChainService

logger = structlog.get_logger()


class GitHubSimulatedResponse:
    def __init__(self, status_code: int, data: dict):
        self.status_code = status_code
        self._data = data

    def json(self):
        return self._data


class ProvisioningService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.audit = AuditChainService(db)

    async def provision(
        self,
        request: AccessRequest,
        mode: ProvisioningMode = ProvisioningMode.DRY_RUN,
    ) -> ProvisioningAttempt:
        role = await self.db.get(RoleModel, request.requested_role_id)
        team_slug = role.github_team_slug if role else None

        stmt = sel(func.count()).select_from(ProvisioningAttempt).where(
            ProvisioningAttempt.request_id == request.id
        )
        count_result = await self.db.execute(stmt)
        attempt_number = (count_result.scalar() or 0) + 1
        now = datetime.now(timezone.utc)

        attempt = ProvisioningAttempt(
            request_id=request.id,
            attempt_number=attempt_number,
            mode=mode,
            started_at=now,
        )
        self.db.add(attempt)

        if mode == ProvisioningMode.DRY_RUN:
            attempt.result = ProvisioningResult.SIMULATED
            attempt.response_code = 200
            attempt.completed_at = now
            request.status = RequestStatus.PROVISIONED
            request.provisioned_at = now
            await self.db.commit()
            await self.db.refresh(attempt)
            await self.audit.log_event(
                event_type="PROVISIONING_DRY_RUN",
                actor_reference="system",
                object_type="provisioning_attempt",
                object_id=attempt.id,
                payload={"request_id": request.id, "role": role.name if role else "unknown",
                          "team": team_slug, "mode": "DRY_RUN", "result": "SIMULATED"},
                correlation_id=request.correlation_id,
            )
            return attempt

        try:
            response = await self._call_github_api(team_slug, request.target_user_reference)
            if response.status_code == 200:
                attempt.result = ProvisioningResult.SUCCESS
                attempt.response_code = response.status_code
                request.status = RequestStatus.PROVISIONED
                request.provisioned_at = now
            else:
                attempt.result = ProvisioningResult.FAILURE
                attempt.response_code = response.status_code
                attempt.error_message = f"GitHub API returned {response.status_code}"
                request.status = RequestStatus.FAILED
                request.failure_reason = attempt.error_message
        except Exception as e:
            attempt.result = ProvisioningResult.FAILURE
            attempt.response_code = 0
            attempt.error_message = str(e)
            request.status = RequestStatus.FAILED
            request.failure_reason = str(e)

        attempt.completed_at = now
        await self.db.commit()
        await self.db.refresh(attempt)
        await self.audit.log_event(
            event_type="PROVISIONING_TEST_API",
            actor_reference="system",
            object_type="provisioning_attempt",
            object_id=attempt.id,
            payload={"request_id": request.id, "result": attempt.result.value if attempt.result else "UNKNOWN",
                      "response_code": attempt.response_code, "mode": "TEST_API"},
            correlation_id=request.correlation_id,
        )
        return attempt

    async def _call_github_api(self, team_slug: Optional[str], username: str) -> GitHubSimulatedResponse:
        if not team_slug:
            logger.warning("No GitHub team slug configured for role")
            return GitHubSimulatedResponse(400, {"error": "no team slug"})
        logger.info("Simulated GitHub API call", team_slug=team_slug, username=username)
        time.sleep(0.1)
        return GitHubSimulatedResponse(200, {"status": "simulated", "team": team_slug, "user": username})

    async def get_attempts(self, request_id: str) -> List[ProvisioningAttempt]:
        stmt = sel(ProvisioningAttempt).where(
            ProvisioningAttempt.request_id == request_id
        ).order_by(ProvisioningAttempt.attempt_number)
        result = await self.db.execute(stmt)
        return list(result.scalars().all())
