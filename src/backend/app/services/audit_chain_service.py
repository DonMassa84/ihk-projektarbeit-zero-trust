import json
import hashlib
from typing import Optional, Dict, Any, List
from datetime import datetime, timezone
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from app.models.models import AuditEvent, generate_uuid


def _canonical_json(data: Any) -> str:
    return json.dumps(data, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def compute_event_hash(
    timestamp: str,
    event_type: str,
    actor_reference: Optional[str],
    object_type: Optional[str],
    object_id: Optional[str],
    payload_json: Optional[Dict[str, Any]],
    previous_hash: Optional[str],
) -> str:
    canonical = (
        str(timestamp)
        + str(event_type)
        + str(actor_reference or "")
        + str(object_type or "")
        + str(object_id or "")
        + _canonical_json(payload_json or {})
        + str(previous_hash or "")
    )
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


class AuditChainService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_last_event(self) -> Optional[AuditEvent]:
        stmt = select(AuditEvent).order_by(AuditEvent.timestamp.desc()).limit(1)
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()

    async def log_event(
        self,
        event_type: str,
        actor_reference: Optional[str] = None,
        object_type: Optional[str] = None,
        object_id: Optional[str] = None,
        payload: Optional[Dict[str, Any]] = None,
        correlation_id: Optional[str] = None,
    ) -> AuditEvent:
        last = await self.get_last_event()
        previous_hash = last.event_hash if last else None
        now = datetime.utcnow()
        timestamp = now.isoformat()
        event_hash = compute_event_hash(
            timestamp=timestamp,
            event_type=event_type,
            actor_reference=actor_reference,
            object_type=object_type,
            object_id=object_id,
            payload_json=payload,
            previous_hash=previous_hash,
        )
        event = AuditEvent(
            id=generate_uuid(),
            event_type=event_type,
            actor_reference=actor_reference,
            object_type=object_type,
            object_id=object_id,
            timestamp=now,
            payload_json=payload or {},
            previous_hash=previous_hash,
            event_hash=event_hash,
            correlation_id=correlation_id,
        )
        self.db.add(event)
        await self.db.commit()
        await self.db.refresh(event)
        return event

    async def get_events(
        self, limit: int = 100, offset: int = 0, event_type: Optional[str] = None
    ) -> List[AuditEvent]:
        stmt = select(AuditEvent).order_by(AuditEvent.timestamp.desc())
        if event_type:
            stmt = stmt.where(AuditEvent.event_type == event_type)
        stmt = stmt.limit(limit).offset(offset)
        result = await self.db.execute(stmt)
        return list(result.scalars().all())

    async def verify_chain(self) -> Dict[str, Any]:
        stmt = select(AuditEvent).order_by(AuditEvent.timestamp.asc())
        result = await self.db.execute(stmt)
        events = list(result.scalars().all())

        if not events:
            return {"chain_valid": True, "events_checked": 0, "first_inconsistency": None}

        previous_hash: Optional[str] = None
        for event in events:
            ts = event.timestamp.isoformat() if event.timestamp else ""
            expected = compute_event_hash(
                timestamp=ts,
                event_type=event.event_type,
                actor_reference=event.actor_reference,
                object_type=event.object_type,
                object_id=event.object_id,
                payload_json=event.payload_json,
                previous_hash=previous_hash,
            )
            if expected != event.event_hash:
                return {
                    "chain_valid": False,
                    "events_checked": events.index(event) + 1,
                    "first_inconsistency": f"Event {event.id}: hash mismatch (expected {expected}, stored {event.event_hash})",
                }
            if event.previous_hash != previous_hash:
                return {
                    "chain_valid": False,
                    "events_checked": events.index(event) + 1,
                    "first_inconsistency": f"Event {event.id}: previous_hash mismatch (expected {previous_hash}, stored {event.previous_hash})",
                }
            previous_hash = event.event_hash

        return {"chain_valid": True, "events_checked": len(events), "first_inconsistency": None}

    async def count_events(self) -> int:
        stmt = select(func.count()).select_from(AuditEvent)
        result = await self.db.execute(stmt)
        return result.scalar() or 0
