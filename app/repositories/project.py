from typing import Protocol
from uuid import UUID

from app.schemas.project import ProjectResponse


class ProjectRepository(Protocol):
    async def create(
        self,
        project: ProjectResponse,
    ) -> ProjectResponse:
        ...

    async def get_by_id(
        self,
        project_id: UUID,
    ) -> ProjectResponse | None:
        ...

    async def list_all(self) -> list[ProjectResponse]:
        ...

    async def update(
        self,
        project: ProjectResponse,
    ) -> ProjectResponse:
        ...
    async def delete(self, project_id: UUID) -> bool:
        ...
    async def get_by_slug(self, slug: str) -> ProjectResponse | None:
        ...


class InMemoryProjectRepository:
    def __init__(self) -> None:
        self._projects: dict[UUID, ProjectResponse] = {}


    async def create(
        self,
        project: ProjectResponse,
    ) -> ProjectResponse:
        self._projects[project.id] = project
        return project


    async def get_by_id(
        self,
        project_id: UUID,
    ) -> ProjectResponse | None:
        return self._projects.get(project_id)


    async def list_all(self) -> list[ProjectResponse]:
        return list(self._projects.values())


    async def update(
        self,
        project: ProjectResponse,
    ) -> ProjectResponse:
        self._projects[project.id] = project
        return project


    async def delete(self, project_id: UUID) -> bool:       
        if project_id not in self._projects:
            return False

        del self._projects[project_id]
        return True


    async def get_by_slug(self, slug: str) -> ProjectResponse | None:
        for project in self._projects.values():
            if project.slug == slug:
                return project

        return None


project_repository = InMemoryProjectRepository()