import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app


@pytest.fixture
def client():
    transport = ASGITransport(app=app)
    return AsyncClient(transport=transport, base_url="http://test")


@pytest.mark.asyncio
async def test_health_endpoint(client):
    response = await client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"


@pytest.mark.asyncio
async def test_login_success(client):
    response = await client.post("/api/v1/auth/login", json={"username": "admin", "password": "admin"})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data


@pytest.mark.asyncio
async def test_login_failure(client):
    response = await client.post("/api/v1/auth/login", json={"username": "admin", "password": "wrong"})
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_rbac_list_roles(client):
    response = await client.get("/api/v1/rbac/roles")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 6


@pytest.mark.asyncio
async def test_audit_logs(client):
    response = await client.get("/api/v1/audit/logs")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


@pytest.mark.asyncio
async def test_audit_stats(client):
    response = await client.get("/api/v1/audit/stats")
    assert response.status_code == 200
    data = response.json()
    assert "total_entries" in data


@pytest.mark.asyncio
async def test_github_trigger(client):
    response = await client.post(
        "/api/v1/github/trigger",
        json={"user": "testuser", "role": "Developer", "action": "grant"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "triggered"


@pytest.mark.asyncio
async def test_ml_anomaly(client):
    response = await client.post(
        "/api/v1/ml/anomaly",
        json={"event_type": "login", "user_id": 1, "resource": "/api/admin"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "is_anomaly" in data


@pytest.mark.asyncio
async def test_rbac_workflow(client):
    create_resp = await client.post(
        "/api/v1/rbac/request",
        json={"user_id": 1, "role_id": 2, "justification": "Need for project"},
    )
    assert create_resp.status_code == 200
    req_id = create_resp.json()["id"]

    approve_resp = await client.post(
        "/api/v1/rbac/approve",
        json={"request_id": req_id, "reviewer_id": 1, "comment": "Approved"},
    )
    assert approve_resp.status_code == 200
    assert approve_resp.json()["status"] == "approved"
