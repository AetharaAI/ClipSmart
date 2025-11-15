"""
Splice generation service for creating split-screen videos.
"""

import logging
from typing import List, Dict, Any, Optional
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.clip import Clip
from app.models.splice import Splice, SpliceMode, SpliceStatus, splice_clips
from app.models.video import Video
from app.services.minimax import MinimaxService
from app.services.video_processor import VideoProcessorService
from app.core.exceptions import ProcessingError, ValidationError
from app.core.config import get_settings

settings = get_settings()
logger = logging.getLogger("clipsmart.splice_generator")


class SpliceGeneratorService:
    """Service for generating AI-powered video splices."""

    def __init__(self):
        self.minimax = MinimaxService()
        self.video_processor = VideoProcessorService()

    async def generate_splice(
        self,
        db: AsyncSession,
        user_id: str,
        video_ids: List[str],
        mode: SpliceMode,
        target_duration: int,
        num_clips: int,
        layout: str = "split_screen"
    ) -> Splice:
        """
        Generate a splice using AI clip selection.

        Args:
            db: Database session
            user_id: User ID
            video_ids: List of video IDs to source clips from
            mode: Splice generation mode
            target_duration: Target duration in seconds
            num_clips: Number of clips to include
            layout: Video layout type

        Returns:
            Created Splice object
        """
        logger.info(f"Generating {mode} splice for user {user_id}")

        # Get all clips from specified videos
        result = await db.execute(
            select(Clip)
            .join(Video)
            .where(Video.id.in_(video_ids))
            .where(Video.user_id == user_id)
        )
        available_clips = result.scalars().all()

        if len(available_clips) < num_clips:
            raise ValidationError(
                f"Not enough clips available. Found {len(available_clips)}, need {num_clips}"
            )

        # Prepare clip data for AI
        clips_data = [
            {
                "id": clip.id,
                "start_time": clip.start_time,
                "end_time": clip.end_time,
                "duration": clip.duration,
                "attention_score": clip.attention_score or 0.5,
                "engagement_score": clip.engagement_score or 0.5,
                "virality_score": clip.virality_score or 0.5,
                "keywords": clip.keywords or [],
                "sentiment": clip.sentiment,
            }
            for clip in available_clips
        ]

        # Get AI recommendations
        recommendations = await self.minimax.generate_splice_recommendations(
            clips=clips_data,
            mode=mode.value,
            target_duration=target_duration,
            num_clips=num_clips
        )

        selected_clip_ids = recommendations.get("selected_clips", [])
        ai_rationale = recommendations.get("rationale", "")

        # Create splice record
        splice = Splice(
            user_id=user_id,
            title=f"{mode.value.title()} Splice - {datetime.utcnow().strftime('%Y%m%d')}",
            mode=mode,
            target_duration=target_duration,
            num_clips=num_clips,
            layout=layout,
            status=SpliceStatus.PENDING,
            generation_params=recommendations.get("params", {}),
            ai_rationale=ai_rationale,
        )

        db.add(splice)
        await db.flush()

        # Associate clips with splice
        for position, clip_id in enumerate(selected_clip_ids):
            stmt = splice_clips.insert().values(
                splice_id=splice.id,
                clip_id=clip_id,
                position=position
            )
            await db.execute(stmt)

        await db.commit()
        await db.refresh(splice)

        logger.info(f"Splice created: {splice.id}")
        return splice

    async def render_splice(
        self,
        db: AsyncSession,
        splice_id: str
    ) -> Splice:
        """
        Render a splice into a split-screen video.

        Args:
            db: Database session
            splice_id: Splice ID

        Returns:
            Updated Splice object
        """
        logger.info(f"Rendering splice: {splice_id}")

        # Get splice with clips
        result = await db.execute(
            select(Splice).where(Splice.id == splice_id)
        )
        splice = result.scalar_one_or_none()

        if not splice:
            raise ValidationError(f"Splice not found: {splice_id}")

        try:
            # Update status
            splice.status = SpliceStatus.PROCESSING
            await db.commit()

            # Get associated clips in order
            result = await db.execute(
                select(Clip, splice_clips.c.position)
                .join(splice_clips, Clip.id == splice_clips.c.clip_id)
                .where(splice_clips.c.splice_id == splice_id)
                .order_by(splice_clips.c.position)
            )
            clips_with_position = result.all()
            clips = [clip for clip, _ in clips_with_position]

            # Get parent videos for clips
            video_ids = [clip.video_id for clip in clips]
            result = await db.execute(
                select(Video).where(Video.id.in_(video_ids))
            )
            videos = {v.id: v for v in result.scalars().all()}

            # Extract individual clips to temp files
            import tempfile
            import os

            temp_clip_paths = []
            for clip in clips:
                video = videos[clip.video_id]
                temp_clip = tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix='.mp4',
                    dir=settings.UPLOAD_DIR
                )
                temp_clip.close()

                await self.video_processor.extract_clip(
                    input_path=video.file_path,
                    output_path=temp_clip.name,
                    start_time=clip.start_time,
                    end_time=clip.end_time,
                    include_audio=True
                )

                temp_clip_paths.append(temp_clip.name)

            # Generate output path
            output_filename = f"splice_{splice_id}.mp4"
            output_path = os.path.join(settings.EXPORT_DIR, output_filename)

            # Create split-screen video
            await self.video_processor.create_split_screen(
                clip_paths=temp_clip_paths,
                output_path=output_path,
                layout=splice.layout,
                resolution="1080x1920",
                fps=30
            )

            # Clean up temp files
            for temp_path in temp_clip_paths:
                try:
                    os.remove(temp_path)
                except:
                    pass

            # Get file size
            file_size = os.path.getsize(output_path)

            # Update splice record
            splice.file_path = output_path
            splice.file_size = file_size
            splice.status = SpliceStatus.COMPLETED
            splice.completed_at = datetime.utcnow()

            # Calculate actual duration
            metadata = await self.video_processor.get_video_metadata(output_path)
            splice.duration = int(metadata['duration'])

            # Generate caption and hashtags
            content_metadata = {
                "mode": splice.mode.value,
                "num_clips": splice.num_clips,
                "keywords": [kw for clip in clips for kw in (clip.keywords or [])],
            }

            caption = await self.minimax.generate_caption(content_metadata, platform="tiktok")
            hashtags = await self.minimax.generate_hashtags(content_metadata, platform="tiktok")

            splice.caption = caption
            splice.hashtags = hashtags

            await db.commit()
            await db.refresh(splice)

            logger.info(f"Splice rendered successfully: {splice_id}")
            return splice

        except Exception as e:
            logger.error(f"Failed to render splice: {str(e)}")
            splice.status = SpliceStatus.FAILED
            splice.processing_error = str(e)
            await db.commit()
            raise ProcessingError(f"Failed to render splice: {str(e)}")

    async def select_clips_by_mode(
        self,
        clips: List[Clip],
        mode: SpliceMode,
        num_clips: int
    ) -> List[Clip]:
        """
        Select clips based on generation mode (fallback if AI fails).

        Args:
            clips: Available clips
            mode: Selection mode
            num_clips: Number of clips to select

        Returns:
            Selected clips
        """
        if mode == SpliceMode.SEMANTIC:
            # Group by keywords/topics, select diverse but coherent clips
            sorted_clips = sorted(
                clips,
                key=lambda c: (c.attention_score or 0) + (c.engagement_score or 0),
                reverse=True
            )

        elif mode == SpliceMode.ECLECTIC:
            # Maximum variety - select clips with different sentiments/topics
            sorted_clips = sorted(
                clips,
                key=lambda c: len(c.keywords or []),
                reverse=True
            )

        elif mode == SpliceMode.TRENDING:
            # Highest virality potential
            sorted_clips = sorted(
                clips,
                key=lambda c: (c.virality_score or 0),
                reverse=True
            )

        else:
            sorted_clips = clips

        return sorted_clips[:num_clips]
