"""
Celery tasks for video processing.
"""

import logging
from app.tasks.celery_app import celery_app

logger = logging.getLogger("clipsmart.tasks.video")


@celery_app.task(name="process_video")
def process_video_task(video_id: str):
    """
    Process a video (extract metadata, generate thumbnail).
    """
    logger.info(f"Processing video: {video_id}")

    # Import here to avoid circular dependencies
    from app.core.database import AsyncSessionLocal
    from app.services.video_processor import VideoProcessorService
    from app.models.video import Video
    from sqlalchemy import select
    import asyncio

    async def _process():
        async with AsyncSessionLocal() as db:
            result = await db.execute(
                select(Video).where(Video.id == video_id)
            )
            video = result.scalar_one_or_none()

            if not video:
                logger.error(f"Video not found: {video_id}")
                return

            try:
                processor = VideoProcessorService()

                # Generate thumbnail
                thumbnail_path = f"/tmp/clipsmart/thumbnails/{video_id}.jpg"
                await processor.generate_thumbnail(
                    video_path=video.file_path,
                    output_path=thumbnail_path
                )

                video.thumbnail_url = f"/static/thumbnails/{video_id}.jpg"
                await db.commit()

                logger.info(f"Video processed: {video_id}")

            except Exception as e:
                logger.error(f"Failed to process video {video_id}: {str(e)}")
                raise

    asyncio.run(_process())


@celery_app.task(name="analyze_video")
def analyze_video_task(video_id: str):
    """
    Analyze video with AI and extract clips.
    """
    logger.info(f"Analyzing video: {video_id}")

    from app.core.database import AsyncSessionLocal
    from app.services.minimax import MinimaxService
    from app.services.video_processor import VideoProcessorService
    from app.models.video import Video, VideoStatus
    from app.models.clip import Clip
    from app.core.config import get_settings
    from sqlalchemy import select
    from datetime import datetime
    import asyncio

    settings = get_settings()

    async def _analyze():
        async with AsyncSessionLocal() as db:
            result = await db.execute(
                select(Video).where(Video.id == video_id)
            )
            video = result.scalar_one_or_none()

            if not video:
                logger.error(f"Video not found: {video_id}")
                return

            try:
                video.status = VideoStatus.ANALYZING
                await db.commit()

                minimax = MinimaxService()

                # Analyze with AI
                analysis_result = await minimax.analyze_video(
                    video_path=video.file_path
                )

                # Extract clips
                clips_data = await minimax.extract_clips(
                    video_path=video.file_path,
                    analysis_result=analysis_result,
                    sensitivity=settings.CLIP_SENSITIVITY_DEFAULT,
                    min_duration=settings.MIN_CLIP_DURATION,
                    max_duration=settings.MAX_CLIP_DURATION,
                    max_clips=settings.MAX_CLIPS_PER_VIDEO
                )

                # Save clips
                for clip_data in clips_data:
                    clip = Clip(
                        video_id=video.id,
                        start_time=clip_data['start_time'],
                        end_time=clip_data['end_time'],
                        duration=clip_data['end_time'] - clip_data['start_time'],
                        attention_score=clip_data.get('attention_score'),
                        engagement_score=clip_data.get('engagement_score'),
                        virality_score=clip_data.get('virality_score'),
                        keywords=clip_data.get('keywords'),
                        entities=clip_data.get('entities'),
                        sentiment=clip_data.get('sentiment'),
                        caption=clip_data.get('caption'),
                    )
                    db.add(clip)

                # Update video
                video.analysis_result = analysis_result
                video.transcript = analysis_result.get('transcript')
                video.audio_analysis = analysis_result.get('audio_analysis')
                video.status = VideoStatus.ANALYZED
                video.analyzed_at = datetime.utcnow()

                await db.commit()

                logger.info(f"Video analyzed: {video_id}, extracted {len(clips_data)} clips")

            except Exception as e:
                logger.error(f"Failed to analyze video {video_id}: {str(e)}")
                video.status = VideoStatus.FAILED
                video.processing_error = str(e)
                await db.commit()
                raise

    asyncio.run(_analyze())
