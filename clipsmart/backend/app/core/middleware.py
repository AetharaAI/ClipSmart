"""
Middleware configuration for ClipSmart application.
"""

import time
import logging
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

logger = logging.getLogger("clipsmart.middleware")


class TimingMiddleware(BaseHTTPMiddleware):
    """Middleware to log request timing."""

    async def dispatch(self, request: Request, call_next):
        start_time = time.time()

        response = await call_next(request)

        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)

        logger.info(
            f"{request.method} {request.url.path} - "
            f"Status: {response.status_code} - "
            f"Time: {process_time:.3f}s"
        )

        return response


class RequestIDMiddleware(BaseHTTPMiddleware):
    """Middleware to add unique request ID to each request."""

    async def dispatch(self, request: Request, call_next):
        import uuid
        request_id = str(uuid.uuid4())

        # Add request ID to request state
        request.state.request_id = request_id

        response = await call_next(request)
        response.headers["X-Request-ID"] = request_id

        return response


def setup_middleware(app: FastAPI) -> None:
    """
    Configure middleware for the FastAPI application.
    """
    # Add timing middleware
    app.add_middleware(TimingMiddleware)

    # Add request ID middleware
    app.add_middleware(RequestIDMiddleware)

    logger.info("✅ Middleware configured")
