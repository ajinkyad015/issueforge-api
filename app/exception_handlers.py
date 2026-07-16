from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.exceptions.project import ProjectSlugAlreadyExistsError


async def project_slug_already_exists_handler(
    request: Request,
    exc: ProjectSlugAlreadyExistsError,
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={
            "detail": str(exc),
        },
    )


def register_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(
        ProjectSlugAlreadyExistsError,
        project_slug_already_exists_handler,
    )