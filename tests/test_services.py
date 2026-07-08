import pytest
from app.services.audit_service import AuditService
from app.services.github_service import GitHubService


@pytest.mark.asyncio
async def test_audit_service_importable():
    assert AuditService is not None


@pytest.mark.asyncio
async def test_github_service_importable():
    assert GitHubService is not None
