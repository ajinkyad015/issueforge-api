from typing import Protocol
from uuid import UUID

from app.schemas.project import ProjectResponse


class ProjectRepository(Protocol):
    async def create(self, project: ProjectResponse) -> ProjectResponse:
        ...

    async def get_by_id(self, project_id: UUID) -> ProjectResponse | None:
        ...


class InMemoryProjectRepository:
    def __init__(self) -> None:
        self._projects: dict[UUID, ProjectResponse] = {}

    async def create(self, project: ProjectResponse) -> ProjectResponse:
        self._projects[project.id] = project
        return project

    async def get_by_id(self, project_id: UUID) -> ProjectResponse | None:
        return self._projects.get(project_id)


project_repository = InMemoryProjectRepository()