"""
Video endpoints.
"""

import os
import shutil
from datetime import datetime
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, Form
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc

from app.core.database import get_db
from app.core.security import get_current_user
from app.core.exceptions import ValidationError, ProcessingError, QuotaExceededError
from app.models.user import User
from app.models.video import Video, VideoStatus, VideoSource
from app.models.clip import Clip
from app.schemas.video import VideoCreate, VideoResponse, VideoUpdate, VideoAnalysisResponse
from app.services.video_processor import VideoProcessorService
from app.services.minimax import MinimaxService
from app.core.config import get_settings

settings = get_settings()
router = APIRouter()
video_processor = VideoProcessorService()
minimax_service = MinimaxService()


@router.post("/upload", response_model=VideoResponse, status_code=status.HTTP_201_CREATED)
async def upload_video(
    file: UploadFile = File(...),
    title: str = Form(...),
    description: Optional[str] = Form(None),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Upload a video file.
    """
    # Check quota
    if not current_user.has_quota_remaining:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Monthly quota exceeded"
        )

    # Validate file type
    if not file.content_type or not file.content_type.startswith('video/'):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="File must be a video"
        )

    # Check file extension
    file_ext = os.path.splitext(file.filename)[1].lower().replace('.', '')
    if file_ext not in settings.ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"File type not allowed. Allowed: {', '.join(settings.ALLOWED_EXTENSIONS)}"
        )

    # Save uploaded file
    import uuid
    file_id = str(uuid.uuid4())
    filename = f"{file_id}.{file_ext}"
    file_path = os.path.join(settings.UPLOAD_DIR, filename)

    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Get file size
        file_size = os.path.getsize(file_path)

        # Check file size
        max_size = settings.MAX_FILE_SIZE_MB * 1024 * 1024
        if file_size > max_size:
            os.remove(file_path)
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"File too large. Maximum size: {settings.MAX_FILE_SIZE_MB}MB"
            )

        # Extract metadata
        metadata = await video_processor.get_video_metadata(file_path)

        # Create video record
        video = Video(
            user_id=current_user.id,
            title=title,
            description=description,
            source_type=VideoSource.UPLOAD,
            filename=filename,
            file_path=file_path,
            file_size=file_size,
            mime_type=file.content_type,
            duration=metadata['duration'],
            width=metadata['width'],
            height=metadata['height'],
            fps=metadata['fps'],
            codec=metadata['codec'],
            status=VideoStatus.UPLOADED,
        )

        db.add(video)

        # Consume user quota
        current_user.consume_quota(1)

        await db.commit()
        await db.refresh(video)

        return video

    except ProcessingError as e:
        # Clean up file on error
        if os.path.exists(file_path):
            os.remove(file_path)
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(e)
        )


@router.get("/", response_model=List[VideoResponse])
async def list_videos(
    skip: int = 0,
    limit: int = 50,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    List all videos for current user.
    """
    result = await db.execute(
        select(Video)
        .where(Video.user_id == current_user.id)
        .order_by(desc(Video.created_at))
        .offset(skip)
        .limit(limit)
    )
    videos = result.scalars().all()

    return videos


@router.get("/{video_id}", response_model=VideoResponse)
async def get_video(
    video_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Get a specific video.
    """
    result = await db.execute(
        select(Video).where(
            Video.id == video_id,
            Video.user_id == current_user.id
        )
    )
    video = result.scalar_one_or_none()

    if not video:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Video not found"
        )

    return video


@router.patch("/{video_id}", response_model=VideoResponse)
async def update_video(
    video_id: str,
    video_update: VideoUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Update video metadata.
    """
    result = await db.execute(
        select(Video).where(
            Video.id == video_id,
            Video.user_id == current_user.id
        )
    )
    video = result.scalar_one_or_none()

    if not video:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Video not found"
        )

    # Update fields
    if video_update.title is not None:
        video.title = video_update.title
    if video_update.description is not None:
        video.description = video_update.description

    await db.commit()
    await db.refresh(video)

    return video


@router.delete("/{video_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_video(
    video_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Delete a video.
    """
    result = await db.execute(
        select(Video).where(
            Video.id == video_id,
            Video.user_id == current_user.id
        )
    )
    video = result.scalar_one_or_none()

    if not video:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Video not found"
        )

    # Delete file
    if os.path.exists(video.file_path):
        os.remove(video.file_path)

    # Delete from database (cascades to clips)
    await db.delete(video)
    await db.commit()


@router.post("/{video_id}/analyze", response_model=VideoAnalysisResponse)
async def analyze_video(
    video_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Analyze video with AI and extract clips.
    """
    result = await db.execute(
        select(Video).where(
            Video.id == video_id,
            Video.user_id == current_user.id
        )
    )
    video = result.scalar_one_or_none()

    if not video:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Video not found"
        )

    try:
        # Update status
        video.status = VideoStatus.ANALYZING
        await db.commit()

        # Analyze with MiniMax
        analysis_result = await minimax_service.analyze_video(
            video_path=video.file_path
        )

        # Extract clips
        clips_data = await minimax_service.extract_clips(
            video_path=video.file_path,
            analysis_result=analysis_result,
            sensitivity=settings.CLIP_SENSITIVITY_DEFAULT,
            min_duration=settings.MIN_CLIP_DURATION,
            max_duration=settings.MAX_CLIP_DURATION,
            max_clips=settings.MAX_CLIPS_PER_VIDEO
        )

        # Save clips to database
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

        return VideoAnalysisResponse(
            video_id=video.id,
            analysis_result=video.analysis_result,
            transcript=video.transcript,
            audio_analysis=video.audio_analysis,
            clips_extracted=len(clips_data),
            status=video.status.value
        )

    except Exception as e:
        video.status = VideoStatus.FAILED
        video.processing_error = str(e)
        await db.commit()

        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Analysis failed: {str(e)}"
        )
