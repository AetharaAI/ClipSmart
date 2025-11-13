"""
Configuration settings for ClipSmart backend application.
"""

import os
from typing import List, Optional
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # Application
    APP_NAME: str = Field(default="ClipSmart API", description="Application name")
    APP_VERSION: str = Field(default="2.0.0", description="Application version")
    ENVIRONMENT: str = Field(default="development", description="Environment (development, staging, production)")
    DEBUG: bool = Field(default=False, description="Enable debug mode")
    
    # Server
    HOST: str = Field(default="0.0.0.0", description="Server host")
    PORT: int = Field(default=8000, description="Server port")
    
    # CORS and Security
    ALLOWED_HOSTS: List[str] = Field(
        default=["http://localhost:3000", "http://localhost:8080", "https://clipsmart.aetherpro.com"],
        description="Allowed hosts for CORS"
    )
    
    # Database
    DATABASE_URL: str = Field(
        default="postgresql+asyncpg://user:password@localhost:5432/clipsmart",
        description="Database connection URL"
    )
    
    # Redis
    REDIS_URL: str = Field(
        default="redis://localhost:6379/0",
        description="Redis connection URL for Celery and caching"
    )
    
    # Authentication
    SECRET_KEY: str = Field(
        default="your-secret-key-here",
        description="Secret key for JWT tokens"
    )
    ALGORITHM: str = Field(default="HS256", description="JWT algorithm")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=30, description="Access token expiration time in minutes")
    
    # External APIs
    MINIMAX_API_KEY: str = Field(..., description="MiniMax-M2 API key")
    MINIMAX_API_BASE_URL: str = Field(
        default="https://api.minimax.chat/v1",
        description="MiniMax-M2 API base URL"
    )
    
    YOUTUBE_API_KEY: str = Field(default="", description="YouTube Data API v3 key")
    
    TAVILY_API_KEY: str = Field(default="", description="Tavily Search API key")
    
    # Supabase
    SUPABASE_URL: str = Field(..., description="Supabase project URL")
    SUPABASE_SERVICE_ROLE_KEY: str = Field(..., description="Supabase service role key")
    SUPABASE_ANON_KEY: str = Field(..., description="Supabase anonymous key")
    
    # File Storage
    UPLOAD_DIR: str = Field(default="/tmp/clipsmart/uploads", description="Upload directory")
    EXPORT_DIR: str = Field(default="/tmp/clipsmart/exports", description="Export directory")
    MAX_FILE_SIZE_MB: int = Field(default=500, description="Maximum file size in MB")
    ALLOWED_EXTENSIONS: List[str] = Field(
        default=["mp4", "mov", "avi", "webm", "mkv"],
        description="Allowed file extensions"
    )
    
    # Video Processing
    FFMPPEG_PATH: str = Field(default="ffmpeg", description="FFmpeg executable path")
    VIDEO_RESOLUTIONS: List[str] = Field(
        default=["720x1280", "1080x1920"],
        description="Supported video resolutions"
    )
    DEFAULT_FPS: int = Field(default=30, description="Default frame rate")
    
    # Celery
    CELERY_BROKER_URL: str = Field(default="redis://localhost:6379/0", description="Celery broker URL")
    CELERY_RESULT_BACKEND: str = Field(default="redis://localhost:6379/0", description="Celery result backend")
    MAX_WORKERS: int = Field(default=4, description="Maximum worker processes")
    
    # API Rate Limiting
    RATE_LIMIT_PER_MINUTE: int = Field(default=60, description="Rate limit per minute")
    RATE_LIMIT_PER_HOUR: int = Field(default=1000, description="Rate limit per hour")
    
    # Processing Quotas
    FREE_USER_MONTHLY_QUOTA: int = Field(default=10, description="Free user monthly processing quota")
    PRO_USER_MONTHLY_QUOTA: int = Field(default=100, description="Pro user monthly processing quota")
    ENTERPRISE_USER_MONTHLY_QUOTA: int = Field(default=1000, description="Enterprise user monthly processing quota")
    
    # Logging
    LOG_LEVEL: str = Field(default="INFO", description="Logging level")
    LOG_FORMAT: str = Field(
        default="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        description="Logging format"
    )
    
    # Static Files
    STATIC_FILES_DISABLED: bool = Field(default=False, description="Disable static file serving")
    
    # AI Processing
    MINIMAX_ANALYSIS_TIMEOUT: int = Field(default=30, description="MiniMax analysis timeout in seconds")
    CLIP_SENSITIVITY_DEFAULT: float = Field(default=0.75, description="Default clip extraction sensitivity")
    MAX_CLIPS_PER_VIDEO: int = Field(default=50, description="Maximum clips per video")
    MIN_CLIP_DURATION: float = Field(default=3.0, description="Minimum clip duration in seconds")
    MAX_CLIP_DURATION: float = Field(default=30.0, description="Maximum clip duration in seconds")
    
    # Performance
    CACHE_TTL: int = Field(default=3600, description="Cache TTL in seconds")
    ENABLE_CACHING: bool = Field(default=True, description="Enable response caching")
    
    # Monitoring
    SENTRY_DSN: str = Field(default="", description="Sentry DSN for error tracking")
    ENABLE_METRICS: bool = Field(default=True, description="Enable metrics collection")
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# Global settings instance
_settings = None


def get_settings() -> Settings:
    """Get or create settings instance."""
    global _settings
    if _settings is None:
        _settings = Settings()
        
        # Create necessary directories
        os.makedirs(_settings.UPLOAD_DIR, exist_ok=True)
        os.makedirs(_settings.EXPORT_DIR, exist_ok=True)
        
        # Validate required settings
        required_settings = [
            "MINIMAX_API_KEY",
            "SUPABASE_URL",
            "SUPABASE_SERVICE_ROLE_KEY",
            "SUPABASE_ANON_KEY",
        ]
        
        missing_settings = []
        for setting in required_settings:
            if not getattr(_settings, setting, None):
                missing_settings.append(setting)
        
        if missing_settings:
            raise ValueError(
                f"Missing required environment variables: {', '.join(missing_settings)}"
            )
    
    return _settings


# Environment-specific configurations
ENVIRONMENT_CONFIGS = {
    "development": {
        "DEBUG": True,
        "LOG_LEVEL": "DEBUG",
        "ALLOWED_HOSTS": ["http://localhost:3000", "http://localhost:8080", "*"],
        "STATIC_FILES_DISABLED": False,
    },
    "staging": {
        "DEBUG": False,
        "LOG_LEVEL": "INFO",
        "ALLOWED_HOSTS": ["https://staging.clipsmart.aetherpro.com"],
    },
    "production": {
        "DEBUG": False,
        "LOG_LEVEL": "WARNING",
        "ALLOWED_HOSTS": ["https://clipsmart.aetherpro.com"],
        "STATIC_FILES_DISABLED": True,  # Use CDN in production
    },
}