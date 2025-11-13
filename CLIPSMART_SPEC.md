# ClipSmart - Enterprise Content Creation Platform Specification
**Version:** 2.0  
**Company:** AetherPro Technologies LLC  
**Date:** 2025-11-06  

## Executive Summary

ClipSmart is a production-grade web application that transforms long-form videos into viral-ready split-screen shorts using advanced AI analysis. The platform integrates MiniMax-M2 multimodal AI to extract attention-grabbing clips and automatically generates engaging split-screen compositions optimized for TikTok, YouTube Shorts, and other social media platforms. Built for enterprise scalability within the Aether ecosystem.

## User Personas

### 1. Content Creators (Primary)
- **Profile:** YouTube creators, TikTok influencers, social media managers
- **Pain Points:** Time-consuming video editing, difficulty creating viral content
- **Needs:** Quick clip extraction, auto-generated hooks, viral optimization
- **Success Metrics:** Time saved per video, engagement rates, viral potential score

### 2. Marketing Professionals
- **Profile:** Brand marketers, agencies, content strategists
- **Pain Points:** Creating engaging ad content, optimizing for different platforms
- **Needs:** Brand-consistent templates, multi-platform optimization, batch processing
- **Success Metrics:** Campaign ROI, content performance across platforms, production efficiency

### 3. Casual Users
- **Profile:** Social media users, small business owners, personal creators
- **Pain Points:** Limited editing skills, time constraints, content ideas
- **Needs:** Simple interface, automated suggestions, quick results
- **Success Metrics:** Ease of use, content quality improvement, learning curve

## Wireframes & UI Flow

