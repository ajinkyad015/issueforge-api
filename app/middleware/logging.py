import logging
import time
from uuid import uuid4

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from app.context.request import request_id_context

logger = logging.getLogger(__name__)


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = str(uuid4())

        request.state.request_id = request_id

        token = request_id_context.set(request_id)

        start_time = time.perf_counter()

        logger.info(
            "Incoming request: %s %s",
            request.method,
            request.url.path,
        )

        try:
            response = await call_next(request)

            duration_ms = (
                time.perf_counter() - start_time
            ) * 1000

            logger.info(
                "Completed request: %s %s | Status=%d | Duration=%.2f ms",
                request.method,
                request.url.path,
                response.status_code,
                duration_ms,
            )

            return response

        finally:
            request_id_context.reset(token)