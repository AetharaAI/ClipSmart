from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import os
from contextlib import asynccontextmanager

from app.core.config import get_settings
from app.core.database import engine, Base
from app.api.v1.api import api_router
from app.core.logging import setup_logging
from app.core.exceptions import (
    ValidationError,
    ProcessingError,
    AuthenticationError,
    QuotaExceededError,
)
from app.core.middleware import setup_middleware
from app.core.security import get_current_user
from app.models.user import User

# Initialize logging
setup_logging()

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager"""
    # Startup
    print("🚀 Starting ClipSmart API...")
    
    # Create database tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    print("✅ Database initialized")
    print("✅ ClipSmart API started successfully")
    
    yield
    
    # Shutdown
    print("🛑 Shutting down ClipSmart API...")


# Create FastAPI application
app = FastAPI(
    title="ClipSmart API",
    description="AI-powered video content creation platform powered by MiniMax-M2",
    version="2.0.0",
    docs_url="/docs" if settings.ENVIRONMENT != "production" else None,
    redoc_url="/redoc" if settings.ENVIRONMENT != "production" else None,
    lifespan=lifespan,
)

# Setup middleware
setup_middleware(app)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"],
    allow_headers=["*"],
)

# Add trusted host middleware for security
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=settings.ALLOWED_HOSTS,
)

# Include API routes
app.include_router(api_router, prefix="/api/v1")

# Mount static files (for serving uploaded files and exports)
if not settings.STATIC_FILES_DISABLED:
    static_files_path = "/tmp/clipsmart_static"
    os.makedirs(static_files_path, exist_ok=True)
    app.mount("/static", StaticFiles(directory=static_files_path), name="static")


# Exception handlers
@app.exception_handler(ValidationError)
async def validation_exception_handler(request, exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "success": False,
            "error": {
                "code": "VALIDATION_ERROR",
                "message": exc.detail,
                "details": exc.errors if hasattr(exc, 'errors') else None,
            }
        }
    )


@app.exception_handler(ProcessingError)
async def processing_exception_handler(request, exc: ProcessingError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "success": False,
            "error": {
                "code": "PROCESSING_ERROR",
                "message": exc.detail,
            }
        }
    )


@app.exception_handler(AuthenticationError)
async def authentication_exception_handler(request, exc: AuthenticationError):
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={
            "success": False,
            "error": {
                "code": "AUTHENTICATION_ERROR",
                "message": exc.detail,
            }
        },
        headers={"WWW-Authenticate": "Bearer"},
    )


@app.exception_handler(QuotaExceededError)
async def quota_exceeded_exception_handler(request, exc: QuotaExceededError):
    return JSONResponse(
        status_code=status.HTTP_429_TOO_MANY_REQUESTS,
        content={
            "success": False,
            "error": {
                "code": "QUOTA_EXCEEDED",
                "message": exc.detail,
            }
        }
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": {
                "code": f"HTTP_{exc.status_code}",
                "message": exc.detail,
            }
        }
    )


@app.exception_handler(Exception)
async def general_exception_handler(request, exc: Exception):
    import traceback
    import logging
    
    # Log the exception
    logging.error(f"Unhandled exception: {exc}")
    logging.error(traceback.format_exc())
    
    # Return generic error in production
    if settings.ENVIRONMENT == "production":
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "success": False,
                "error": {
                    "code": "INTERNAL_SERVER_ERROR",
                    "message": "An internal server error occurred",
                }
            }
        )
    else:
        # Return detailed error in development
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "success": False,
                "error": {
                    "code": "INTERNAL_SERVER_ERROR",
                    "message": str(exc),
                    "traceback": traceback.format_exc(),
                }
            }
        )


# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "clipsmart-api",
        "version": "2.0.0",
        "environment": settings.ENVIRONMENT,
    }


# Root endpoint
@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "service": "ClipSmart API",
        "version": "2.0.0",
        "description": "AI-powered video content creation platform powered by MiniMax-M2",
        "docs": "/docs" if settings.ENVIRONMENT != "production" else None,
        "health": "/health",
    }


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.ENVIRONMENT == "development",
        log_level="info",
        access_log=True,
    )