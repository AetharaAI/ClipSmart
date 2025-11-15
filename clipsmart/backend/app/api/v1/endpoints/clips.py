"""
Clip endpoints.
"""

from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc

from app.core.database import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.models.clip import Clip
from app.models.video import Video
from app.schemas.clip import ClipResponse, ClipUpdate

router = APIRouter()


@router.get("/", response_model=List[ClipResponse])
async def list_clips(
    video_id: str = Query(None, description="Filter by video ID"),
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    List all clips for current user.
    """
    query = select(Clip).join(Video).where(Video.user_id == current_user.id)

    if video_id:
        query = query.where(Clip.video_id == video_id)

    query = query.order_by(desc(Clip.created_at)).offset(skip).limit(limit)

    result = await db.execute(query)
    clips = result.scalars().all()

    return clips


@router.get("/{clip_id}", response_model=ClipResponse)
async def get_clip(
    clip_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Get a specific clip.
    """
    result = await db.execute(
        select(Clip)
        .join(Video)
        .where(
            Clip.id == clip_id,
            Video.user_id == current_user.id
        )
    )
    clip = result.scalar_one_or_none()

    if not clip:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Clip not found"
        )

    return clip


@router.patch("/{clip_id}", response_model=ClipResponse)
async def update_clip(
    clip_id: str,
    clip_update: ClipUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Update clip metadata.
    """
    result = await db.execute(
        select(Clip)
        .join(Video)
        .where(
            Clip.id == clip_id,
            Video.user_id == current_user.id
        )
    )
    clip = result.scalar_one_or_none()

    if not clip:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Clip not found"
        )

    # Update fields
    if clip_update.title is not None:
        clip.title = clip_update.title
    if clip_update.description is not None:
        clip.description = clip_update.description

    await db.commit()
    await db.refresh(clip)

    return clip


@router.delete("/{clip_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_clip(
    clip_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Delete a clip.
    """
    result = await db.execute(
        select(Clip)
        .join(Video)
        .where(
            Clip.id == clip_id,
            Video.user_id == current_user.id
        )
    )
    clip = result.scalar_one_or_none()

    if not clip:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Clip not found"
        )

    await db.delete(clip)
    await db.commit()
