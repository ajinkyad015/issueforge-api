
from app.repositories.project import project_repository
from app.services.project import ProjectService


def get_project_service() -> ProjectService:
    return ProjectService(project_repository)