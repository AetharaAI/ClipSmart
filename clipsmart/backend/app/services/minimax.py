"""
MiniMax-M2 AI integration service.
"""

import httpx
import logging
from typing import Dict, Any, List, Optional
from tenacity import retry, stop_after_attempt, wait_exponential

from app.core.config import get_settings
from app.core.exceptions import ExternalAPIError

settings = get_settings()
logger = logging.getLogger("clipsmart.minimax")


class MinimaxService:
    """Service for interacting with MiniMax-M2 API."""

    def __init__(self):
        self.api_key = settings.MINIMAX_API_KEY
        self.base_url = settings.MINIMAX_API_BASE_URL
        self.timeout = settings.MINIMAX_ANALYSIS_TIMEOUT

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10)
    )
    async def analyze_video(
        self,
        video_path: str,
        transcript: Optional[str] = None,
        audio_features: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Analyze video content using MiniMax-M2.

        Args:
            video_path: Path to the video file
            transcript: Optional video transcript
            audio_features: Optional audio analysis features

        Returns:
            Analysis results including attention scores, topics, entities
        """
        logger.info(f"Analyzing video: {video_path}")

        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                # Prepare request payload
                payload = {
                    "model": "minimax-m2",
                    "task": "video_analysis",
                    "video_path": video_path,
                    "include_attention_scores": True,
                    "include_topics": True,
                    "include_entities": True,
                    "include_sentiment": True,
                }

                if transcript:
                    payload["transcript"] = transcript

                if audio_features:
                    payload["audio_features"] = audio_features

                response = await client.post(
                    f"{self.base_url}/analyze",
                    json=payload,
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json",
                    }
                )

                response.raise_for_status()
                result = response.json()

                logger.info(f"Video analysis completed successfully")
                return result

        except httpx.HTTPError as e:
            logger.error(f"MiniMax API error: {str(e)}")
            raise ExternalAPIError(f"Failed to analyze video: {str(e)}")

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10)
    )
    async def extract_clips(
        self,
        video_path: str,
        analysis_result: Dict[str, Any],
        sensitivity: float = 0.75,
        min_duration: float = 3.0,
        max_duration: float = 30.0,
        max_clips: int = 50
    ) -> List[Dict[str, Any]]:
        """
        Extract clips from video based on AI analysis.

        Args:
            video_path: Path to the video file
            analysis_result: Previous analysis result
            sensitivity: Clip extraction sensitivity (0-1)
            min_duration: Minimum clip duration in seconds
            max_duration: Maximum clip duration in seconds
            max_clips: Maximum number of clips to extract

        Returns:
            List of clip candidates with timing and scores
        """
        logger.info(f"Extracting clips from video: {video_path}")

        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                payload = {
                    "model": "minimax-m2",
                    "task": "clip_extraction",
                    "video_path": video_path,
                    "analysis_result": analysis_result,
                    "sensitivity": sensitivity,
                    "min_duration": min_duration,
                    "max_duration": max_duration,
                    "max_clips": max_clips,
                }

                response = await client.post(
                    f"{self.base_url}/extract_clips",
                    json=payload,
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json",
                    }
                )

                response.raise_for_status()
                result = response.json()

                clips = result.get("clips", [])
                logger.info(f"Extracted {len(clips)} clips")

                return clips

        except httpx.HTTPError as e:
            logger.error(f"MiniMax API error: {str(e)}")
            raise ExternalAPIError(f"Failed to extract clips: {str(e)}")

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10)
    )
    async def generate_splice_recommendations(
        self,
        clips: List[Dict[str, Any]],
        mode: str,
        target_duration: int,
        num_clips: int
    ) -> Dict[str, Any]:
        """
        Generate splice recommendations using AI.

        Args:
            clips: List of available clips with metadata
            mode: Generation mode (semantic, eclectic, trending)
            target_duration: Target splice duration in seconds
            num_clips: Number of clips to include

        Returns:
            Recommendations including clip selection and rationale
        """
        logger.info(f"Generating {mode} splice recommendations")

        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                payload = {
                    "model": "minimax-m2",
                    "task": "splice_generation",
                    "clips": clips,
                    "mode": mode,
                    "target_duration": target_duration,
                    "num_clips": num_clips,
                }

                response = await client.post(
                    f"{self.base_url}/generate_splice",
                    json=payload,
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json",
                    }
                )

                response.raise_for_status()
                result = response.json()

                logger.info(f"Generated splice recommendations: {len(result.get('selected_clips', []))} clips")
                return result

        except httpx.HTTPError as e:
            logger.error(f"MiniMax API error: {str(e)}")
            raise ExternalAPIError(f"Failed to generate splice: {str(e)}")

    async def generate_caption(
        self,
        clip_metadata: Dict[str, Any],
        platform: str = "tiktok"
    ) -> str:
        """
        Generate a caption for a clip or splice.

        Args:
            clip_metadata: Metadata about the clip/splice
            platform: Target platform (tiktok, youtube_shorts, instagram_reels)

        Returns:
            Generated caption text
        """
        logger.info(f"Generating caption for {platform}")

        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                payload = {
                    "model": "minimax-m2",
                    "task": "caption_generation",
                    "metadata": clip_metadata,
                    "platform": platform,
                }

                response = await client.post(
                    f"{self.base_url}/generate_caption",
                    json=payload,
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json",
                    }
                )

                response.raise_for_status()
                result = response.json()

                caption = result.get("caption", "")
                logger.info(f"Generated caption: {caption[:50]}...")

                return caption

        except httpx.HTTPError as e:
            logger.error(f"MiniMax API error: {str(e)}")
            # Return empty string on error rather than failing
            return ""

    async def generate_hashtags(
        self,
        content_metadata: Dict[str, Any],
        platform: str = "tiktok",
        max_hashtags: int = 10
    ) -> List[str]:
        """
        Generate hashtags for content.

        Args:
            content_metadata: Metadata about the content
            platform: Target platform
            max_hashtags: Maximum number of hashtags to generate

        Returns:
            List of suggested hashtags
        """
        logger.info(f"Generating hashtags for {platform}")

        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                payload = {
                    "model": "minimax-m2",
                    "task": "hashtag_generation",
                    "metadata": content_metadata,
                    "platform": platform,
                    "max_hashtags": max_hashtags,
                }

                response = await client.post(
                    f"{self.base_url}/generate_hashtags",
                    json=payload,
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json",
                    }
                )

                response.raise_for_status()
                result = response.json()

                hashtags = result.get("hashtags", [])
                logger.info(f"Generated {len(hashtags)} hashtags")

                return hashtags

        except httpx.HTTPError as e:
            logger.error(f"MiniMax API error: {str(e)}")
            # Return empty list on error
            return []
