from fastapi import APIRouter, HTTPException
from typing import List
from ...schemas.github import GitHubTriggerRequest, GitHubWorkflowResponse

router = APIRouter(prefix="/github", tags=["GitHub Integration"])

@router.post("/trigger", response_model=dict)
async def trigger_workflow(body: GitHubTriggerRequest):
    return {
        "status": "triggered",
        "workflow": "rbac-workflow.yml",
        "user": body.user,
        "role": body.role,
        "action": body.action,
    }

@router.post("/webhook")
async def handle_webhook():
    return {"status": "received"}

@router.get("/history", response_model=List[GitHubWorkflowResponse])
async def workflow_history():
    return [
        GitHubWorkflowResponse(
            id=1, workflow_name="rbac-workflow",
            status="completed", triggered_at="2026-07-08T00:00:00Z",
            completed_at="2026-07-08T00:05:00Z", conclusion="success",
        )
    ]
