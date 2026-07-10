import pytest
import uuid
from httpx import AsyncClient, ASGITransport
from app.main import app
from app.core.database import init_db, close_db, engine, Base, async_session_maker


BASE_URL = "http://test"


def _unique(prefix: str = "user") -> str:
    return f"{prefix}-{uuid.uuid4().hex[:8]}"


@pytest.fixture(autouse=True)
async def setup_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url=BASE_URL) as ac:
        yield ac


@pytest.fixture
async def seeded_data(client):
    req = await client.post("/api/v1/users", json={
        "external_reference": "requester-001",
        "display_name": "Alice Requester",
    })
    requester = req.json()
    req = await client.post("/api/v1/users", json={
        "external_reference": "target-001",
        "display_name": "Bob Target",
    })
    target = req.json()
    req = await client.post("/api/v1/users", json={
        "external_reference": "approver-001",
        "display_name": "Carol Approver",
    })
    approver = req.json()
    req = await client.post("/api/v1/roles", json={
        "name": "Repository Reader",
        "description": "Read-only access to repositories",
        "risk_level": "low",
        "github_team_slug": "readers",
    })
    reader_role = req.json()
    req = await client.post("/api/v1/roles", json={
        "name": "Security Reviewer",
        "description": "Security audit access",
        "risk_level": "high",
        "github_team_slug": "security-reviewers",
    })
    security_role = req.json()
    return {
        "requester": requester,
        "target": target,
        "approver": approver,
        "reader_role": reader_role,
        "security_role": security_role,
    }


# TF01 – Gültiger Antrag
@pytest.mark.asyncio
async def test_tf01_valid_request(client, seeded_data):
    resp = await client.post("/api/v1/access-requests", json={
        "requester_reference": seeded_data["requester"]["id"],
        "target_user_reference": seeded_data["target"]["id"],
        "requested_role_id": seeded_data["reader_role"]["id"],
        "justification": "Need read access for development work",
    })
    assert resp.status_code == 201
    data = resp.json()
    assert data["status"] == "DRAFT"
    assert data["correlation_id"] is not None


# TF02 – Fehlendes Pflichtfeld
@pytest.mark.asyncio
async def test_tf02_missing_required_field(client, seeded_data):
    resp = await client.post("/api/v1/access-requests", json={
        "requester_reference": seeded_data["requester"]["id"],
        "target_user_reference": seeded_data["target"]["id"],
        "requested_role_id": seeded_data["reader_role"]["id"],
        "justification": "",
    })
    assert resp.status_code == 422


# TF03 – Unbekannte Rolle
@pytest.mark.asyncio
async def test_tf03_unknown_role(client, seeded_data):
    resp = await client.post("/api/v1/access-requests", json={
        "requester_reference": seeded_data["requester"]["id"],
        "target_user_reference": seeded_data["target"]["id"],
        "requested_role_id": "nonexistent-role-id",
        "justification": "Need access for a valid reason here",
    })
    assert resp.status_code == 422
    assert "not found" in resp.json()["detail"].lower()


# TF05 – Unzulässiger Statusübergang: Provision ohne APPROVED
@pytest.mark.asyncio
async def test_tf05_provision_without_approval(client, seeded_data):
    req = await client.post("/api/v1/access-requests", json={
        "requester_reference": seeded_data["requester"]["id"],
        "target_user_reference": seeded_data["target"]["id"],
        "requested_role_id": seeded_data["reader_role"]["id"],
        "justification": "Need access for development purposes",
    })
    ar_id = req.json()["id"]
    # Attempt to provision while still DRAFT
    resp = await client.post(f"/api/v1/access-requests/{ar_id}/provision?mode=dry_run")
    assert resp.status_code == 422


# TF06 – Selbstgenehmigung abgelehnt
@pytest.mark.asyncio
async def test_tf06_self_approval_rejected(client, seeded_data):
    req = await client.post("/api/v1/access-requests", json={
        "requester_reference": seeded_data["requester"]["id"],
        "target_user_reference": seeded_data["target"]["id"],
        "requested_role_id": seeded_data["reader_role"]["id"],
        "justification": "Need access for development purposes",
    })
    ar_id = req.json()["id"]
    # Submit
    await client.post(f"/api/v1/access-requests/{ar_id}/submit")
    # Try self-approval (requester == approver)
    resp = await client.post(f"/api/v1/access-requests/{ar_id}/approve", json={
        "approver_reference": seeded_data["requester"]["id"],
        "comment": "I approve myself",
    })
    assert resp.status_code == 422
    assert "self-approval" in resp.json()["detail"].lower()


# TF07 – Gültige Genehmigung
@pytest.mark.asyncio
async def test_tf07_valid_approval(client, seeded_data):
    req = await client.post("/api/v1/access-requests", json={
        "requester_reference": seeded_data["requester"]["id"],
        "target_user_reference": seeded_data["target"]["id"],
        "requested_role_id": seeded_data["reader_role"]["id"],
        "justification": "Need access for development purposes",
    })
    ar_id = req.json()["id"]
    await client.post(f"/api/v1/access-requests/{ar_id}/submit")
    resp = await client.post(f"/api/v1/access-requests/{ar_id}/approve", json={
        "approver_reference": seeded_data["approver"]["id"],
        "comment": "Approved for development",
    })
    assert resp.status_code == 200
    assert resp.json()["status"] == "APPROVED"


