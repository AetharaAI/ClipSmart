"""
User database model.
"""

from datetime import datetime
from sqlalchemy import Column, String, Boolean, DateTime, Integer, Enum as SQLEnum
from sqlalchemy.orm import relationship
import enum
import uuid

from app.core.database import Base


class UserTier(str, enum.Enum):
    """User subscription tier."""
    FREE = "free"
    PRO = "pro"
    ENTERPRISE = "enterprise"


class User(Base):
    """User model for authentication and authorization."""

    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=True)

    # Account status
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)

    # Subscription
    tier = Column(SQLEnum(UserTier), default=UserTier.FREE, nullable=False)
    monthly_quota_used = Column(Integer, default=0)
    quota_reset_date = Column(DateTime, nullable=True)

    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    last_login = Column(DateTime, nullable=True)

    # Relationships
    videos = relationship("Video", back_populates="user", cascade="all, delete-orphan")
    splices = relationship("Splice", back_populates="user", cascade="all, delete-orphan")
    exports = relationship("Export", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User {self.username} ({self.email})>"

    @property
    def monthly_quota_limit(self) -> int:
        """Get the monthly quota limit based on user tier."""
        from app.core.config import get_settings
        settings = get_settings()

        quotas = {
            UserTier.FREE: settings.FREE_USER_MONTHLY_QUOTA,
            UserTier.PRO: settings.PRO_USER_MONTHLY_QUOTA,
            UserTier.ENTERPRISE: settings.ENTERPRISE_USER_MONTHLY_QUOTA,
        }
        return quotas.get(self.tier, 10)

    @property
    def has_quota_remaining(self) -> bool:
        """Check if user has quota remaining."""
        # Reset quota if needed
        if self.quota_reset_date and datetime.utcnow() > self.quota_reset_date:
            return True
        return self.monthly_quota_used < self.monthly_quota_limit

    def consume_quota(self, amount: int = 1) -> None:
        """Consume user quota."""
        self.monthly_quota_used += amount
