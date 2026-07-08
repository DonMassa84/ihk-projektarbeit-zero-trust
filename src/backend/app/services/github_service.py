from typing import Optional, Dict, Any, List
from datetime import datetime
from github import Github, GithubIntegration
from github.GithubException import GithubException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.config import settings
from app.models.models import GitHubWorkflow
from app.services.audit_service import AuditService
import structlog
import json
import hmac
import hashlib

logger = structlog.get_logger()


class GitHubService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.audit = AuditService(db)
        self._client = None
        self._app = None

    @property
    def client(self) -> Optional[Github]:
        if not self._client and settings.GITHUB_APP_ID:
            try:
                private_key = settings.GITHUB_APP_PRIVATE_KEY
                if private_key:
                    integration = GithubIntegration(
                        app_id=settings.GITHUB_APP_ID,
                        private_key=private_key,
                    )
                    if settings.GITHUB_APP_INSTALLATION_ID:
                        self._client = integration.get_installation(
                            int(settings.GITHUB_APP_INSTALLATION_ID)
                        )
            except Exception as e:
                logger.error("Failed to initialize GitHub client", error=str(e))
        return self._client

    async def trigger_rbac_workflow(
        self,
        user_login: str,
        role_name: str,
        action: str = "grant",
        repo_name: str = "zero-trust-github-integration",
    ) -> dict:
        workflow_run = GitHubWorkflow(
            workflow_name="RBAC Auto-Provisioning",
            trigger_type="rbac_provisioning",
            status="pending",
            payload={
                "user": user_login,
                "role": role_name,
                "action": action,
                "repo": repo_name,
            },
        )
        self.db.add(workflow_run)
        await self.db.commit()
        await self.db.refresh(workflow_run)

        if not self.client:
            workflow_run.status = "simulated"
            workflow_run.result = {
                "message": f"GitHub integration not configured. Simulated: {action} {role_name} for {user_login}",
                "simulated": True,
            }
            await self.db.commit()

            await self.audit.log(
                user_id=None,
                action="GITHUB_WORKFLOW_SIMULATED",
                resource_type="workflow",
                resource_id=workflow_run.id,
                details=workflow_run.payload,
            )

            return workflow_run.result

        try:
            repo = self.client.get_repo(f"DonMassa84/{repo_name}")
            workflow = repo.get_workflow("rbac-workflow.yml")
            dispatch = workflow.create_dispatch(
                ref="main",
                inputs={
                    "user": user_login,
                    "role": role_name,
                    "action": action,
                },
            )

            workflow_run.status = "dispatched"
            workflow_run.result = {"github_dispatch": "success"}
            await self.db.commit()

        except GithubException as e:
            workflow_run.status = "failed"
            workflow_run.result = {"error": str(e)}
            await self.db.commit()

            await self.audit.log(
                user_id=None,
                action="GITHUB_WORKFLOW_FAILED",
                resource_type="workflow",
                resource_id=workflow_run.id,
                details={"error": str(e)},
                result="failure",
            )

        return workflow_run.result

    async def verify_webhook(self, payload: bytes, signature: str) -> bool:
        if not settings.GITHUB_WEBHOOK_SECRET:
            return True
        secret = settings.GITHUB_WEBHOOK_SECRET.encode()
        expected = hmac.new(secret, payload, hashlib.sha256).hexdigest()
        return hmac.compare_digest(f"sha256={expected}", signature)

    async def handle_webhook(self, event: str, payload: Dict[str, Any]) -> dict:
        action = payload.get("action", "")
        logger.info("Webhook received", event=event, action=action)

        workflow_entry = GitHubWorkflow(
            workflow_name=f"webhook_{event}",
            trigger_type="webhook",
            status="received",
            payload=payload,
        )
        self.db.add(workflow_entry)
        await self.db.commit()

        if event == "pull_request" and action == "opened":
            await self._handle_pr_opened(payload)

        elif event == "pull_request" and action == "closed":
            await self._handle_pr_closed(payload)

        return {"status": "processed", "workflow_id": workflow_entry.id}

    async def _handle_pr_opened(self, payload: Dict[str, Any]) -> None:
        pr = payload.get("pull_request", {})
        title = pr.get("title", "")
        user = pr.get("user", {}).get("login", "")

        if "[ROLE]" in title:
            await self.audit.log(
                user_id=None,
                action="PR_ROLE_REQUEST_DETECTED",
                resource_type="pull_request",
                resource_id=str(pr.get("number")),
                details={"title": title, "author": user},
            )

    async def _handle_pr_closed(self, payload: Dict[str, Any]) -> None:
        pr = payload.get("pull_request", {})
        merged = pr.get("merged", False)
        if merged and "[ROLE]" in pr.get("title", ""):
            await self.audit.log(
                user_id=None,
                action="PR_ROLE_REQUEST_MERGED",
                resource_type="pull_request",
                resource_id=str(pr.get("number")),
                details={"title": pr.get("title")},
            )

    async def get_workflow_history(self, limit: int = 20) -> List[dict]:
        stmt = (
            select(GitHubWorkflow)
            .order_by(GitHubWorkflow.started_at.desc())
            .limit(limit)
        )
        result = await self.db.execute(stmt)
        workflows = result.scalars().all()

        return [
            {
                "id": w.id,
                "workflow_name": w.workflow_name,
                "trigger_type": w.trigger_type,
                "status": w.status,
                "started_at": w.started_at.isoformat() if w.started_at else None,
                "completed_at": w.completed_at.isoformat() if w.completed_at else None,
                "result": w.result,
            }
            for w in workflows
        ]