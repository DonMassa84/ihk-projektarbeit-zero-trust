from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class UserReferenceCreate(BaseModel):
    external_reference: str
    display_name: Optional[str] = None


class UserReferenceResponse(BaseModel):
    id: str
    external_reference: str
    display_name: Optional[str]
    active: bool


class RoleCreate(BaseModel):
    name: str
    description: Optional[str] = None
    risk_level: str = "low"
    github_team_slug: Optional[str] = None


class RoleResponse(BaseModel):
    id: str
    name: str
    description: Optional[str]
    risk_level: str
    github_team_slug: Optional[str]
    active: bool


class AccessRequestCreate(BaseModel):
    requester_reference: str = Field(..., min_length=1)
    target_user_reference: str = Field(..., min_length=1)
    requested_role_id: str = Field(..., min_length=1)
    justification: str = Field(..., min_length=10)


class AccessRequestSubmit(BaseModel):
    pass


class AccessRequestApprove(BaseModel):
    approver_reference: str = Field(..., min_length=1)
    comment: Optional[str] = None


class AccessRequestReject(BaseModel):
    approver_reference: str = Field(..., min_length=1)
    reason: str = Field(..., min_length=5)


class AccessRequestResponse(BaseModel):
    id: str
    requester_reference: str
    target_user_reference: str
    requested_role_id: str
    justification: str
    status: str
    correlation_id: str
    requested_at: Optional[datetime]
    decided_at: Optional[datetime]
    decided_by: Optional[str]
    provisioned_at: Optional[datetime]
    failure_reason: Optional[str]


class AccessRequestListResponse(BaseModel):
    requests: List[AccessRequestResponse]
    total: int


class AuditEventResponse(BaseModel):
    id: str
    event_type: str
    actor_reference: Optional[str]
    object_type: Optional[str]
    object_id: Optional[str]
    timestamp: Optional[datetime]
    payload_json: Optional[dict]
    previous_hash: Optional[str]
    event_hash: str
    correlation_id: Optional[str]


class AuditVerifyResponse(BaseModel):
    chain_valid: bool
    events_checked: int
    first_inconsistency: Optional[str]


class ProvisioningAttemptResponse(BaseModel):
    id: str
    request_id: str
    attempt_number: int
    mode: str
    result: Optional[str]
    response_code: Optional[int]
    error_message: Optional[str]


class ErrorResponse(BaseModel):
    detail: str
    code: str = "ERROR"
    correlation_id: Optional[str] = None
