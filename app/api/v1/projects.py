from datetime import datetime, timezone
from uuid import uuid4

from fastapi import APIRouter, status

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

    return project