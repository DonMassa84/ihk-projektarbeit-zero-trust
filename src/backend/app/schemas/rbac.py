from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class RoleRequestCreate(BaseModel):
    user_id: int
    role_id: int
    justification: str

class RoleRequestResponse(BaseModel):
    id: int
    user_id: int
    role_id: int
    status: str
    justification: str
    created_at: datetime
    reviewed_by: Optional[int] = None
    reviewed_at: Optional[datetime] = None

class ApproveRequest(BaseModel):
    request_id: int
    reviewer_id: int
    comment: Optional[str] = None

class RejectRequest(BaseModel):
    request_id: int
    reviewer_id: int
    reason: str

class RevokeRequest(BaseModel):
    user_id: int
    role_id: int
    revoked_by: int
    reason: str

class RoleResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

class UserRoleResponse(BaseModel):
    user_id: int
    role_id: int
    role_name: str
    assigned_at: datetime