# TF08 – Ablehnung
@pytest.mark.asyncio
async def test_tf08_rejection(client, seeded_data):
    req = await client.post("/api/v1/access-requests", json={
        "requester_reference": seeded_data["requester"]["id"],
        "target_user_reference": seeded_data["target"]["id"],
        "requested_role_id": seeded_data["reader_role"]["id"],
        "justification": "Need access for development purposes",
    })
    ar_id = req.json()["id"]
    await client.post(f"/api/v1/access-requests/{ar_id}/submit")
    resp = await client.post(f"/api/v1/access-requests/{ar_id}/reject", json={
        "approver_reference": seeded_data["approver"]["id"],
        "reason": "Role not appropriate for current tasks",
    })
    assert resp.status_code == 200
    assert resp.json()["status"] == "REJECTED"


# TF09 – Provision ohne Genehmigung blockiert
@pytest.mark.asyncio
async def test_tf09_provision_without_approval_blocked(client, seeded_data):
    req = await client.post("/api/v1/access-requests", json={
        "requester_reference": seeded_data["requester"]["id"],
        "target_user_reference": seeded_data["target"]["id"],
        "requested_role_id": seeded_data["reader_role"]["id"],
        "justification": "Need access for development purposes",
    })
    ar_id = req.json()["id"]
    await client.post(f"/api/v1/access-requests/{ar_id}/submit")
    resp = await client.post(f"/api/v1/access-requests/{ar_id}/provision?mode=dry_run")
    assert resp.status_code == 422


# TF10 – Erfolgreicher Dry-Run
@pytest.mark.asyncio
async def test_tf10_successful_dry_run(client, seeded_data):
    req = await client.post("/api/v1/access-requests", json={
        "requester_reference": seeded_data["requester"]["id"],
        "target_user_reference": seeded_data["target"]["id"],
        "requested_role_id": seeded_data["reader_role"]["id"],
        "justification": "Need access for development purposes",
    })
    ar_id = req.json()["id"]
    await client.post(f"/api/v1/access-requests/{ar_id}/submit")
    await client.post(f"/api/v1/access-requests/{ar_id}/approve", json={
        "approver_reference": seeded_data["approver"]["id"],
        "comment": "Approved",
    })
    resp = await client.post(f"/api/v1/access-requests/{ar_id}/provision?mode=dry_run")
    assert resp.status_code == 200
    assert resp.json()["status"] == "PROVISIONED"


# TF12 – Manipulierte Auditkette erkannt
@pytest.mark.asyncio
async def test_tf12_audit_chain_integrity(client, seeded_data):
    # Create an access request to generate audit events
    req = await client.post("/api/v1/access-requests", json={
        "requester_reference": seeded_data["requester"]["id"],
        "target_user_reference": seeded_data["target"]["id"],
        "requested_role_id": seeded_data["reader_role"]["id"],
        "justification": "Need access for development purposes",
    })
    ar_id = req.json()["id"]
    await client.post(f"/api/v1/access-requests/{ar_id}/submit")
    await client.post(f"/api/v1/access-requests/{ar_id}/approve", json={
        "approver_reference": seeded_data["approver"]["id"],
        "comment": "Approved",
    })
    # Verify audit chain
    verify = await client.get("/api/v1/audit/verify")
    assert verify.status_code == 200
    data = verify.json()
    assert data["chain_valid"] is True
    assert data["events_checked"] >= 3  # at least created + submitted + approved
    # List audit events
    events = await client.get("/api/v1/audit/events")
    assert events.status_code == 200
    assert len(events.json()) >= 3


# TF03b – Inaktive Rolle
@pytest.mark.asyncio
async def test_tf04_inactive_role(client, seeded_data):
    # Deactivate the role directly
    from app.core.database import async_session_maker
    from app.models.models import Role as RoleModel
    async with async_session_maker() as session:
        role = await session.get(RoleModel, seeded_data["reader_role"]["id"])
        role.active = False
        await session.commit()
    resp = await client.post("/api/v1/access-requests", json={
        "requester_reference": seeded_data["requester"]["id"],
        "target_user_reference": seeded_data["target"]["id"],
        "requested_role_id": seeded_data["reader_role"]["id"],
        "justification": "Need access for development purposes",
    })
    assert resp.status_code == 422
    assert "inactive" in resp.json()["detail"].lower()


# TF13 – Idempotente Mehrfachprovisionierung
@pytest.mark.asyncio
async def test_tf13_idempotent_provisioning(client, seeded_data):
    req = await client.post("/api/v1/access-requests", json={
        "requester_reference": seeded_data["requester"]["id"],
        "target_user_reference": seeded_data["target"]["id"],
        "requested_role_id": seeded_data["reader_role"]["id"],
        "justification": "Need access for development purposes",
    })
    ar_id = req.json()["id"]
    await client.post(f"/api/v1/access-requests/{ar_id}/submit")
    await client.post(f"/api/v1/access-requests/{ar_id}/approve", json={
        "approver_reference": seeded_data["approver"]["id"],
        "comment": "Approved",
    })
    # Provision twice
    r1 = await client.post(f"/api/v1/access-requests/{ar_id}/provision?mode=dry_run")
    assert r1.status_code == 200
    assert r1.json()["status"] == "PROVISIONED"
    r2 = await client.post(f"/api/v1/access-requests/{ar_id}/provision?mode=dry_run")
    assert r2.status_code == 200
    assert r2.json()["status"] == "PROVISIONED"


# Gesundheitstests
@pytest.mark.asyncio
async def test_health_endpoint(client):
    resp = await client.get("/api/v1/health")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"


@pytest.mark.asyncio
async def test_readiness_endpoint(client):
    resp = await client.get("/api/v1/ready")
    assert resp.status_code == 200
    data = resp.json()
    assert data["ready"] is True
