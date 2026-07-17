import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.v1.router import api_router
from app.core.config import settings
from app.core.logging import setup_logging
from app.exception_handlers import register_exception_handlers
from app.middleware.logging import RequestLoggingMiddleware

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()

    logger.info("Starting IssueForge API...")

    # Example application resource
    app.state.started_at = "Application Started"

    logger.info("Application resources initialized.")

    yield

    logger.info("Cleaning up application resources...")

    del app.state.started_at

    logger.info("Application shutdown complete.")


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    lifespan=lifespan,
)

app.add_middleware(RequestLoggingMiddleware)

register_exception_handlers(app)

app.include_router(api_router)