### Landing Page
```
┌─────────────────────────────────────────────────────────┐
│  AETHERPRO LOGO    ClipSmart           [Login/Register] │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Transform Long Videos Into Viral Shorts                │
│                                                         │
│  [Drag & Drop Video Here]  or  [Paste YouTube URL]     │
│                                                         │
│  ⭐ AI-Powered Clip Extraction                         │
│  ✨ 3 Smart Splice Modes                               │
│  🚀 Export Ready for Social Media                      │
│                                                         │
│         [Try Free Demo]  [Watch Video]                 │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Upload Interface
```
┌─────────────────────────────────────────────────────────┐
│ ← Back  Upload Video                                    │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌─────────────────────────────────┐                   │
│  │     DRAG & DROP ZONE            │                   │
│  │                                 │                   │
│  │    📹 MP4, MOV, AVI, WebM       │                   │
│  │                                 │                   │
│  │       Drop files here           │                   │
│  │      or click to browse         │                   │
│  │                                 │                   │
│  └─────────────────────────────────┘                   │
│                                                         │
│  📌 Or paste YouTube URL: [________________] [Add]     │
│                                                         │
│  📌 Or browse trending:  [Search trending videos]      │
│                                                         │
│  Upload Progress: ████████░░░░░░░░░░░░ 67% (45MB/67MB) │
│  Estimated time: 2 minutes remaining                   │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Analysis & Clip Selection
```
┌─────────────────────────────────────────────────────────┐
│ ← Back  Analyzing Video...  🧠 AI Processing           │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Scene Detection: ████████████████░░░░ 85%             │
│  Attention Scoring: ████████████░░░░░░ 65%             │
│  Audio Analysis: ████████████████████ 100%             │
│                                                         │
│  🎬 Top 12 Clips Found (Score > 75%)                   │
│                                                         │
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐       │
│  │☑️🎯  │ │☑️💯  │ │✅  │ │☑️🎪  │ │✅  │ │☑️🔥  │       │
│  │0.94 │ │0.92 │ │0.89 │ │0.87 │ │0.86 │ │0.85 │       │
│  │ 3.2s│ │ 5.1s│ │ 7.8s│ │12.3s│ │15.7s│ │18.9s│       │
│  └─────┘ └─────┘ └─────┘ └─────┘ └─────┘ └─────┘       │
│                                                         │
│  Sensitivity: [====================●] Advanced          │
│  [▶️ Preview All] [🔄 Re-analyze] [Next: Create Splices]│
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Splice Editor
```
┌─────────────────────────────────────────────────────────┐
│ ← Back  Create Splice  [Save Draft] [Export]            │
├─────────────────────────────────────────────────────────┤
│  Mode: [Semantic] [Eclectic] [Trending]                 │
│                                                         │
│  ┌───────────────┬───────────────┐                     │
│  │   TOP CLIP    │  BOTTOM CLIP   │                     │
│  │               │                │                     │
│  │   🎬 Video    │   🎬 Video     │                     │
│  │  Preview      │  Preview       │                     │
│  │               │                │                     │
│  │ Similarity:   │ Contrast:      │                     │
│  │ 0.74 ⭐⭐⭐⭐   │ High 🎪🎪🎪     │                     │
│  └───────────────┴───────────────┘                     │
│                                                         │
│  Audio Mix:  🔊 Top: [====●] 70% 🔊 Bottom: [===●] 50% │
│                                                         │
│  Text Overlay: "Wait for this hack..." [+ Add Text]    │
│                                                         │
│  Split Ratio: [========●====] 60% Top / 40% Bottom     │
│  Preview: [▶️ Play Splice]                             │
│                                                         │
│  [Swap Clips] [Change Mode] [Add Effect] [Export]      │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Export Interface
```
┌─────────────────────────────────────────────────────────┐
│ ← Back  Export Ready! 🎉                               │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌─────────────────┐  ┌─────────────────┐             │
│  │   PREVIEW       │  │   DOWNLOAD      │             │
│  │                 │  │                 │             │
│  │  🎬 Final Video │  │  📥 MP4 File    │             │
│  │  9:16 Portrait  │  │  720x1280       │             │
│  │  30s Duration   │  │  H.264 + AAC    │             │
│  │                 │  │  45 MB          │             │
│  │  [▶️ Preview]    │  │  [📥 Download]  │             │
│  └─────────────────┘  └─────────────────┘             │
│                                                         │
│  📝 Auto-Generated Description:                        │
│  "🔥 Mind-blowing tech hack that will change your      │
│   life! Wait for the surprise ending... #TechHacks    │
│   #Viral #Innovation"                                   │
│                                                         │
│  🏷️ Hashtags: #TechHacks #Innovation #Viral #LifeHack  │
│              #Productivity #Gadgets #DIY #TechTok       │
│                                                         │
│  [📤 Save to Library] [🔗 Share Link] [📱 Direct Upload]│
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## API Endpoint Specifications

### Authentication & User Management
```typescript
POST /api/auth/login
Body: { email: string, password: string }
Response: { user: User, token: string }

POST /api/auth/register
Body: { email: string, password: string, name: string }
Response: { user: User, token: string }

GET /api/user/profile
Headers: Authorization: Bearer <token>
Response: UserProfile

PUT /api/user/profile
Headers: Authorization: Bearer <token>
Body: Partial<UserProfile>
Response: UserProfile
```

### Video Upload & Management
```typescript
POST /api/upload
Body: multipart/form-data (video file)
Headers: Authorization: Bearer <token>
Response: { upload_id: string, file_size: number, estimated_processing_time: number }

POST /api/upload/youtube
Body: { url: string }
Headers: Authorization: Bearer <token>
Response: { video_id: string, title: string, duration: number }

GET /api/library/videos
Headers: Authorization: Bearer <token>
Query: { page?: number, limit?: number, sort?: string }
Response: { videos: Video[], total: number, has_more: boolean }

GET /api/videos/{video_id}
Headers: Authorization: Bearer <token>
Response: VideoDetail

DELETE /api/videos/{video_id}
Headers: Authorization: Bearer <token>
Response: { success: boolean, message: string }
```

### AI Analysis & Clip Extraction
```typescript
POST /api/analyze
Body: { video_id: string, sensitivity?: number }
Headers: Authorization: Bearer <token>
Response: { analysis_id: string, status: "processing", estimated_completion: string }

