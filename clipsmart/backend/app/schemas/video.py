"""
Video schemas for API validation.
"""

from datetime import datetime
from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field, HttpUrl


class VideoBase(BaseModel):
    """Base video schema."""
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = None


class VideoCreate(VideoBase):
    """Schema for video creation."""
    source_type: str = Field(default="upload")
    source_url: Optional[str] = None


class VideoUpdate(BaseModel):
    """Schema for video update."""
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = None


class VideoResponse(VideoBase):
    """Schema for video response."""
    id: str
    user_id: str
    source_type: str
    source_url: Optional[str] = None
    filename: str
    file_size: int
    duration: float
    width: Optional[int] = None
    height: Optional[int] = None
    fps: Optional[float] = None
    status: str
    thumbnail_url: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    analyzed_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class VideoAnalysisResponse(BaseModel):
    """Schema for video analysis results."""
    video_id: str
    analysis_result: Optional[Dict[str, Any]] = None
    transcript: Optional[str] = None
    audio_analysis: Optional[Dict[str, Any]] = None
    clips_extracted: int
    status: str

    class Config:
        from_attributes = True


class VideoUploadResponse(BaseModel):
    """Schema for video upload response."""
    success: bool
    video_id: str
    message: str
    upload_url: Optional[str] = None
