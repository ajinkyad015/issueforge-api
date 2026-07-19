from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.project import Project
from app.repositories.project import ProjectRepository
from app.schemas.project import ProjectResponse


class SQLAlchemyProjectRepository(ProjectRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create(
        self,
        project: ProjectResponse,
    ) -> ProjectResponse:
        db_project = Project(
            id=project.id,
            name=project.name,
            slug=project.slug,
            description=project.description,
            created_at=project.created_at,
            updated_at=project.updated_at,
        )

        self._session.add(db_project)
        await self._session.commit()
        await self._session.refresh(db_project)

        return ProjectResponse.model_validate(db_project)

    async def get_by_id(
        self,
        project_id: UUID,
    ) -> ProjectResponse | None:
        statement = select(Project).where(Project.id == project_id)

        result = await self._session.execute(statement)
        project = result.scalar_one_or_none()

        if project is None:
            return None

        return ProjectResponse.model_validate(project)

    async def list_all(self) -> list[ProjectResponse]:
        statement = select(Project)

        result = await self._session.execute(statement)
        projects = result.scalars().all()

        return [
            ProjectResponse.model_validate(project)
            for project in projects
        ]

    async def update(
        self,
        project: ProjectResponse,
    ) -> ProjectResponse:
        statement = select(Project).where(Project.id == project.id)

        result = await self._session.execute(statement)
        db_project = result.scalar_one_or_none()

        if db_project is None:
            raise ValueError("Project not found")

        db_project.name = project.name
        db_project.slug = project.slug
        db_project.description = project.description
        db_project.updated_at = project.updated_at

        await self._session.commit()
        await self._session.refresh(db_project)

        return ProjectResponse.model_validate(db_project)

    async def delete(
        self,
        project_id: UUID,
    ) -> bool:
        statement = select(Project).where(Project.id == project_id)

        result = await self._session.execute(statement)
        project = result.scalar_one_or_none()

        if project is None:
            return False

        await self._session.delete(project)
        await self._session.commit()

        return True

    async def get_by_slug(
        self,
        slug: str,
    ) -> ProjectResponse | None:
        statement = select(Project).where(Project.slug == slug)

        result = await self._session.execute(statement)
        project = result.scalar_one_or_none()

        if project is None:
            return None

        return ProjectResponse.model_validate(project)