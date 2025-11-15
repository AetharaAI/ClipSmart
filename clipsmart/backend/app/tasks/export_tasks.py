"""
Celery tasks for export processing.
"""

import logging
from app.tasks.celery_app import celery_app

logger = logging.getLogger("clipsmart.tasks.export")


@celery_app.task(name="create_export")
def create_export_task(export_id: str):
    """
    Process an export for a platform.
    """
    logger.info(f"Processing export: {export_id}")

    from app.core.database import AsyncSessionLocal
    from app.models.export import Export, ExportStatus
    from app.services.export_service import ExportService
    from sqlalchemy import select
    import asyncio

    async def _export():
        async with AsyncSessionLocal() as db:
            result = await db.execute(
                select(Export).where(Export.id == export_id)
            )
            export = result.scalar_one_or_none()

            if not export:
                logger.error(f"Export not found: {export_id}")
                return

            try:
                # Export is created in the service, this task can be used
                # for additional post-processing if needed
                logger.info(f"Export processed: {export_id}")

            except Exception as e:
                logger.error(f"Failed to process export {export_id}: {str(e)}")
                export.status = ExportStatus.FAILED
                export.processing_error = str(e)
                await db.commit()
                raise

    asyncio.run(_export())
