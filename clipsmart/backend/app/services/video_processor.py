"""
Video processing service using FFmpeg and OpenCV.
"""

import os
import logging
import subprocess
import json
from typing import Dict, Any, List, Optional, Tuple
from pathlib import Path
import cv2
import ffmpeg

from app.core.config import get_settings
from app.core.exceptions import ProcessingError

settings = get_settings()
logger = logging.getLogger("clipsmart.video_processor")


class VideoProcessorService:
    """Service for video processing operations."""

    def __init__(self):
        self.ffmpeg_path = settings.FFMPPEG_PATH
        self.upload_dir = Path(settings.UPLOAD_DIR)
        self.export_dir = Path(settings.EXPORT_DIR)

        # Ensure directories exist
        self.upload_dir.mkdir(parents=True, exist_ok=True)
        self.export_dir.mkdir(parents=True, exist_ok=True)

    async def get_video_metadata(self, video_path: str) -> Dict[str, Any]:
        """
        Extract video metadata using FFprobe.

        Args:
            video_path: Path to video file

        Returns:
            Dictionary with video metadata
        """
        logger.info(f"Extracting metadata from: {video_path}")

        try:
            probe = ffmpeg.probe(video_path)

            # Get video stream
            video_stream = next(
                (stream for stream in probe['streams'] if stream['codec_type'] == 'video'),
                None
            )

            if not video_stream:
                raise ProcessingError("No video stream found in file")

            # Get audio stream
            audio_stream = next(
                (stream for stream in probe['streams'] if stream['codec_type'] == 'audio'),
                None
            )

            metadata = {
                'duration': float(probe['format']['duration']),
                'size': int(probe['format']['size']),
                'bitrate': int(probe['format'].get('bit_rate', 0)),
                'width': int(video_stream['width']),
                'height': int(video_stream['height']),
                'fps': eval(video_stream['r_frame_rate']),
                'codec': video_stream['codec_name'],
                'has_audio': audio_stream is not None,
            }

            logger.info(f"Metadata extracted: {metadata}")
            return metadata

        except ffmpeg.Error as e:
            logger.error(f"FFprobe error: {e.stderr.decode() if e.stderr else str(e)}")
            raise ProcessingError(f"Failed to extract video metadata: {str(e)}")

    async def extract_clip(
        self,
        input_path: str,
        output_path: str,
        start_time: float,
        end_time: float,
        include_audio: bool = True
    ) -> str:
        """
        Extract a clip from a video.

        Args:
            input_path: Path to input video
            output_path: Path for output clip
            start_time: Start time in seconds
            end_time: End time in seconds
            include_audio: Whether to include audio

        Returns:
            Path to extracted clip
        """
        logger.info(f"Extracting clip: {start_time}s - {end_time}s")

        try:
            duration = end_time - start_time

            # Build FFmpeg command
            stream = ffmpeg.input(input_path, ss=start_time, t=duration)

            if include_audio:
                stream = ffmpeg.output(
                    stream,
                    output_path,
                    vcodec='libx264',
                    acodec='aac',
                    preset='fast',
                    crf=23
                )
            else:
                stream = ffmpeg.output(
                    stream,
                    output_path,
                    vcodec='libx264',
                    preset='fast',
                    crf=23,
                    an=None  # No audio
                )

            # Run FFmpeg
            ffmpeg.run(stream, overwrite_output=True, quiet=True)

            logger.info(f"Clip extracted successfully: {output_path}")
            return output_path

        except ffmpeg.Error as e:
            logger.error(f"FFmpeg error: {e.stderr.decode() if e.stderr else str(e)}")
            raise ProcessingError(f"Failed to extract clip: {str(e)}")

    async def generate_thumbnail(
        self,
        video_path: str,
        output_path: str,
        timestamp: Optional[float] = None
    ) -> str:
        """
        Generate a thumbnail from video.

        Args:
            video_path: Path to video file
            output_path: Path for output thumbnail
            timestamp: Timestamp in seconds (default: middle of video)

        Returns:
            Path to generated thumbnail
        """
        logger.info(f"Generating thumbnail for: {video_path}")

        try:
            # If no timestamp specified, use middle of video
            if timestamp is None:
                metadata = await self.get_video_metadata(video_path)
                timestamp = metadata['duration'] / 2

            # Extract frame
            stream = ffmpeg.input(video_path, ss=timestamp)
            stream = ffmpeg.output(
                stream,
                output_path,
                vframes=1,
                format='image2',
                vcodec='mjpeg'
            )

            ffmpeg.run(stream, overwrite_output=True, quiet=True)

            logger.info(f"Thumbnail generated: {output_path}")
            return output_path

        except ffmpeg.Error as e:
            logger.error(f"FFmpeg error: {e.stderr.decode() if e.stderr else str(e)}")
            raise ProcessingError(f"Failed to generate thumbnail: {str(e)}")

    async def create_split_screen(
        self,
        clip_paths: List[str],
        output_path: str,
        layout: str = "split_screen",
        resolution: str = "1080x1920",
        fps: int = 30
    ) -> str:
        """
        Create a split-screen video from multiple clips.

        Args:
            clip_paths: List of paths to clip files
            output_path: Path for output video
            layout: Layout type (split_screen, grid, etc.)
            resolution: Output resolution (WxH)
            fps: Output frame rate

        Returns:
            Path to generated split-screen video
        """
        logger.info(f"Creating split-screen video with {len(clip_paths)} clips")

        try:
            width, height = map(int, resolution.split('x'))

            if layout == "split_screen" and len(clip_paths) == 2:
                # Vertical split screen (top/bottom)
                input1 = ffmpeg.input(clip_paths[0])
                input2 = ffmpeg.input(clip_paths[1])

                # Scale both clips to half height
                v1 = input1.video.filter('scale', width, height // 2)
                v2 = input2.video.filter('scale', width, height // 2)

                # Stack vertically
                joined = ffmpeg.filter([v1, v2], 'vstack')

                # Mix audio
                a1 = input1.audio
                a2 = input2.audio
                audio = ffmpeg.filter([a1, a2], 'amix', inputs=2)

                # Output
                output = ffmpeg.output(
                    joined,
                    audio,
                    output_path,
                    vcodec='libx264',
                    acodec='aac',
                    preset='medium',
                    crf=23,
                    r=fps
                )

                ffmpeg.run(output, overwrite_output=True, quiet=True)

            elif layout == "grid":
                # Grid layout for multiple clips
                # This is simplified - in production, you'd calculate grid dimensions
                inputs = [ffmpeg.input(path) for path in clip_paths[:4]]

                # Scale all to quarter size
                scaled = [
                    inp.video.filter('scale', width // 2, height // 2)
                    for inp in inputs
                ]

                # Create 2x2 grid
                if len(scaled) >= 2:
                    top = ffmpeg.filter([scaled[0], scaled[1]], 'hstack')
                if len(scaled) >= 4:
                    bottom = ffmpeg.filter([scaled[2], scaled[3]], 'hstack')
                    joined = ffmpeg.filter([top, bottom], 'vstack')
                else:
                    joined = top

                # Mix audio from all clips
                audios = [inp.audio for inp in inputs]
                audio = ffmpeg.filter(audios, 'amix', inputs=len(audios))

                # Output
                output = ffmpeg.output(
                    joined,
                    audio,
                    output_path,
                    vcodec='libx264',
                    acodec='aac',
                    preset='medium',
                    crf=23,
                    r=fps
                )

                ffmpeg.run(output, overwrite_output=True, quiet=True)

            else:
                raise ProcessingError(f"Unsupported layout: {layout}")

            logger.info(f"Split-screen video created: {output_path}")
            return output_path

        except ffmpeg.Error as e:
            logger.error(f"FFmpeg error: {e.stderr.decode() if e.stderr else str(e)}")
            raise ProcessingError(f"Failed to create split-screen: {str(e)}")

    async def optimize_for_platform(
        self,
        input_path: str,
        output_path: str,
        platform: str,
        resolution: str = "1080x1920",
        fps: int = 30,
        watermark: Optional[str] = None
    ) -> str:
        """
        Optimize video for specific platform.

        Args:
            input_path: Path to input video
            output_path: Path for output video
            platform: Target platform (tiktok, youtube_shorts, instagram_reels)
            resolution: Output resolution
            fps: Output frame rate
            watermark: Optional watermark text

        Returns:
            Path to optimized video
        """
        logger.info(f"Optimizing video for {platform}")

        try:
            width, height = map(int, resolution.split('x'))

            stream = ffmpeg.input(input_path)

            # Scale to target resolution
            video = stream.video.filter('scale', width, height)

            # Add watermark if specified
            if watermark:
                video = video.drawtext(
                    text=watermark,
                    x='(w-text_w)/2',
                    y='h-th-10',
                    fontsize=24,
                    fontcolor='white',
                    shadowcolor='black',
                    shadowx=2,
                    shadowy=2
                )

            # Platform-specific optimizations
            if platform == "tiktok":
                # TikTok prefers H.264, AAC, specific bitrate
                output = ffmpeg.output(
                    video,
                    stream.audio,
                    output_path,
                    vcodec='libx264',
                    acodec='aac',
                    preset='medium',
                    crf=23,
                    r=fps,
                    **{'b:v': '2M', 'b:a': '128k'}
                )

            elif platform == "youtube_shorts":
                # YouTube Shorts optimization
                output = ffmpeg.output(
                    video,
                    stream.audio,
                    output_path,
                    vcodec='libx264',
                    acodec='aac',
                    preset='medium',
                    crf=22,
                    r=fps,
                    **{'b:v': '3M', 'b:a': '192k'}
                )

            elif platform == "instagram_reels":
                # Instagram Reels optimization
                output = ffmpeg.output(
                    video,
                    stream.audio,
                    output_path,
                    vcodec='libx264',
                    acodec='aac',
                    preset='medium',
                    crf=23,
                    r=fps,
                    **{'b:v': '2.5M', 'b:a': '128k'}
                )

            else:
                # Generic optimization
                output = ffmpeg.output(
                    video,
                    stream.audio,
                    output_path,
                    vcodec='libx264',
                    acodec='aac',
                    preset='medium',
                    crf=23,
                    r=fps
                )

            ffmpeg.run(output, overwrite_output=True, quiet=True)

            logger.info(f"Video optimized for {platform}: {output_path}")
            return output_path

        except ffmpeg.Error as e:
            logger.error(f"FFmpeg error: {e.stderr.decode() if e.stderr else str(e)}")
            raise ProcessingError(f"Failed to optimize video: {str(e)}")

    async def extract_audio(self, video_path: str, output_path: str) -> str:
        """
        Extract audio from video.

        Args:
            video_path: Path to video file
            output_path: Path for output audio file

        Returns:
            Path to extracted audio
        """
        logger.info(f"Extracting audio from: {video_path}")

        try:
            stream = ffmpeg.input(video_path)
            audio = stream.audio
            output = ffmpeg.output(audio, output_path, acodec='libmp3lame', ar=44100)

            ffmpeg.run(output, overwrite_output=True, quiet=True)

            logger.info(f"Audio extracted: {output_path}")
            return output_path

        except ffmpeg.Error as e:
            logger.error(f"FFmpeg error: {e.stderr.decode() if e.stderr else str(e)}")
            raise ProcessingError(f"Failed to extract audio: {str(e)}")
