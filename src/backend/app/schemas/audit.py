from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class AuditLogCreate(BaseModel):
    action: str
    resource: str
    user_id: int
    details: Optional[str] = None
    result: Optional[str] = None

class AuditLogResponse(BaseModel):
    id: int
    timestamp: datetime
    action: str
    resource: str
    user_id: int
    details: Optional[str] = None
    result: Optional[str] = None

class AuditStatsResponse(BaseModel):
    total_entries: int
    actions_by_type: dict
    recent_activity: List[AuditLogResponse]
