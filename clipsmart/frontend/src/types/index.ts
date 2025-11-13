// User Types
export interface User {
  id: string;
  email: string;
  full_name?: string;
  avatar_url?: string;
  subscription_tier: 'free' | 'pro' | 'enterprise';
  processing_quota: number;
  created_at: string;
  updated_at: string;
}

export interface UserProfile {
  id: string;
  email: string;
  full_name?: string;
  avatar_url?: string;
  subscription_tier: 'free' | 'pro' | 'enterprise';
  processing_quota: number;
  used_quota: number;
  videos_processed: number;
  clips_created: number;
  splices_exported: number;
  created_at: string;
}

// Video Types
export interface Video {
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
  error_message?: string;
  created_at: string;
  updated_at: string;
}

export interface VideoUpload {
  title: string;
  file?: File;
  youtube_url?: string;
  upload_source: 'upload' | 'youtube';
}

export interface VideoUploadProgress {
  upload_id: string;
  progress: number;
  speed: number; // bytes per second
  eta: number; // seconds remaining
  status: 'uploading' | 'processing' | 'completed' | 'error';
}

// Clip Types
export interface Clip {
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

export interface ClipAnalysis {
  analysis_id: string;
  video_id: string;
  status: 'pending' | 'processing' | 'completed' | 'failed';
  clips: Clip[];
  progress: number;
  estimated_completion?: string;
  error_message?: string;
}

// Splice Types
export interface Splice {
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
  error_message?: string;
  created_at: string;
  updated_at: string;
}

export interface SpliceCreate {
  clip_ids: [string, string]; // [top_clip_id, bottom_clip_id]
  mode: 'semantic' | 'eclectic' | 'trending';
  options?: {
    split_ratio?: number;
    audio_mix?: {
      top_volume?: number;
      bottom_volume?: number;
    };
    text_overlays?: TextOverlay[];
  };
}

export interface TextOverlay {
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

// Export Types
export interface Export {
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
    thumbnail_url?: string;
  };
  processing_status: 'pending' | 'processing' | 'completed' | 'failed';
  error_message?: string;
  created_at: string;
  completed_at?: string;
}

export interface ExportFormat {
  resolution: '720x1280' | '1080x1920';
  fps: 30;
  codec: 'h264';
  bitrate?: number;
}

export interface ExportCreate {
  splice_id: string;
  format?: ExportFormat;
  metadata?: {
    title?: string;
    description?: string;
    hashtags?: string[];
  };
}

// API Response Types
export interface ApiResponse<T = any> {
  success: boolean;
  data?: T;
  error?: {
    code: string;
    message: string;
    details?: any;
  };
  meta?: {
    total?: number;
    page?: number;
    limit?: number;
  };
}

export interface PaginatedResponse<T> extends ApiResponse<T[]> {
  meta: {
    total: number;
    page: number;
    limit: number;
    has_more: boolean;
  };
}

// Processing Job Types
export interface ProcessingJob {
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

// Trending Types
export interface TrendingVideo {
  id: string;
  title: string;
  thumbnail_url?: string;
  duration?: number;
  view_count?: number;
  trending_score?: number;
  source: 'youtube' | 'tiktok' | 'instagram';
  video_url: string;
  extracted_at: string;
}

export interface TrendingHashtag {
  tag: string;
  count: number;
  trending_score: number;
  category: string;
}

// Analytics Types
export interface UserAnalytics {
  videos_processed: number;
  clips_extracted: number;
  splices_created: number;
  exports_completed: number;
  total_processing_time: number;
  average_clip_score: number;
  favorite_modes: {
    semantic: number;
    eclectic: number;
    trending: number;
  };
  export_formats: {
    resolution: string;
    count: number;
  }[];
}

// Upload Types
export interface FileUploadResponse {
  upload_id: string;
  file_size: number;
  estimated_processing_time: number;
  chunk_size: number;
  total_chunks: number;
}

export interface UploadChunk {
  chunk_index: number;
  data: ArrayBuffer;
  checksum?: string;
}

// Component Props Types
export interface VideoPlayerProps {
  src: string;
  poster?: string;
  onTimeUpdate?: (currentTime: number) => void;
  onDurationChange?: (duration: number) => void;
  onPlay?: () => void;
  onPause?: () => void;
  className?: string;
  autoPlay?: boolean;
  loop?: boolean;
  muted?: boolean;
}

export interface ClipGridProps {
  clips: Clip[];
  onClipSelect?: (clipId: string, selected: boolean) => void;
  onClipPreview?: (clipId: string) => void;
  selectedClips?: string[];
  className?: string;
}

export interface SpliceEditorProps {
  splice: Splice;
  onUpdate?: (updates: Partial<Splice>) => void;
  onPreview?: () => void;
  onExport?: () => void;
  className?: string;
}

export interface ExportModalProps {
  splice: Splice;
  onExport?: (format: ExportFormat, metadata?: any) => void;
  onClose?: () => void;
}

// Store Types
export interface AppStore {
  user: User | null;
  videos: Video[];
  currentVideo: Video | null;
  clips: Clip[];
  splices: Splice[];
  currentSplice: Splice | null;
  exports: Export[];
  isLoading: boolean;
  error: string | null;
}

export interface UploadStore {
  uploads: VideoUploadProgress[];
  isUploading: boolean;
  uploadProgress: number;
}

// Hook Types
export interface UseVideoUploadOptions {
  onProgress?: (progress: VideoUploadProgress) => void;
  onComplete?: (video: Video) => void;
  onError?: (error: string) => void;
}

export interface UseSpliceGenerationOptions {
  onStart?: () => void;
  onProgress?: (progress: number) => void;
  onComplete?: (splice: Splice) => void;
  onError?: (error: string) => void;
}

export interface UseExportOptions {
  onStart?: () => void;
  onProgress?: (progress: number) => void;
  onComplete?: (export: Export) => void;
  onError?: (error: string) => void;
}

// Error Types
export interface AppError {
  code: string;
  message: string;
  details?: any;
  timestamp: string;
}

export type ErrorType = 
  | 'UPLOAD_FAILED'
  | 'ANALYSIS_FAILED'
  | 'SPLICE_FAILED'
  | 'EXPORT_FAILED'
  | 'AUTHENTICATION_FAILED'
  | 'PERMISSION_DENIED'
  | 'QUOTA_EXCEEDED'
  | 'NETWORK_ERROR'
  | 'VALIDATION_ERROR';

// MiniMax-M2 API Types
export interface MinimaxAnalysisRequest {
  video_frames: string[]; // Base64 encoded frames
  audio_transcript: string;
  duration_seconds: number;
  analysis_type: 'attention_scoring' | 'semantic_embedding' | 'content_safety';
}

export interface MinimaxAnalysisResponse {
  attention_score: number;
  visual_intensity: number;
  audio_intensity: number;
  emotion_detected: string;
  motion_score: number;
  semantic_hooks: string[];
  embedding: number[];
  confidence: number;
}

export interface MinimaxEmbedding {
  vector: number[];
  dimension: number;
  model_version: string;
}

// YouTube API Types
export interface YouTubeVideoInfo {
  id: string;
  title: string;
  description: string;
  thumbnail_url: string;
  duration: string; // ISO 8601 duration
  view_count: number;
  like_count: number;
  channel_title: string;
  published_at: string;
}

// Tavily Search Types
export interface TavilySearchResult {
  title: string;
  url: string;
  content: string;
  score: number;
  published_date?: string;
}

// Form Types
export interface LoginForm {
  email: string;
  password: string;
}

export interface RegisterForm {
  email: string;
  password: string;
  confirm_password: string;
  full_name: string;
}

export interface SpliceSettingsForm {
  mode: 'semantic' | 'eclectic' | 'trending';
  split_ratio: number;
  audio_mix: {
    top_volume: number;
    bottom_volume: number;
  };
  text_overlays: TextOverlay[];
}

export interface ExportSettingsForm {
  format: ExportFormat;
  metadata: {
    title?: string;
    description?: string;
    hashtags?: string[];
  };
}