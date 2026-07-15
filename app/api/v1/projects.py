from uuid import UUID

from fastapi import APIRouter, HTTPException, status

from app.repositories.project import project_repository
from app.schemas.project import ProjectCreate, ProjectResponse
from app.services.project import ProjectService


router = APIRouter()

project_service = ProjectService(project_repository)


@router.post(
    "/projects",
    response_model=ProjectResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_project(project_data: ProjectCreate) -> ProjectResponse:
    return await project_service.create_project(project_data)


@router.get(
    "/projects/{project_id}",
    response_model=ProjectResponse,
    status_code=status.HTTP_200_OK,
)
async def get_project(project_id: UUID) -> ProjectResponse:
    project = await project_service.get_project(project_id)

    if project is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found",
        )

    return project