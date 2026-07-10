from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.schemas.health import HealthResponse, ReadinessResponse
from app.services.audit_chain_service import AuditChainService

router = APIRouter(tags=["Health"])


@router.get("/health", response_model=HealthResponse)
async def health_check():
    return HealthResponse(status="ok", database="connected", version="2.0.0-pilot")


@router.get("/ready", response_model=ReadinessResponse)
async def readiness_check(db: AsyncSession = Depends(get_db)):
    audit = AuditChainService(db)
    try:
        event_count = await audit.count_events()
        chain = await audit.verify_chain()
        return ReadinessResponse(
            ready=True,
            database="connected",
            audit_integrity="valid" if chain["chain_valid"] else "invalid",
        )
    except Exception as e:
        return ReadinessResponse(
            ready=False,
            database="error",
            audit_integrity=f"check_failed: {e}",
        )
