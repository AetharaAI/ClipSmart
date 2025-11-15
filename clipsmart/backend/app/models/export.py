"""
Export database model.
"""

from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, JSON, Enum as SQLEnum, Text
from sqlalchemy.orm import relationship
import enum
import uuid

from app.core.database import Base


class ExportPlatform(str, enum.Enum):
    """Export platform."""
    TIKTOK = "tiktok"
    YOUTUBE_SHORTS = "youtube_shorts"
    INSTAGRAM_REELS = "instagram_reels"
    GENERIC = "generic"


class ExportStatus(str, enum.Enum):
    """Export processing status."""
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


class Export(Base):
    """Export model for platform-optimized videos."""

    __tablename__ = "exports"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    splice_id = Column(String, ForeignKey("splices.id", ondelete="CASCADE"), nullable=False)

    # Platform and format
    platform = Column(SQLEnum(ExportPlatform), nullable=False)
    resolution = Column(String, nullable=False)  # e.g., "720x1280", "1080x1920"
    fps = Column(Integer, nullable=False)

    # Status
    status = Column(SQLEnum(ExportStatus), default=ExportStatus.PENDING, nullable=False)
    processing_error = Column(Text, nullable=True)

    # File information
    file_path = Column(String, nullable=True)
    file_size = Column(Integer, nullable=True)  # in bytes
    file_url = Column(String, nullable=True)  # URL for download

    # Export settings
    settings = Column(JSON, nullable=True)  # Platform-specific settings
    watermark = Column(String, nullable=True)  # Watermark text or image path

    # Metadata
    duration = Column(Integer, nullable=True)  # Duration in seconds
    bitrate = Column(Integer, nullable=True)  # Bitrate in kbps

    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    completed_at = Column(DateTime, nullable=True)
    expires_at = Column(DateTime, nullable=True)  # When download link expires

    # Relationships
    user = relationship("User", back_populates="exports")
    splice = relationship("Splice", back_populates="exports")

    def __repr__(self):
        return f"<Export {self.platform} ({self.id})>"
