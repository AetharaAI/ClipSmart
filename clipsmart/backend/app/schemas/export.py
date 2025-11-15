"""
Export schemas for API validation.
"""

from datetime import datetime
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field


class ExportBase(BaseModel):
    """Base export schema."""
    platform: str = Field(..., regex="^(tiktok|youtube_shorts|instagram_reels|generic)$")
    resolution: str = Field(default="1080x1920")
    fps: int = Field(default=30, ge=24, le=60)


class ExportCreate(ExportBase):
    """Schema for export creation."""
    splice_id: str
    watermark: Optional[str] = None
    settings: Optional[Dict[str, Any]] = None


class ExportUpdate(BaseModel):
    """Schema for export update."""
    watermark: Optional[str] = None
    settings: Optional[Dict[str, Any]] = None


class ExportResponse(ExportBase):
    """Schema for export response."""
    id: str
    user_id: str
    splice_id: str
    status: str
    file_path: Optional[str] = None
    file_url: Optional[str] = None
    file_size: Optional[int] = None
    duration: Optional[int] = None
    created_at: datetime
    updated_at: datetime
    completed_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None

    class Config:
        from_attributes = True
