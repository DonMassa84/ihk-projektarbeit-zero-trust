from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
    database: str = "connected"
    version: str = "2.0.0"


class ReadinessResponse(BaseModel):
    ready: bool
    database: str
    audit_integrity: str
