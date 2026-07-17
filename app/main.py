from fastapi import FastAPI

from app.api.v1.router import api_router
from app.exception_handlers import register_exception_handlers

from app.core.config import settings

from app.core.logging import setup_logging

setup_logging()


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)
register_exception_handlers(app)


app.include_router(
    api_router,
    prefix="/api/v1",
)