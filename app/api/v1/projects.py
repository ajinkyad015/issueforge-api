from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from app.dependencies.project import get_project_service
from app.schemas.project import (
    ProjectCreate,
    ProjectResponse,
    ProjectUpdate,
)
from app.services.project import ProjectService
from app.exceptions.project import ProjectSlugAlreadyExistsError

router = APIRouter()


ProjectServiceDependency = Annotated[
    ProjectService,
    Depends(get_project_service),
]


@router.post(
    "/projects",
    response_model=ProjectResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_project(
    project_data: ProjectCreate,
    service: ProjectServiceDependency,
) -> ProjectResponse:
    try:
        return await service.create_project(project_data)

    except ProjectSlugAlreadyExistsError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        ) from exc

@router.get(
    "/projects",
    response_model=list[ProjectResponse],
    status_code=status.HTTP_200_OK,
)
async def list_projects(
    service: ProjectServiceDependency,
) -> list[ProjectResponse]:
    return await service.list_projects()


@router.get(
    "/projects/{project_id}",
    response_model=ProjectResponse,
    status_code=status.HTTP_200_OK,
)
async def get_project(
    project_id: UUID,
    service: ProjectServiceDependency,
) -> ProjectResponse:
    project = await service.get_project(project_id)

    if project is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found",
        )

    return project


@router.patch(
    "/projects/{project_id}",
    response_model=ProjectResponse,
    status_code=status.HTTP_200_OK,
)
async def update_project(
    project_id: UUID,
    project_data: ProjectUpdate,
    service: ProjectServiceDependency,
) -> ProjectResponse:
    try:
        project = await service.update_project(
            project_id=project_id,
            project_data=project_data,
        )

    except ProjectSlugAlreadyExistsError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        ) from exc

    if project is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found",
        )

    return project


@router.delete(
    "/projects/{project_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_project(
    project_id: UUID,
    service: ProjectServiceDependency,
) -> None:
    deleted = await service.delete_project(project_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found",
        )