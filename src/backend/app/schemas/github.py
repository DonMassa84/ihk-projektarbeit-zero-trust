from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class GitHubTriggerRequest(BaseModel):
    user: str
    role: str
    action: str

class GitHubWorkflowResponse(BaseModel):
    id: int
    workflow_name: str
    status: str
    triggered_at: datetime
    completed_at: Optional[datetime] = None
    conclusion: Optional[str] = None
