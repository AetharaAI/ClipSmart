"""
Celery tasks for splice generation.
"""

import logging
from app.tasks.celery_app import celery_app

logger = logging.getLogger("clipsmart.tasks.splice")


@celery_app.task(name="render_splice")
def render_splice_task(splice_id: str):
    """
    Render a splice into a split-screen video.
    """
    logger.info(f"Rendering splice: {splice_id}")

    from app.core.database import AsyncSessionLocal
    from app.services.splice_generator import SpliceGeneratorService
    import asyncio

    async def _render():
        async with AsyncSessionLocal() as db:
            try:
                service = SpliceGeneratorService()
                splice = await service.render_splice(db=db, splice_id=splice_id)

                logger.info(f"Splice rendered: {splice_id}")
                return splice.id

            except Exception as e:
                logger.error(f"Failed to render splice {splice_id}: {str(e)}")
                raise

    asyncio.run(_render())
