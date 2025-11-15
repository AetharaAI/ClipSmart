"""
Main API router that combines all endpoint routers.
"""

from fastapi import APIRouter

from app.api.v1.endpoints import auth, videos, clips, splices, exports

api_router = APIRouter()

# Include all endpoint routers
api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(videos.router, prefix="/videos", tags=["Videos"])
api_router.include_router(clips.router, prefix="/clips", tags=["Clips"])
api_router.include_router(splices.router, prefix="/splices", tags=["Splices"])
api_router.include_router(exports.router, prefix="/exports", tags=["Exports"])