GET /api/analyze/{analysis_id}
Headers: Authorization: Bearer <token>
Response: { status: "processing" | "completed" | "failed", clips: Clip[], progress: number }

POST /api/clips/batch-update
Body: { clip_ids: string[], selected: boolean[] }
Headers: Authorization: Bearer <token>
Response: { success: boolean }
```

### Splice Generation & Editing
```typescript
POST /api/splice/generate
Body: {
  clip_ids: [string, string],
  mode: "semantic" | "eclectic" | "trending",
  options: {
    split_ratio?: number,
    audio_mix?: { top_volume: number, bottom_volume: number },
    text_overlays?: TextOverlay[]
  }
}
Headers: Authorization: Bearer <token>
Response: { splice_id: string, preview_url: string }

GET /api/splice/{splice_id}
Headers: Authorization: Bearer <token>
Response: SpliceDetail

PUT /api/splice/{splice_id}
Body: Partial<SpliceDetail>
Headers: Authorization: Bearer <token>
Response: SpliceDetail

POST /api/splice/preview
Body: { splice_id: string, timestamp?: number }
Headers: Authorization: Bearer <token>
Response: { preview_url: string, current_frame: number }
```

### Export & Download
```typescript
POST /api/export
Body: {
  splice_id: string,
  format: {
    resolution: "720x1280" | "1080x1920",
    fps: 30,
    codec: "h264",
    bitrate: number
  },
  metadata: {
    title?: string,
    description?: string,
    hashtags?: string[]
  }
}
Headers: Authorization: Bearer <token>
Response: { export_id: string, status: "processing" }

GET /api/export/{export_id}
Headers: Authorization: Bearer <token>
Response: { status: "processing" | "completed" | "failed", download_url?: string }

GET /api/export/{export_id}/download
Headers: Authorization: Bearer <token>
Response: File download stream
```

### Trending & Discovery
```typescript
GET /api/trending/videos
Query: { topic?: string, limit?: number, timeframe?: string }
Headers: Authorization: Bearer <token>
Response: { videos: TrendingVideo[], metadata: { topic: string, generated_at: string } }

GET /api/trending/hashtags
Query: { limit?: number }
Headers: Authorization: Bearer <token>
Response: { hashtags: TrendingHashtag[] }
```

### Analytics & Insights
```typescript
GET /api/analytics/dashboard
Headers: Authorization: Bearer <token>
Response: {
  videos_processed: number,
  clips_extracted: number,
  splices_created: number,
  exports_completed: number,
  total_processing_time: number
}

