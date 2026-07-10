import enum
import uuid
from datetime import datetime
from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Text, Enum, JSON, Integer
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base


def generate_uuid() -> str:
    return str(uuid.uuid4())


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


class RequestStatus(str, enum.Enum):
    DRAFT = "DRAFT"
    SUBMITTED = "SUBMITTED"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    PROVISIONING = "PROVISIONING"
    PROVISIONED = "PROVISIONED"
    FAILED = "FAILED"


class ProvisioningMode(str, enum.Enum):
    DRY_RUN = "DRY_RUN"
    TEST_API = "TEST_API"


class ProvisioningResult(str, enum.Enum):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"
    SIMULATED = "SIMULATED"


class UserReference(Base):
    __tablename__ = "user_references"
    id = Column(String, primary_key=True, default=generate_uuid)
    external_reference = Column(String(255), unique=True, nullable=False, index=True)
    display_name = Column(String(255), nullable=True)
    active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())

    access_requests = relationship("AccessRequest", foreign_keys="AccessRequest.requester_reference", back_populates="requester")
    target_requests = relationship("AccessRequest", foreign_keys="AccessRequest.target_user_reference", back_populates="target_user")


class Role(Base):
    __tablename__ = "roles"
    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String(100), unique=True, nullable=False, index=True)
    description = Column(Text, nullable=True)
    risk_level = Column(String(20), default="low")
    github_team_slug = Column(String(100), nullable=True)
    active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())

    access_requests = relationship("AccessRequest", back_populates="requested_role")


class AccessRequest(Base):
    __tablename__ = "access_requests"
    id = Column(String, primary_key=True, default=generate_uuid)
    requester_reference = Column(String, ForeignKey("user_references.id"), nullable=False)
    target_user_reference = Column(String, ForeignKey("user_references.id"), nullable=False)
    requested_role_id = Column(String, ForeignKey("roles.id"), nullable=False)
    justification = Column(Text, nullable=False)
    status = Column(Enum(RequestStatus), default=RequestStatus.DRAFT, nullable=False)
    requested_at = Column(DateTime, server_default=func.now())
    decided_at = Column(DateTime, nullable=True)
    decided_by = Column(String, nullable=True)
    provisioned_at = Column(DateTime, nullable=True)
    failure_reason = Column(Text, nullable=True)
    correlation_id = Column(String(100), nullable=False, index=True)

    requester = relationship("UserReference", foreign_keys=[requester_reference], back_populates="access_requests")
    target_user = relationship("UserReference", foreign_keys=[target_user_reference], back_populates="target_requests")
    requested_role = relationship("Role", back_populates="access_requests")
    approval_decisions = relationship("ApprovalDecision", back_populates="request")
    provisioning_attempts = relationship("ProvisioningAttempt", back_populates="request")


class ApprovalDecision(Base):
    __tablename__ = "approval_decisions"
    id = Column(String, primary_key=True, default=generate_uuid)
    request_id = Column(String, ForeignKey("access_requests.id"), nullable=False)
    decision = Column(String(20), nullable=False)
    approver_reference = Column(String(100), nullable=False)
    comment = Column(Text, nullable=True)
    decided_at = Column(DateTime, server_default=func.now())

    request = relationship("AccessRequest", back_populates="approval_decisions")


class AuditEvent(Base):
    __tablename__ = "audit_events"
    id = Column(String, primary_key=True, default=generate_uuid)
    event_type = Column(String(100), nullable=False, index=True)
    actor_reference = Column(String(100), nullable=True)
    object_type = Column(String(50), nullable=True)
    object_id = Column(String, nullable=True)
    timestamp = Column(DateTime, server_default=func.now(), index=True)
    payload_json = Column(JSON, nullable=True)
    previous_hash = Column(String(64), nullable=True)
    event_hash = Column(String(64), unique=True, nullable=False)
    correlation_id = Column(String(100), nullable=True, index=True)


class ProvisioningAttempt(Base):
    __tablename__ = "provisioning_attempts"
    id = Column(String, primary_key=True, default=generate_uuid)
    request_id = Column(String, ForeignKey("access_requests.id"), nullable=False)
    attempt_number = Column(Integer, default=1)
    mode = Column(Enum(ProvisioningMode), default=ProvisioningMode.DRY_RUN)
    result = Column(Enum(ProvisioningResult), nullable=True)
    response_code = Column(Integer, nullable=True)
    error_message = Column(Text, nullable=True)
    started_at = Column(DateTime, server_default=func.now())
    completed_at = Column(DateTime, nullable=True)

    request = relationship("AccessRequest", back_populates="provisioning_attempts")


class ComplianceReport(Base):
    __tablename__ = "compliance_reports"
    id = Column(String, primary_key=True, default=generate_uuid)
    report_type = Column(String(50), nullable=False)
    status = Column(String(20), default="generating")
    findings = Column(JSON, nullable=True)
    summary = Column(Text, nullable=True)
    generated_by = Column(String, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
