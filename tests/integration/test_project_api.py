from fastapi.testclient import TestClient

from app.core.settings import settings


def test_create_project_success(client: TestClient):
    response = client.post(
        "/projects",
        headers={
            "X-API-Key": settings.api_key,
        },
        json={
            "name": "IssueForge",
            "slug": "issueforge",
            "description": "Issue Tracker",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "IssueForge"
    assert data["slug"] == "issueforge"
    assert data["description"] == "Issue Tracker"
    assert "id" in data