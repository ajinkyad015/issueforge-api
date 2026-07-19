"""this dependancy was designed for inmemory project response method without the actual db"""
# from app.repositories.project import project_repository
# from app.services.project import ProjectService



# def get_project_service() -> ProjectService:
#     return ProjectService(project_repository)

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.repositories.sqlalchemy_project import (
    SQLAlchemyProjectRepository,
)
from app.services.project import ProjectService


def get_project_service(
    session: AsyncSession = Depends(get_db),
) -> ProjectService:

    repository = SQLAlchemyProjectRepository(session)

    return ProjectService(repository)