"""
Clip database model.
"""

from datetime import datetime
from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey, JSON, Text
from sqlalchemy.orm import relationship
import uuid

from app.core.database import Base


class Clip(Base):
    """Clip model for extracted video segments."""

    __tablename__ = "clips"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    video_id = Column(String, ForeignKey("videos.id", ondelete="CASCADE"), nullable=False)

    # Clip metadata
    title = Column(String, nullable=True)
    description = Column(Text, nullable=True)

    # Timing
    start_time = Column(Float, nullable=False)  # in seconds
    end_time = Column(Float, nullable=False)  # in seconds
    duration = Column(Float, nullable=False)  # in seconds

    # AI scoring
    attention_score = Column(Float, nullable=True)  # 0-1 score from MiniMax-M2
    engagement_score = Column(Float, nullable=True)  # 0-1 score
    virality_score = Column(Float, nullable=True)  # 0-1 score

    # Content analysis
    keywords = Column(JSON, nullable=True)  # List of keywords
    entities = Column(JSON, nullable=True)  # Detected entities
    sentiment = Column(String, nullable=True)  # positive/negative/neutral
    caption = Column(Text, nullable=True)  # Auto-generated caption

    # File information (for pre-extracted clips)
    file_path = Column(String, nullable=True)
    thumbnail_url = Column(String, nullable=True)

    # Metadata
    metadata = Column(JSON, nullable=True)  # Additional metadata from AI

    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationships
    video = relationship("Video", back_populates="clips")
    splices = relationship("Splice", secondary="splice_clips", back_populates="clips")

    def __repr__(self):
        return f"<Clip {self.id} ({self.start_time}s-{self.end_time}s)>"
