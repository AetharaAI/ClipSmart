"""
Splice schemas for API validation.
"""

from datetime import datetime
from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field


class SpliceBase(BaseModel):
    """Base splice schema."""
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = None
    mode: str = Field(..., regex="^(semantic|eclectic|trending)$")


class SpliceCreate(SpliceBase):
    """Schema for splice creation."""
    clip_ids: List[str] = Field(..., min_items=2, max_items=20)
    target_duration: int = Field(..., ge=15, le=60)
    layout: str = Field(default="split_screen")


class SpliceUpdate(BaseModel):
    """Schema for splice update."""
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = None


class SpliceResponse(SpliceBase):
    """Schema for splice response."""
    id: str
    user_id: str
    num_clips: int
    target_duration: int
    layout: str
    status: str
    file_path: Optional[str] = None
    file_size: Optional[int] = None
    duration: Optional[int] = None
    hashtags: Optional[List[str]] = None
    caption: Optional[str] = None
    ai_rationale: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    completed_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class SpliceGenerateRequest(BaseModel):
    """Schema for AI-powered splice generation."""
    video_ids: List[str] = Field(..., min_items=1, max_items=10)
    mode: str = Field(..., regex="^(semantic|eclectic|trending)$")
    target_duration: int = Field(..., ge=15, le=60)
    num_clips: int = Field(default=3, ge=2, le=10)
    layout: str = Field(default="split_screen")
