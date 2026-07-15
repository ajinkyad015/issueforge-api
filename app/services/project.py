from datetime import datetime, timezone
from uuid import UUID, uuid4

from app.repositories.project import ProjectRepository
from app.schemas.project import (
    ProjectCreate,
    ProjectResponse,
    ProjectUpdate,
)


class ProjectService:
    def __init__(self, repository: ProjectRepository) -> None:
        self._repository = repository

    async def create_project(
        self,
        project_data: ProjectCreate,
    ) -> ProjectResponse:
        now = datetime.now(timezone.utc)

        project = ProjectResponse(
            id=uuid4(),
            name=project_data.name,
            slug=project_data.slug,
            description=project_data.description,
            created_at=now,
            updated_at=now,
        )

        return await self._repository.create(project)

    async def get_project(
        self,
        project_id: UUID,
    ) -> ProjectResponse | None:
        return await self._repository.get_by_id(project_id)

    async def list_projects(self) -> list[ProjectResponse]:
        return await self._repository.list_all()

    async def update_project(
        self,
        project_id: UUID,
        project_data: ProjectUpdate,
    ) -> ProjectResponse | None:
        existing_project = await self._repository.get_by_id(project_id)

        if existing_project is None:
            return None

        update_data = project_data.model_dump(exclude_unset=True)

        updated_project = existing_project.model_copy(
            update={
                **update_data,
                "updated_at": datetime.now(timezone.utc),
            }
        )

        return await self._repository.update(updated_project)