import time
import uuid

from starlette.middleware.base import BaseHTTPMiddleware

from app.core.logging import logger


class RequestLoggerMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        request_id = str(uuid.uuid4())[:8]

        start = time.perf_counter()

        logger.info(
            f"[{request_id}] {request.method} {request.url.path} started"
        )

        response = await call_next(request)

        elapsed = round((time.perf_counter() - start) * 1000, 2)

        logger.info(
            f"[{request_id}] "
            f"{request.method} "
            f"{request.url.path} "
            f"{response.status_code} "
            f"{elapsed} ms"
        )

        response.headers["X-Request-ID"] = request_id

        return response