from pydantic import BaseModel
from typing import Optional

class HealthResponse(BaseModel):
    status: str
    version: str = "1.0.0"
    database: Optional[str] = None
    redis: Optional[str] = None
