"""
Custom exceptions for ClipSmart application.
"""

from typing import Any, Dict, Optional


class ClipSmartException(Exception):
    """Base exception for ClipSmart application."""

    def __init__(self, detail: str, errors: Optional[Dict[str, Any]] = None):
        self.detail = detail
        self.errors = errors
        super().__init__(detail)


class ValidationError(ClipSmartException):
    """Raised when input validation fails."""
    pass


class ProcessingError(ClipSmartException):
    """Raised when video or AI processing fails."""
    pass


class AuthenticationError(ClipSmartException):
    """Raised when authentication fails."""
    pass


class QuotaExceededError(ClipSmartException):
    """Raised when user exceeds their quota."""
    pass


class ResourceNotFoundError(ClipSmartException):
    """Raised when a requested resource is not found."""
    pass


class StorageError(ClipSmartException):
    """Raised when file storage operations fail."""
    pass


class ExternalAPIError(ClipSmartException):
    """Raised when external API calls fail."""
    pass
