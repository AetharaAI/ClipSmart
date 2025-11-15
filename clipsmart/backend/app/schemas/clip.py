"""
Clip schemas for API validation.
"""

from datetime import datetime
from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field


class ClipBase(BaseModel):
    """Base clip schema."""
    title: Optional[str] = None
    description: Optional[str] = None


class ClipCreate(ClipBase):
    """Schema for clip creation."""
    video_id: str
    start_time: float = Field(..., ge=0)
    end_time: float = Field(..., ge=0)


class ClipUpdate(BaseModel):
    """Schema for clip update."""
    title: Optional[str] = None
    description: Optional[str] = None


class ClipResponse(ClipBase):
    """Schema for clip response."""
    id: str
    video_id: str
    start_time: float
    end_time: float
    duration: float
    attention_score: Optional[float] = None
    engagement_score: Optional[float] = None
    virality_score: Optional[float] = None
    keywords: Optional[List[str]] = None
    entities: Optional[Dict[str, Any]] = None
    sentiment: Optional[str] = None
    caption: Optional[str] = None
    thumbnail_url: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True
