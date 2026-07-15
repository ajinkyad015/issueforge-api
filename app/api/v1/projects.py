from datetime import datetime, timezone
from uuid import UUID, uuid4

from fastapi import APIRouter, HTTPException, status

from app.repositories.project import project_repository
from app.schemas.project import ProjectCreate, ProjectResponse


router = APIRouter()


@router.post(
    "/projects",
    response_model=ProjectResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_project(project_data: ProjectCreate) -> ProjectResponse:
    now = datetime.now(timezone.utc)

    project = ProjectResponse(
        id=uuid4(),
        name=project_data.name,
        slug=project_data.slug,
        description=project_data.description,
        created_at=now,
        updated_at=now,
    )

    return await project_repository.create(project)


@router.get(
    "/projects/{project_id}",
    response_model=ProjectResponse,
    status_code=status.HTTP_200_OK,
)
async def get_project(project_id: UUID) -> ProjectResponse:
    project = await project_repository.get_by_id(project_id)

    if project is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found",
        )

    return project