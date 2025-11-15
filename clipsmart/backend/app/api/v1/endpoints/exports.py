"""
Export endpoints.
"""

from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc

from app.core.database import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.models.export import Export, ExportPlatform
from app.schemas.export import ExportCreate, ExportResponse
from app.services.export_service import ExportService

router = APIRouter()
export_service = ExportService()


@router.post("/", response_model=ExportResponse, status_code=status.HTTP_201_CREATED)
async def create_export(
    export_data: ExportCreate,
    background_tasks: BackgroundTasks,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Create an export for a splice.
    """
    # Create export (processing happens in service)
    export = await export_service.create_export(
        db=db,
        user_id=current_user.id,
        splice_id=export_data.splice_id,
        platform=ExportPlatform(export_data.platform),
        resolution=export_data.resolution,
        fps=export_data.fps,
        watermark=export_data.watermark,
        settings_dict=export_data.settings
    )

    return export


@router.get("/", response_model=List[ExportResponse])
async def list_exports(
    splice_id: Optional[str] = None,
    skip: int = 0,
    limit: int = 50,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    List all exports for current user.
    """
    query = select(Export).where(Export.user_id == current_user.id)

    if splice_id:
        query = query.where(Export.splice_id == splice_id)

    query = query.order_by(desc(Export.created_at)).offset(skip).limit(limit)

    result = await db.execute(query)
    exports = result.scalars().all()

    return exports


@router.get("/{export_id}", response_model=ExportResponse)
async def get_export(
    export_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Get a specific export.
    """
    result = await db.execute(
        select(Export).where(
            Export.id == export_id,
            Export.user_id == current_user.id
        )
    )
    export = result.scalar_one_or_none()

    if not export:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Export not found"
        )

    return export


@router.get("/{export_id}/download")
async def download_export(
    export_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Get download URL for an export.
    """
    download_url = await export_service.get_download_url(
        db=db,
        export_id=export_id,
        user_id=current_user.id
    )

    return {
        "download_url": download_url
    }


@router.delete("/{export_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_export(
    export_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Delete an export.
    """
    import os

    result = await db.execute(
        select(Export).where(
            Export.id == export_id,
            Export.user_id == current_user.id
        )
    )
    export = result.scalar_one_or_none()

    if not export:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Export not found"
        )

    # Delete file
    if export.file_path and os.path.exists(export.file_path):
        os.remove(export.file_path)

    await db.delete(export)
    await db.commit()
