"""
Splice database model.
"""

from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, JSON, Enum as SQLEnum, Text, Table
from sqlalchemy.orm import relationship
import enum
import uuid

from app.core.database import Base


class SpliceMode(str, enum.Enum):
    """Splice generation mode."""
    SEMANTIC = "semantic"  # Thematic coherence
    ECLECTIC = "eclectic"  # Max variety/chaos
    TRENDING = "trending"  # Viral potential


class SpliceStatus(str, enum.Enum):
    """Splice processing status."""
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


# Association table for splice-clip many-to-many relationship
splice_clips = Table(
    'splice_clips',
    Base.metadata,
    Column('splice_id', String, ForeignKey('splices.id', ondelete="CASCADE"), primary_key=True),
    Column('clip_id', String, ForeignKey('clips.id', ondelete="CASCADE"), primary_key=True),
    Column('position', Integer, nullable=False),  # Order of clip in splice
    Column('created_at', DateTime, default=datetime.utcnow, nullable=False),
)


class Splice(Base):
    """Splice model for generated split-screen videos."""

    __tablename__ = "splices"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    # Splice metadata
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    mode = Column(SQLEnum(SpliceMode), nullable=False)

    # Generation parameters
    target_duration = Column(Integer, nullable=False)  # Target duration in seconds
    num_clips = Column(Integer, nullable=False)  # Number of clips to include
    layout = Column(String, default="split_screen", nullable=False)  # Layout type

    # Status
    status = Column(SQLEnum(SpliceStatus), default=SpliceStatus.PENDING, nullable=False)
    processing_error = Column(Text, nullable=True)

    # AI Generation metadata
    generation_params = Column(JSON, nullable=True)  # Parameters used for generation
    ai_rationale = Column(Text, nullable=True)  # AI explanation for clip selection

    # File information (once rendered)
    file_path = Column(String, nullable=True)
    file_size = Column(Integer, nullable=True)  # in bytes
    duration = Column(Integer, nullable=True)  # Actual duration in seconds

    # Social media optimization
    platform_optimized = Column(JSON, nullable=True)  # {"tiktok": true, "youtube": true, etc.}
    hashtags = Column(JSON, nullable=True)  # Suggested hashtags
    caption = Column(Text, nullable=True)  # Suggested caption

    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    completed_at = Column(DateTime, nullable=True)

    # Relationships
    user = relationship("User", back_populates="splices")
    clips = relationship("Clip", secondary=splice_clips, back_populates="splices")
    exports = relationship("Export", back_populates="splice", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Splice {self.title} ({self.mode})>"
