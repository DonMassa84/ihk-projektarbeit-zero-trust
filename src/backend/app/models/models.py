from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text, Enum, JSON, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base
import enum
import uuid


def generate_uuid() -> str:
    return str(uuid.uuid4())


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=generate_uuid)
    email = Column(String(255), unique=True, nullable=False, index=True)
    display_name = Column(String(255), nullable=False)
    azure_ad_id = Column(String(255), unique=True, nullable=True, index=True)
    department = Column(String(100), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    role_assignments = relationship("UserRoleAssignment", back_populates="user")
    audit_logs = relationship("AuditLog", back_populates="user")
    role_requests = relationship("RoleRequest", back_populates="user")


class Role(Base):
    __tablename__ = "roles"

    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String(100), unique=True, nullable=False, index=True)
    description = Column(Text, nullable=True)
    hierarchy_level = Column(Integer, default=100)
    is_system_role = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    assignments = relationship("UserRoleAssignment", back_populates="role")
    policies = relationship("RolePolicy", back_populates="role")
    requests = relationship("RoleRequest", back_populates="role")


class UserRoleAssignment(Base):
    __tablename__ = "user_role_assignments"

    id = Column(String, primary_key=True, default=generate_uuid)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    role_id = Column(String, ForeignKey("roles.id"), nullable=False)
    grant_start = Column(DateTime(timezone=True), server_default=func.now())
    grant_end = Column(DateTime(timezone=True), nullable=True)
    granted_by = Column(String, ForeignKey("users.id"), nullable=True)
    revoke_reason = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="role_assignments", foreign_keys=[user_id])
    role = relationship("Role", back_populates="assignments")


class Policy(Base):
    __tablename__ = "policies"

    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String(200), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    policy_type = Column(String(50), nullable=False)
    rules_json = Column(JSON, nullable=False)
    version = Column(Integer, default=1)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class RolePolicy(Base):
    __tablename__ = "role_policies"

    id = Column(String, primary_key=True, default=generate_uuid)
    role_id = Column(String, ForeignKey("roles.id"), nullable=False)
    policy_id = Column(String, ForeignKey("policies.id"), nullable=False)

    role = relationship("Role", back_populates="policies")
    policy = relationship("Policy")


class RoleRequest(Base):
    __tablename__ = "role_requests"

    id = Column(String, primary_key=True, default=generate_uuid)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    role_id = Column(String, ForeignKey("roles.id"), nullable=False)
    status = Column(Enum("pending", "approved", "rejected", "cancelled", name="request_status"), default="pending")
    justification = Column(Text, nullable=True)
    reviewed_by = Column(String, ForeignKey("users.id"), nullable=True)
    review_comment = Column(Text, nullable=True)
    github_workflow_run_id = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    user = relationship("User", back_populates="role_requests", foreign_keys=[user_id])
    role = relationship("Role", back_populates="requests")


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(String, primary_key=True, default=generate_uuid)
    user_id = Column(String, ForeignKey("users.id"), nullable=True, index=True)
    action = Column(String(100), nullable=False, index=True)
    resource_type = Column(String(50), nullable=True)
    resource_id = Column(String, nullable=True)
    details = Column(JSON, nullable=True)
    ip_address = Column(String(45), nullable=True)
    user_agent = Column(String(500), nullable=True)
    result = Column(String(20), default="success")
    anomaly_score = Column(Float, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), index=True)

    user = relationship("User", back_populates="audit_logs")


class GitHubWorkflow(Base):
    __tablename__ = "github_workflows"

    id = Column(String, primary_key=True, default=generate_uuid)
    workflow_name = Column(String(200), nullable=False)
    run_id = Column(String, unique=True, nullable=True)
    trigger_type = Column(String(50), nullable=False)
    status = Column(String(20), default="pending")
    payload = Column(JSON, nullable=True)
    result = Column(JSON, nullable=True)
    started_at = Column(DateTime(timezone=True), server_default=func.now())
    completed_at = Column(DateTime(timezone=True), nullable=True)


class ComplianceReport(Base):
    __tablename__ = "compliance_reports"

    id = Column(String, primary_key=True, default=generate_uuid)
    report_type = Column(String(50), nullable=False)
    status = Column(String(20), default="generating")
    findings = Column(JSON, nullable=True)
    summary = Column(Text, nullable=True)
    generated_by = Column(String, ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())