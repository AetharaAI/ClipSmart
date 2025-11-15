"""
Splice endpoints.
"""

from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc

from app.core.database import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.models.splice import Splice, SpliceMode
from app.schemas.splice import SpliceCreate, SpliceResponse, SpliceUpdate, SpliceGenerateRequest
from app.services.splice_generator import SpliceGeneratorService

router = APIRouter()
splice_service = SpliceGeneratorService()


@router.post("/generate", response_model=SpliceResponse, status_code=status.HTTP_201_CREATED)
async def generate_splice(
    request: SpliceGenerateRequest,
    background_tasks: BackgroundTasks,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Generate a splice using AI clip selection.
    """
    # Create splice
    splice = await splice_service.generate_splice(
        db=db,
        user_id=current_user.id,
        video_ids=request.video_ids,
        mode=SpliceMode(request.mode),
        target_duration=request.target_duration,
        num_clips=request.num_clips,
        layout=request.layout
    )

    # Render splice in background
    background_tasks.add_task(
        splice_service.render_splice,
        db=db,
        splice_id=splice.id
    )

    return splice


@router.post("/", response_model=SpliceResponse, status_code=status.HTTP_201_CREATED)
async def create_splice(
    splice_data: SpliceCreate,
    background_tasks: BackgroundTasks,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Create a splice with manually selected clips.
    """
    from app.models.splice import splice_clips as splice_clips_table
    from app.models.clip import Clip
    from app.models.video import Video

    # Verify clips belong to user
    result = await db.execute(
        select(Clip)
        .join(Video)
        .where(
            Clip.id.in_(splice_data.clip_ids),
            Video.user_id == current_user.id
        )
    )
    clips = result.scalars().all()

    if len(clips) != len(splice_data.clip_ids):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Some clips not found or don't belong to you"
        )

    # Create splice
    splice = Splice(
        user_id=current_user.id,
        title=splice_data.title,
        description=splice_data.description,
        mode=SpliceMode(splice_data.mode),
        target_duration=splice_data.target_duration,
        num_clips=len(splice_data.clip_ids),
        layout=splice_data.layout,
    )

    db.add(splice)
    await db.flush()

    # Associate clips
    for position, clip_id in enumerate(splice_data.clip_ids):
        stmt = splice_clips_table.insert().values(
            splice_id=splice.id,
            clip_id=clip_id,
            position=position
        )
        await db.execute(stmt)

    await db.commit()
    await db.refresh(splice)

    # Render splice in background
    background_tasks.add_task(
        splice_service.render_splice,
        db=db,
        splice_id=splice.id
    )

    return splice


@router.get("/", response_model=List[SpliceResponse])
async def list_splices(
    skip: int = 0,
    limit: int = 50,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    List all splices for current user.
    """
    result = await db.execute(
        select(Splice)
        .where(Splice.user_id == current_user.id)
        .order_by(desc(Splice.created_at))
        .offset(skip)
        .limit(limit)
    )
    splices = result.scalars().all()

    return splices


@router.get("/{splice_id}", response_model=SpliceResponse)
async def get_splice(
    splice_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Get a specific splice.
    """
    result = await db.execute(
        select(Splice).where(
            Splice.id == splice_id,
            Splice.user_id == current_user.id
        )
    )
    splice = result.scalar_one_or_none()

    if not splice:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Splice not found"
        )

    return splice


@router.patch("/{splice_id}", response_model=SpliceResponse)
async def update_splice(
    splice_id: str,
    splice_update: SpliceUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Update splice metadata.
    """
    result = await db.execute(
        select(Splice).where(
            Splice.id == splice_id,
            Splice.user_id == current_user.id
        )
    )
    splice = result.scalar_one_or_none()

    if not splice:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Splice not found"
        )

    # Update fields
    if splice_update.title is not None:
        splice.title = splice_update.title
    if splice_update.description is not None:
        splice.description = splice_update.description

    await db.commit()
    await db.refresh(splice)

    return splice


@router.delete("/{splice_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_splice(
    splice_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Delete a splice.
    """
    import os

    result = await db.execute(
        select(Splice).where(
            Splice.id == splice_id,
            Splice.user_id == current_user.id
        )
    )
    splice = result.scalar_one_or_none()

    if not splice:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Splice not found"
        )

    # Delete file
    if splice.file_path and os.path.exists(splice.file_path):
        os.remove(splice.file_path)

    await db.delete(splice)
    await db.commit()


@router.post("/{splice_id}/render", response_model=SpliceResponse)
async def render_splice(
    splice_id: str,
    background_tasks: BackgroundTasks,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Manually trigger splice rendering.
    """
    result = await db.execute(
        select(Splice).where(
            Splice.id == splice_id,
            Splice.user_id == current_user.id
        )
    )
    splice = result.scalar_one_or_none()

    if not splice:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Splice not found"
        )

    # Render in background
    background_tasks.add_task(
        splice_service.render_splice,
        db=db,
        splice_id=splice_id
    )

    return splice
