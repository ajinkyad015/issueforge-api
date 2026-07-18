import pytest
from fastapi.testclient import TestClient

from app.dependencies.project import get_project_service
from app.main import app
from app.repositories.project import InMemoryProjectRepository
from app.services.project import ProjectService



@pytest.fixture
def repository() -> InMemoryProjectRepository:
    return InMemoryProjectRepository()


@pytest.fixture
def service(repository: InMemoryProjectRepository) -> ProjectService:
    return ProjectService(repository)


@pytest.fixture
def client(service):
    app.dependency_overrides[get_project_service] = lambda: service

    with TestClient(app) as client:
        yield client

    app.dependency_overrides.clear()