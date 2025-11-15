"""
Logging configuration for ClipSmart application.
"""

import logging
import sys
from typing import Any
from app.core.config import get_settings

settings = get_settings()


def setup_logging() -> None:
    """
    Configure application logging.
    """
    # Configure root logger
    logging.basicConfig(
        level=getattr(logging, settings.LOG_LEVEL.upper()),
        format=settings.LOG_FORMAT,
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )

    # Set up specific loggers
    loggers = {
        "uvicorn": logging.INFO,
        "uvicorn.access": logging.INFO,
        "uvicorn.error": logging.ERROR,
        "sqlalchemy.engine": logging.WARNING if not settings.DEBUG else logging.INFO,
        "celery": logging.INFO,
    }

    for logger_name, level in loggers.items():
        logger = logging.getLogger(logger_name)
        logger.setLevel(level)

    # Create application logger
    app_logger = logging.getLogger("clipsmart")
    app_logger.setLevel(getattr(logging, settings.LOG_LEVEL.upper()))

    if settings.DEBUG:
        app_logger.info("🔧 Debug mode enabled")

    app_logger.info(f"📝 Logging configured at {settings.LOG_LEVEL} level")


def get_logger(name: str) -> logging.Logger:
    """
    Get a logger instance for the given name.
    """
    return logging.getLogger(f"clipsmart.{name}")
