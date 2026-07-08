from typing import Optional, Dict, Any, List
from datetime import datetime, timedelta
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, and_
from sqlalchemy.orm import selectinload
from app.models.models import AuditLog


class AuditService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def log(
        self,
        user_id: Optional[str],
        action: str,
        resource_type: Optional[str] = None,
        resource_id: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None,
        ip_address: Optional[str] = None,
        user_agent: Optional[str] = None,
        result: str = "success",
        anomaly_score: Optional[float] = None,
    ) -> AuditLog:
        entry = AuditLog(
            user_id=user_id,
            action=action,
            resource_type=resource_type,
            resource_id=resource_id,
            details=details or {},
            ip_address=ip_address,
            user_agent=user_agent,
            result=result,
            anomaly_score=anomaly_score,
        )
        self.db.add(entry)
        await self.db.commit()
        await self.db.refresh(entry)
        return entry

    async def get_user_logs(
        self,
        user_id: str,
        limit: int = 50,
        offset: int = 0,
        action_filter: Optional[str] = None,
    ) -> dict:
        stmt = select(AuditLog).where(AuditLog.user_id == user_id)
        if action_filter:
            stmt = stmt.where(AuditLog.action == action_filter)
        stmt = stmt.order_by(AuditLog.created_at.desc()).limit(limit).offset(offset)

        result = await self.db.execute(stmt)
        logs = result.scalars().all()

        count_stmt = select(func.count()).select_from(AuditLog).where(AuditLog.user_id == user_id)
        if action_filter:
            count_stmt = count_stmt.where(AuditLog.action == action_filter)
        total = await self.db.execute(count_stmt)

        return {
            "logs": [
                {
                    "id": entry.id,
                    "action": entry.action,
                    "resource_type": entry.resource_type,
                    "resource_id": entry.resource_id,
                    "details": entry.details,
                    "result": entry.result,
                    "anomaly_score": entry.anomaly_score,
                    "timestamp": entry.created_at.isoformat() if entry.created_at else None,
                }
                for entry in logs
            ],
            "total": total.scalar(),
            "limit": limit,
            "offset": offset,
        }

    async def get_recent_activities(
        self, 
        limit: int = 20,
        only_anomalies: bool = False,
        min_anomaly_score: float = 0.7,
    ) -> List[dict]:
        stmt = select(AuditLog).options(selectinload(AuditLog.user))
        if only_anomalies:
            stmt = stmt.where(AuditLog.anomaly_score >= min_anomaly_score)
        stmt = stmt.order_by(AuditLog.created_at.desc()).limit(limit)

        result = await self.db.execute(stmt)
        logs = result.scalars().all()

        return [
            {
                "id": entry.id,
                "user": entry.user.display_name if entry.user else "System",
                "action": entry.action,
                "resource_type": entry.resource_type,
                "details": entry.details,
                "result": entry.result,
                "is_anomaly": (entry.anomaly_score or 0) >= min_anomaly_score,
                "anomaly_score": entry.anomaly_score,
                "timestamp": entry.created_at.isoformat() if entry.created_at else None,
            }
            for entry in logs
        ]

    async def get_audit_stats(self, days: int = 30) -> dict:
        since = datetime.utcnow() - timedelta(days=days)
        stmt = (
            select(
                AuditLog.action,
                AuditLog.result,
                func.count().label("count"),
            )
            .where(AuditLog.created_at >= since)
            .group_by(AuditLog.action, AuditLog.result)
        )
        result = await self.db.execute(stmt)
        rows = result.fetchall()

        actions = {}
        for action, result_status, count in rows:
            if action not in actions:
                actions[action] = {"success": 0, "failure": 0, "total": 0}
            actions[action][result_status] = count
            actions[action]["total"] += count

        anomaly_count = await self.db.execute(
            select(func.count()).select_from(AuditLog).where(
                and_(
                    AuditLog.created_at >= since,
                    AuditLog.anomaly_score >= 0.7,
                )
            )
        )

        return {
            "total_events": sum(a["total"] for a in actions.values()),
            "unique_actions": len(actions),
            "anomalies_detected": anomaly_count.scalar() or 0,
            "actions_breakdown": actions,
            "period_days": days,
        }