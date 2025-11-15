"""
Video database model.
"""

from datetime import datetime
from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey, JSON, Enum as SQLEnum, Text
from sqlalchemy.orm import relationship
import enum
import uuid

from app.core.database import Base


class VideoStatus(str, enum.Enum):
    """Video processing status."""
    UPLOADING = "uploading"
    UPLOADED = "uploaded"
    ANALYZING = "analyzing"
    ANALYZED = "analyzed"
    FAILED = "failed"


class VideoSource(str, enum.Enum):
    """Video source type."""
    UPLOAD = "upload"
    YOUTUBE = "youtube"
    URL = "url"


class Video(Base):
    """Video model for uploaded and processed videos."""

    __tablename__ = "videos"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    # Video metadata
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    source_type = Column(SQLEnum(VideoSource), default=VideoSource.UPLOAD, nullable=False)
    source_url = Column(String, nullable=True)  # For YouTube or URL sources

    # File information
    filename = Column(String, nullable=False)
    file_path = Column(String, nullable=False)
    file_size = Column(Integer, nullable=False)  # in bytes
    mime_type = Column(String, nullable=False)

    # Video properties
    duration = Column(Float, nullable=False)  # in seconds
    width = Column(Integer, nullable=True)
    height = Column(Integer, nullable=True)
    fps = Column(Float, nullable=True)
    codec = Column(String, nullable=True)

    # Processing status
    status = Column(SQLEnum(VideoStatus), default=VideoStatus.UPLOADED, nullable=False)
    processing_error = Column(Text, nullable=True)

    # AI Analysis results
    analysis_result = Column(JSON, nullable=True)  # MiniMax-M2 analysis
    transcript = Column(Text, nullable=True)
    audio_analysis = Column(JSON, nullable=True)

    # Thumbnails
    thumbnail_url = Column(String, nullable=True)

    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    analyzed_at = Column(DateTime, nullable=True)

    # Relationships
    user = relationship("User", back_populates="videos")
    clips = relationship("Clip", back_populates="video", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Video {self.title} ({self.id})>"
