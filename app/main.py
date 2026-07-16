from fastapi import FastAPI

from app.api.v1.router import api_router
from app.exception_handlers import register_exception_handlers

app = FastAPI(
    title="IssueForge API",
    description="A production-style issue tracking REST API.",
    version="0.1.0",
)
register_exception_handlers(app)


app.include_router(
    api_router,
    prefix="/api/v1",
)