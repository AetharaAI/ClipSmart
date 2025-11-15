"""
Export service for platform-optimized videos.
"""

import os
import logging
from datetime import datetime, timedelta
from typing import Optional, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.export import Export, ExportStatus, ExportPlatform
from app.models.splice import Splice
from app.services.video_processor import VideoProcessorService
from app.core.exceptions import ProcessingError, ValidationError
from app.core.config import get_settings

settings = get_settings()
logger = logging.getLogger("clipsmart.export")


class ExportService:
    """Service for exporting videos for different platforms."""

    def __init__(self):
        self.video_processor = VideoProcessorService()

    async def create_export(
        self,
        db: AsyncSession,
        user_id: str,
        splice_id: str,
        platform: ExportPlatform,
        resolution: str = "1080x1920",
        fps: int = 30,
        watermark: Optional[str] = None,
        settings_dict: Optional[Dict[str, Any]] = None
    ) -> Export:
        """
        Create and process an export for a specific platform.

        Args:
            db: Database session
            user_id: User ID
            splice_id: Splice ID to export
            platform: Target platform
            resolution: Output resolution
            fps: Output frame rate
            watermark: Optional watermark text
            settings_dict: Platform-specific settings

        Returns:
            Created Export object
        """
        logger.info(f"Creating {platform} export for splice {splice_id}")

        # Get splice
        result = await db.execute(
            select(Splice).where(
                Splice.id == splice_id,
                Splice.user_id == user_id
            )
        )
        splice = result.scalar_one_or_none()

        if not splice:
            raise ValidationError(f"Splice not found: {splice_id}")

        if not splice.file_path or not os.path.exists(splice.file_path):
            raise ValidationError("Splice has not been rendered yet")

        # Create export record
        export = Export(
            user_id=user_id,
            splice_id=splice_id,
            platform=platform,
            resolution=resolution,
            fps=fps,
            watermark=watermark,
            settings=settings_dict or {},
            status=ExportStatus.PENDING,
        )

        db.add(export)
        await db.commit()
        await db.refresh(export)

        try:
            # Update status
            export.status = ExportStatus.PROCESSING
            await db.commit()

            # Generate output path
            output_filename = f"export_{export.id}_{platform.value}.mp4"
            output_path = os.path.join(settings.EXPORT_DIR, output_filename)

            # Optimize for platform
            await self.video_processor.optimize_for_platform(
                input_path=splice.file_path,
                output_path=output_path,
                platform=platform.value,
                resolution=resolution,
                fps=fps,
                watermark=watermark
            )

            # Get file info
            file_size = os.path.getsize(output_path)
            metadata = await self.video_processor.get_video_metadata(output_path)

            # Update export record
            export.file_path = output_path
            export.file_size = file_size
            export.duration = int(metadata['duration'])
            export.bitrate = metadata.get('bitrate', 0)
            export.status = ExportStatus.COMPLETED
            export.completed_at = datetime.utcnow()

            # Set expiration (7 days from now)
            export.expires_at = datetime.utcnow() + timedelta(days=7)

            # In production, upload to S3/CDN and set file_url
            # For now, use local path
            export.file_url = f"/static/exports/{output_filename}"

            await db.commit()
            await db.refresh(export)

            logger.info(f"Export completed: {export.id}")
            return export

        except Exception as e:
            logger.error(f"Failed to create export: {str(e)}")
            export.status = ExportStatus.FAILED
            export.processing_error = str(e)
            await db.commit()
            raise ProcessingError(f"Failed to create export: {str(e)}")

    async def get_download_url(
        self,
        db: AsyncSession,
        export_id: str,
        user_id: str
    ) -> str:
        """
        Get download URL for an export.

        Args:
            db: Database session
            export_id: Export ID
            user_id: User ID

        Returns:
            Download URL
        """
        result = await db.execute(
            select(Export).where(
                Export.id == export_id,
                Export.user_id == user_id
            )
        )
        export = result.scalar_one_or_none()

        if not export:
            raise ValidationError(f"Export not found: {export_id}")

        if export.status != ExportStatus.COMPLETED:
            raise ValidationError("Export is not completed yet")

        if export.expires_at and datetime.utcnow() > export.expires_at:
            raise ValidationError("Export download link has expired")

        return export.file_url or ""