GET /api/analytics/performance
Query: { timeframe: "7d" | "30d" | "90d" }
Headers: Authorization: Bearer <token>
Response: {
  average_clip_score: number,
  popular_modes: { semantic: number, eclectic: number, trending: number },
  export_formats: { resolution: string, count: number }[]
}
```

## Database Schema

### PostgreSQL Tables

```sql
-- Users table (extends Supabase auth.users)
CREATE TABLE public.users (
    id UUID REFERENCES auth.users(id) PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    full_name TEXT,
    avatar_url TEXT,
    subscription_tier TEXT DEFAULT 'free',
    processing_quota INTEGER DEFAULT 10,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Videos table
CREATE TABLE public.videos (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES public.users(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    original_filename TEXT,
    file_size BIGINT,
    duration_seconds INTEGER,
    resolution_width INTEGER,
    resolution_height INTEGER,
    format TEXT,
    storage_path TEXT NOT NULL,
    thumbnail_path TEXT,
    upload_source TEXT NOT NULL, -- 'upload', 'youtube', 'trending'
    youtube_url TEXT,
    processing_status TEXT DEFAULT 'pending', -- pending, processing, completed, failed
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Clips table (AI-extracted video segments)
CREATE TABLE public.clips (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    video_id UUID REFERENCES public.videos(id) ON DELETE CASCADE,
    start_time_seconds DECIMAL(10,3) NOT NULL,
    end_time_seconds DECIMAL(10,3) NOT NULL,
    duration_seconds DECIMAL(10,3) NOT NULL,
    attention_score DECIMAL(5,4), -- 0.0 to 1.0
    visual_intensity DECIMAL(5,4),
    audio_intensity DECIMAL(5,4),
    motion_score DECIMAL(5,4),
    semantic_hooks JSONB, -- Array of detected hooks
    emotion_detected TEXT,
    embedding VECTOR(1536), -- MiniMax-M2 embedding
    thumbnail_path TEXT,
    storage_path TEXT,
    selected BOOLEAN DEFAULT false,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Splices table (split-screen combinations)
CREATE TABLE public.splices (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES public.users(id) ON DELETE CASCADE,
    top_clip_id UUID REFERENCES public.clips(id) ON DELETE CASCADE,
    bottom_clip_id UUID REFERENCES public.clips(id) ON DELETE CASCADE,
    mode TEXT NOT NULL, -- 'semantic', 'eclectic', 'trending'
    similarity_score DECIMAL(5,4),
    contrast_score DECIMAL(5,4),
    split_ratio DECIMAL(3,2) DEFAULT 0.5, -- 0.0 to 1.0
    audio_mix JSONB, -- { top_volume: 0.7, bottom_volume: 0.5 }
    text_overlays JSONB, -- Array of text overlay objects
    preview_path TEXT,
    status TEXT DEFAULT 'draft', -- draft, processing, completed, failed
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Exports table (final rendered videos)
CREATE TABLE public.exports (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES public.users(id) ON DELETE CASCADE,
    splice_id UUID REFERENCES public.splices(id) ON DELETE CASCADE,
    filename TEXT NOT NULL,
    file_size BIGINT,
    resolution TEXT NOT NULL, -- '720x1280', '1080x1920'
    fps INTEGER DEFAULT 30,
    codec TEXT DEFAULT 'h264',
    bitrate INTEGER,
    duration_seconds INTEGER,
    storage_path TEXT NOT NULL,
    download_url TEXT,
    metadata JSONB, -- title, description, hashtags
    processing_status TEXT DEFAULT 'pending',
    error_message TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    completed_at TIMESTAMP WITH TIME ZONE
);

-- Processing jobs table (Celery task tracking)
CREATE TABLE public.processing_jobs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES public.users(id) ON DELETE CASCADE,
    video_id UUID REFERENCES public.videos(id) ON DELETE CASCADE,
    task_type TEXT NOT NULL, -- 'analysis', 'splice_generation', 'export'
    task_id TEXT NOT NULL, -- Celery task ID
    status TEXT DEFAULT 'pending', -- pending, running, completed, failed
    progress INTEGER DEFAULT 0,
    result JSONB,
    error_message TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Vector similarity index for clips
CREATE INDEX clips_embedding_idx ON public.clips 
USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);

-- Performance indexes
CREATE INDEX idx_videos_user_id ON public.videos(user_id);
CREATE INDEX idx_clips_video_id ON public.clips(video_id);
CREATE INDEX idx_clips_selected ON public.clips(selected) WHERE selected = true;
CREATE INDEX idx_splices_user_id ON public.splices(user_id);
CREATE INDEX idx_exports_user_id ON public.exports(user_id);
CREATE INDEX idx_processing_jobs_status ON public.processing_jobs(status);
```

## Data Models

### TypeScript Interfaces (Frontend)

```typescript
interface User {
  id: string;
  email: string;
  full_name?: string;
  avatar_url?: string;
  subscription_tier: 'free' | 'pro' | 'enterprise';
  processing_quota: number;
  created_at: string;
  updated_at: string;
}

interface Video {
  id: string;
  user_id: string;
  title: string;
  original_filename?: string;
  file_size?: number;
  duration_seconds?: number;
  resolution_width?: number;
  resolution_height?: number;
  format?: string;
  storage_path: string;
  thumbnail_path?: string;
  upload_source: 'upload' | 'youtube' | 'trending';
  youtube_url?: string;
  processing_status: 'pending' | 'processing' | 'completed' | 'failed';
  created_at: string;
  updated_at: string;
}

interface Clip {
  id: string;
  video_id: string;
  start_time_seconds: number;
  end_time_seconds: number;
  duration_seconds: number;
  attention_score?: number;
  visual_intensity?: number;
  audio_intensity?: number;
  motion_score?: number;
  semantic_hooks: string[];
  emotion_detected?: string;
  embedding?: number[];
  thumbnail_path?: string;
  storage_path?: string;
  selected: boolean;
  created_at: string;
}

interface Splice {
  id: string;
  user_id: string;
  top_clip_id: string;
  bottom_clip_id: string;
  mode: 'semantic' | 'eclectic' | 'trending';
  similarity_score?: number;
  contrast_score?: number;
  split_ratio: number;
  audio_mix: {
    top_volume: number;
    bottom_volume: number;
  };
  text_overlays: TextOverlay[];
  preview_path?: string;
  status: 'draft' | 'processing' | 'completed' | 'failed';
  created_at: string;
  updated_at: string;
}

interface TextOverlay {
  id: string;
  text: string;
  position: {
    x: number;
    y: number;
  };
  font_size: number;
  font_family: string;
  color: string;
  animation?: {
    type: 'fade_in' | 'slide_up' | 'typewriter';
    duration: number;
  };
  style?: {
    bold: boolean;
    italic: boolean;
    shadow: boolean;
  };
}

interface Export {
  id: string;
  user_id: string;
  splice_id: string;
  filename: string;
  file_size?: number;
  resolution: string;
  fps: number;
  codec: string;
  bitrate?: number;
  duration_seconds?: number;
  storage_path: string;
  download_url?: string;
  metadata?: {
    title?: string;
    description?: string;
    hashtags?: string[];
  };
  processing_status: 'pending' | 'processing' | 'completed' | 'failed';
  error_message?: string;
  created_at: string;
  completed_at?: string;
}

interface ProcessingJob {
  id: string;
  user_id: string;
  video_id?: string;
  task_type: 'analysis' | 'splice_generation' | 'export';
  task_id: string;
  status: 'pending' | 'running' | 'completed' | 'failed';
  progress: number;
  result?: any;
  error_message?: string;
  created_at: string;
  updated_at: string;
}
```

### Pydantic Models (Backend)

```python
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum

class UploadSource(str, Enum):
    UPLOAD = "upload"
    YOUTUBE = "youtube"
    TRENDING = "trending"

class ProcessingStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"

class SpliceMode(str, Enum):
    SEMANTIC = "semantic"
    ECLECTIC = "eclectic"
    TRENDING = "trending"

class TaskType(str, Enum):
    ANALYSIS = "analysis"
    SPLICE_GENERATION = "splice_generation"
    EXPORT = "export"

class UserCreate(BaseModel):
    email: str = Field(..., description="User email address")
    password: str = Field(..., min_length=8, description="User password")
    full_name: str = Field(..., description="User full name")

class UserResponse(BaseModel):
    id: str
    email: str
    full_name: Optional[str]
    avatar_url: Optional[str]
    subscription_tier: str
    processing_quota: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class VideoUpload(BaseModel):
    title: str = Field(..., description="Video title")
    original_filename: Optional[str] = Field(None, description="Original uploaded filename")

class VideoResponse(BaseModel):
    id: str
    user_id: str
    title: str
    original_filename: Optional[str]
    file_size: Optional[int]
    duration_seconds: Optional[int]
    resolution_width: Optional[int]
    resolution_height: Optional[int]
    format: Optional[str]
    storage_path: str
    thumbnail_path: Optional[str]
    upload_source: UploadSource
    youtube_url: Optional[str]
    processing_status: ProcessingStatus
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class YouTubeUpload(BaseModel):
    url: str = Field(..., description="YouTube video URL")

class ClipResponse(BaseModel):
    id: str
    video_id: str
    start_time_seconds: float
    end_time_seconds: float
    duration_seconds: float
    attention_score: Optional[float]
    visual_intensity: Optional[float]
    audio_intensity: Optional[float]
    motion_score: Optional[float]
    semantic_hooks: List[str]
    emotion_detected: Optional[str]
    embedding: Optional[List[float]]
    thumbnail_path: Optional[str]
    storage_path: Optional[str]
    selected: bool
    created_at: datetime

    class Config:
        from_attributes = True

class AudioMix(BaseModel):
    top_volume: float = Field(default=0.7, ge=0.0, le=1.0, description="Top clip volume 0-1")
    bottom_volume: float = Field(default=0.5, ge=0.0, le=1.0, description="Bottom clip volume 0-1")

class TextOverlay(BaseModel):
    text: str = Field(..., description="Text content")
    position: Dict[str, float] = Field(..., description="X,Y position coordinates")
    font_size: int = Field(default=24, ge=12, le=72, description="Font size in pixels")
    font_family: str = Field(default="Arial", description="Font family name")
    color: str = Field(default="#FFFFFF", description="Text color hex code")
    animation: Optional[Dict[str, Any]] = Field(None, description="Animation configuration")
    style: Optional[Dict[str, bool]] = Field(None, description="Text style options")

class SpliceCreate(BaseModel):
    clip_ids: List[str] = Field(..., min_items=2, max_items=2, description="Top and bottom clip IDs")
    mode: SpliceMode = Field(..., description="Splice generation mode")
    options: Dict[str, Any] = Field(default_factory=dict, description="Additional options")

class SpliceResponse(BaseModel):
    id: str
    user_id: str
    top_clip_id: str
    bottom_clip_id: str
    mode: SpliceMode
    similarity_score: Optional[float]
    contrast_score: Optional[float]
    split_ratio: float
    audio_mix: AudioMix
    text_overlays: List[TextOverlay]
    preview_path: Optional[str]
    status: ProcessingStatus
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class ExportFormat(BaseModel):
    resolution: str = Field(default="720x1280", description="Video resolution")
    fps: int = Field(default=30, ge=15, le=60, description="Frames per second")
    codec: str = Field(default="h264", description="Video codec")
    bitrate: Optional[int] = Field(None, description="Bitrate in kbps")

class ExportMetadata(BaseModel):
    title: Optional[str] = Field(None, description="Video title")
    description: Optional[str] = Field(None, description="Video description")
    hashtags: Optional[List[str]] = Field(None, description="Hashtag list")

class ExportCreate(BaseModel):
    splice_id: str = Field(..., description="Splice ID to export")
    format: ExportFormat = Field(default_factory=ExportFormat, description="Export format settings")
    metadata: Optional[ExportMetadata] = Field(None, description="Video metadata")

class ExportResponse(BaseModel):
    id: str
    user_id: str
    splice_id: str
    filename: str
    file_size: Optional[int]
    resolution: str
    fps: int
    codec: str
    bitrate: Optional[int]
    duration_seconds: Optional[int]
    storage_path: str
    download_url: Optional[str]
    metadata: Optional[ExportMetadata]
    processing_status: ProcessingStatus
    error_message: Optional[str]
    created_at: datetime
    completed_at: Optional[datetime]

    class Config:
        from_attributes = True

class AnalysisRequest(BaseModel):
    video_id: str = Field(..., description="Video to analyze")
    sensitivity: float = Field(default=0.75, ge=0.0, le=1.0, description="Attention score threshold")

class AnalysisResponse(BaseModel):
    analysis_id: str
    status: ProcessingStatus
    estimated_completion: Optional[str]
    clips: List[ClipResponse] = []
    progress: int = Field(default=0, ge=0, le=100)

class ProcessingJobResponse(BaseModel):
    id: str
    user_id: str
    video_id: Optional[str]
    task_type: TaskType
    task_id: str
    status: ProcessingStatus
    progress: int
    result: Optional[Dict[str, Any]]
    error_message: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
```

## Integration Points

### MiniMax-M2 API Integration
```python
class MinimaxM2Client:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.minimax.chat/v1"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    async def analyze_clip(
        self,
        video_frames: List[str],  # Base64 encoded frames
        audio_transcript: str,
        duration_seconds: float,
        analysis_type: str = "attention_scoring"
    ) -> Dict[str, Any]:
        """Analyze video clip using MiniMax-M2 multimodal AI"""
        payload = {
            "video_frames": video_frames,
            "audio_transcript": audio_transcript,
            "duration_seconds": duration_seconds,
            "analysis_type": analysis_type
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.base_url}/multimodal/analyze",
                headers=self.headers,
                json=payload
            ) as response:
                if response.status == 200:
                    return await response.json()
                elif response.status == 429:
                    raise M2APIError("Rate limit exceeded", "RATE_LIMIT")
                else:
                    raise M2APIError("Analysis failed", "ANALYSIS_ERROR")

    async def generate_embeddings(self, clips: List[Dict]) -> List[List[float]]:
        """Generate semantic embeddings for clips"""
        # Implementation for semantic similarity scoring
        pass

    async def content_safety_check(self, video_path: str) -> Dict[str, Any]:
        """Check content for safety violations"""
        # Implementation for content moderation
        pass
```

### YouTube Data API Integration
```python
class YouTubeAPIClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://www.googleapis.com/youtube/v3"

    async def get_video_info(self, url: str) -> Dict[str, Any]:
        """Extract video information from YouTube URL"""
        video_id = self._extract_video_id(url)
        
        params = {
            "part": "snippet,contentDetails,statistics",
            "id": video_id,
            "key": self.api_key
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self.base_url}/videos",
                params=params
            ) as response:
                return await response.json()

    async def download_video(self, url: str) -> bytes:
        """Download video from YouTube (using yt-dlp)"""
        # Implementation using yt-dlp
        pass
```

### Tavily Search API Integration
```python
class TavilySearchClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.tavily.com/search"

    async def search_trending_videos(
        self,
        topic: str,
        limit: int = 10,
        timeframe: str = "24h"
    ) -> List[Dict[str, Any]]:
        """Search for trending videos by topic"""
        params = {
            "api_key": self.api_key,
            "query": f"trending {topic} videos TikTok YouTube",
            "search_depth": "advanced",
            "include_answer": False,
            "include_images": True,
            "include_raw_content": False,
            "max_results": limit
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.get(self.base_url, params=params) as response:
                return await response.json()
```

## Security & Compliance

### Data Protection
- **Encryption**: All user data encrypted at rest using AES-256
- **Transmission**: HTTPS/TLS 1.3 for all API communications
- **Storage**: Supabase provides enterprise-grade encryption
- **Access Control**: Role-based permissions with Supabase RLS (Row Level Security)

### GDPR Compliance
- **Consent Management**: Explicit user consent for video processing and storage
- **Right to Access**: Users can download all their data in JSON format
- **Right to Deletion**: Complete data purging via API endpoint
- **Data Portability**: Export functionality for data migration
- **Privacy by Design**: Minimal data collection, automatic cleanup

### Content Moderation
- **AI Screening**: MiniMax-M2 content safety analysis on upload
- **Automated Blocking**: Explicit content, violence, hate speech detection
- **User Appeals**: Manual review process for disputed content
- **Reporting System**: Community reporting for inappropriate content

## Performance Targets

### Response Times
- **Upload Initiation**: < 2 seconds
- **Analysis Completion**: < 30 seconds per 5-minute video
- **Splice Generation**: < 10 seconds per combination
- **Export Processing**: < 15 seconds for 30-second output
- **API Responses**: < 500ms for most endpoints

### Scalability
- **Concurrent Users**: 100+ simultaneous processing jobs
- **Daily Volume**: 1000+ videos processed
- **Storage**: Auto-scaling Supabase Storage
- **Bandwidth**: CDN delivery for all media assets

### Reliability
- **Uptime**: 99.9% availability target
- **Error Recovery**: Automatic retry with exponential backoff
- **Data Backup**: Daily automated backups
- **Monitoring**: Real-time performance and error tracking

This specification provides the foundation for building ClipSmart as an enterprise-grade content creation platform within the Aether ecosystem.