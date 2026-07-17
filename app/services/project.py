import logging
from datetime import datetime, timezone
from uuid import UUID, uuid4

from app.exceptions.project import ProjectSlugAlreadyExistsError
from app.repositories.project import ProjectRepository
from app.schemas.project import (
    ProjectCreate,
    ProjectResponse,
    ProjectUpdate,
)

logger = logging.getLogger(__name__)


class ProjectService:
    def __init__(self, repository: ProjectRepository) -> None:
        self._repository = repository

    async def create_project(
        self,
        project_data: ProjectCreate,
    ) -> ProjectResponse:
        logger.info(
            "Creating project with slug=%s",
            project_data.slug,
        )

        existing_project = await self._repository.get_by_slug(
            project_data.slug
        )

        if existing_project is not None:
            logger.warning(
                "Project creation failed. Duplicate slug=%s",
                project_data.slug,
            )
            raise ProjectSlugAlreadyExistsError(project_data.slug)

        now = datetime.now(timezone.utc)

        project = ProjectResponse(
            id=uuid4(),
            name=project_data.name,
            slug=project_data.slug,
            description=project_data.description,
            created_at=now,
            updated_at=now,
        )

        created_project = await self._repository.create(project)

        logger.info(
            "Project created successfully id=%s slug=%s",
            created_project.id,
            created_project.slug,
        )

        return created_project

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
        logger.info(
            "Updating project id=%s",
            project_id,
        )

        existing_project = await self._repository.get_by_id(project_id)

        if existing_project is None:
            logger.warning(
                "Project update failed. Project not found id=%s",
                project_id,
            )
            return None

        update_data = project_data.model_dump(exclude_unset=True)

        new_slug = update_data.get("slug")

        if new_slug is not None and new_slug != existing_project.slug:
            project_with_slug = await self._repository.get_by_slug(new_slug)

            if project_with_slug is not None:
                logger.warning(
                    "Project update failed. Duplicate slug=%s",
                    new_slug,
                )
                raise ProjectSlugAlreadyExistsError(new_slug)

        updated_project = existing_project.model_copy(
            update={
                **update_data,
                "updated_at": datetime.now(timezone.utc),
            }
        )

        updated_project = await self._repository.update(updated_project)

        logger.info(
            "Project updated successfully id=%s",
            updated_project.id,
        )

        return updated_project

    async def delete_project(
        self,
        project_id: UUID,
    ) -> bool:
        logger.info(
            "Deleting project id=%s",
            project_id,
        )

        deleted = await self._repository.delete(project_id)

        if deleted:
            logger.info(
                "Project deleted successfully id=%s",
                project_id,
            )
        else:
            logger.warning(
                "Project deletion failed. Project not found id=%s",
                project_id,
            )

        return deleted