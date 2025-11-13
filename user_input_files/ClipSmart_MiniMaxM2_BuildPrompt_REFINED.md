# ClipSmart - Production Build Prompt for MiniMax-M2 Agent
**Version:** 2.0 - Enterprise Ready  
**Target:** MiniMax-M2 Agent Builder (Free Pro Trial ends Nov 7th)  
**Company:** AetherPro Technologies LLC  
**Integration:** Part of the Aether Ecosystem  

---

## 🎯 MISSION CRITICAL OVERVIEW

You are an elite full-stack AI engineer building **ClipSmart**, a production-grade web application that transforms long-form videos into viral-ready split-screen shorts. This is a flagship product for AetherPro Technologies LLC, designed to integrate seamlessly with the Aether ecosystem (AetherPro OS, AetherAgentForge, AetherInterface).

**Core Value Proposition:** Analyze long-form content → Extract attention-grabbing clips → Generate viral split-screen compositions → Export to TikTok/YouTube Shorts format.

---

## 🏗️ ARCHITECTURE & TECH STACK

### Frontend Stack
- **Framework:** Next.js 14+ (App Router, TypeScript, React Server Components)
- **UI Library:** Tailwind CSS 3.4+ with custom AetherPro theme (ethereal blues, neon accents, glass morphism)
- **Animation:** Framer Motion for smooth transitions, loading states
- **Video Player:** React-Player with custom controls + timeline scrubber
- **State Management:** Zustand for client state, React Query for server state
- **Auth:** Supabase Auth (OAuth providers: Google, GitHub, Twitter)
- **Upload/Storage:** Direct S3-compatible upload (Supabase Storage), chunked upload for large files (>500MB)

### Backend Stack
- **API Framework:** FastAPI (Python 3.11+) with async/await throughout
- **Task Queue:** Celery 5.3+ with Redis as broker (for video processing jobs)
- **Video Processing:**
  - FFmpeg 6.0+ (clip extraction, overlay composition, encoding)
  - OpenCV 4.8+ (frame analysis, motion detection, scene change detection)
  - PyDub for audio processing (volume normalization, peak detection)
- **AI/ML Integration:**
  - **Primary:** MiniMax-M2 API for multimodal analysis (vision + audio + language)
  - **Fallback:** OpenCV-based heuristics if API quota exceeded
  - **Embedding Generation:** M2 embeddings for semantic similarity scoring
  - **Audio Transcription:** Whisper API or M2 transcription
- **External APIs:**
  - YouTube Data API v3 (video fetching, metadata)
  - Tavily Search API (trending video discovery)
  - Optional: TikTok/Instagram APIs for direct upload (future)

### Database & Infrastructure
- **Primary DB:** Supabase PostgreSQL (user data, video metadata, clip library)
- **Vector Store:** pgvector extension for clip embeddings (similarity search)
- **Caching:** Redis for session data, API response caching, job status
- **File Storage:** Supabase Storage (S3-compatible) with CDN delivery
- **Deployment:**
  - Frontend: Vercel (Edge Functions for serverless API routes)
  - Backend: Railway.app or Render.com (Docker containers)
  - Dev Environment: Docker Compose for local full-stack development

---

## 🎨 USER FLOW & FEATURES

### Phase 1: Video Input (Multiple Sources)
1. **Local Upload:** Drag-and-drop or file picker, chunked upload with progress bar
2. **YouTube URL:** Paste link, app fetches and caches video temporarily
3. **Trending Discovery:** Search Tavily API for viral videos by topic/hashtag
4. **User Library:** Access previously uploaded/analyzed videos

**UI Requirements:**
- Clean dropzone with visual feedback (hover, drag-over states)
- Real-time upload progress with speed/ETA
- Thumbnail previews for all uploaded videos
- Support formats: MP4, MOV, AVI, WebM (transcode to H.264 if needed)

### Phase 2: AI-Powered Clip Extraction
**MiniMax-M2 Analysis Pipeline:**

1. **Scene Segmentation:**
   - Detect scene changes using OpenCV + M2 vision analysis
   - Segment video into 5-15 second chunks
   - Target: 8-12 clips per 10-minute video

2. **Attention Scoring (Multi-Modal):**
   - **Visual Analysis (M2):**
     - Facial expression intensity (surprise, joy, shock)
     - Motion velocity (sudden movements, camera pans)
     - Visual complexity (color saturation, object density)
   - **Audio Analysis (M2 + PyDub):**
     - Volume peaks (laughs, shouts, dramatic pauses)
     - Speech emotion detection via M2 transcription sentiment
     - Music intensity changes
   - **Semantic Content (M2 Language):**
     - Hook phrases detection ("Wait for it", "You won't believe")
     - Question/answer patterns
     - Conflict/resolution arcs

3. **Ranking Algorithm:**
   ```python
   clip_score = (
       0.35 * visual_intensity +
       0.30 * audio_peak_score +
       0.20 * motion_score +
       0.15 * semantic_hook_score
   )
   # Filter: keep only clips with score > 75th percentile
   ```

4. **User Review Interface:**
   - Grid view of top 10-20 clips with thumbnails + scores
   - Inline video preview on hover
   - Manual selection/deselection checkboxes
   - "Re-analyze with different sensitivity" slider

### Phase 3: Split-Screen Splice Generation
**Three Splice Modes:**

#### Mode 1: Semantic Relevance (Contextual Pairing)
- Use M2 embeddings to compute cosine similarity between clips
- Pair clips with 0.65-0.85 similarity (related but not identical)
- **Example:** Top clip = "DIY phone stand hack", Bottom clip = "Tech review channel intro"
- **UI:** Show similarity score + reason ("Both about tech gadgets")

#### Mode 2: Eclectic Contrast (Viral Chaos)
- Pair clips with LOW similarity (<0.3) for comedic/surprising effect
- Prioritize contrasting emotions (calm top + chaotic bottom)
- **Example:** Top clip = "Zen meditation guide", Bottom clip = "High-speed skateboard crash"
- **UI:** Show contrast reason ("Unexpected juxtaposition for engagement")

#### Mode 3: Trending Fusion (User Interest + Viral Content)
- Bottom clip: User's uploaded content (their channel focus)
- Top clip: Trending video from Tavily search (related topic)
- **Example:** Bottom = User's coding tutorial, Top = Viral tech news reaction
- **UI:** Show trending score + source (TikTok, YouTube Shorts, etc.)

**Splice Composition UI:**
- Drag-and-drop interface to swap top/bottom clips
- Real-time preview with adjustable split ratio (default 50/50, allow 60/40 or 40/60)
- Audio mixing controls:
  - Top clip volume slider (0-100%)
  - Bottom clip volume slider (0-100%)
  - Auto-ducking option (lower bottom audio when top audio peaks)
- Text overlay editor:
  - Add captions/titles with M2-suggested hooks
  - Font selection, position, animation presets

### Phase 4: Export & Optimization
**Output Specifications:**
- **Resolution:** 720x1280 (9:16 portrait) or 1080x1920 (user selectable)
- **Codec:** H.264 (high compatibility) with AAC audio
- **Bitrate:** 5-8 Mbps (good quality, reasonable file size)
- **Duration:** 15-60 seconds (optimal for TikTok/Shorts)
- **Framerate:** 30fps (smooth playback)

**Export Options:**
- Direct download (MP4 file)
- Save to user library (Supabase Storage)
- Copy shareable link (public URL with expiration)
- Future: Direct upload to TikTok/YouTube API (Phase 2 feature)

**Post-Export Features:**
- Generate thumbnail suggestions (M2 identifies best frame)
- Auto-generate video descriptions with hooks (M2 language model)
- Hashtag recommendations based on content (M2 + Tavily trending tags)

---

## 🤖 MINIMAX-M2 INTEGRATION DETAILS

### API Endpoint Structure
```python
# Primary M2 Analysis Endpoint
POST /api/analyze-clip
{
  "video_frames": [base64_frame_1, base64_frame_2, ...],  # Every 0.5s
  "audio_transcript": "full audio text from Whisper",
  "duration_seconds": 12,
  "analysis_type": "attention_scoring"  # or "semantic_embedding"
}

# M2 Response Format
{
  "attention_score": 0.87,
  "visual_intensity": 0.92,
  "audio_intensity": 0.81,
  "emotion_detected": "excitement",
  "motion_score": 0.88,
  "semantic_hooks": ["Wait for it", "Unbelievable result"],
  "embedding": [0.234, -0.567, ...],  # 1536-dim vector
  "confidence": 0.94
}
```

### Rate Limiting & Fallback Strategy
```python
# M2 API Quota Management
if m2_quota_exceeded():
    # Fallback to OpenCV + PyDub heuristics
    use_opencv_motion_detection()
    use_pydub_audio_peaks()
    use_basic_scene_segmentation()
    log_warning("Using fallback analysis - reduced accuracy")
else:
    # Use M2 for superior analysis
    use_minimax_m2_api()
```

### Error Handling
```python
try:
    m2_response = await call_minimax_m2_api(clip_data)
except M2APIError as e:
    if e.code == "RATE_LIMIT":
        queue_for_retry(clip_data, delay=60)  # Retry after 1 min
    elif e.code == "INVALID_CONTENT":
        log_error(f"M2 rejected content: {e.message}")
        use_fallback_analysis()
    else:
        raise  # Critical error, surface to user
```

---

## 🔐 SECURITY & PRIVACY

### Data Protection
- **Video Processing:** Process in isolated Docker containers, auto-delete after 24h
- **User Data:** All PII encrypted at rest (Supabase encryption)
- **GDPR Compliance:** 
  - Explicit consent for video storage
  - Right to delete (user can purge all their data)
  - Data export option (download all clips as ZIP)
- **API Keys:** Stored in environment variables, never in code
  - `MINIMAX_API_KEY`
  - `YOUTUBE_API_KEY`
  - `TAVILY_API_KEY`
  - `SUPABASE_URL` & `SUPABASE_ANON_KEY`

### Content Moderation
- Run M2 content safety check on all uploaded videos
- Block uploads containing:
  - Explicit adult content
  - Violence/gore
  - Hate speech/discriminatory content
- User can appeal false positives (manual review queue)

---

## 📊 PERFORMANCE & SCALABILITY

### Target Benchmarks
- **Upload Time:** <5s for 100MB video (chunked upload)
- **Analysis Time:** <30s for 5-minute video (M2 API + FFmpeg)
- **Splice Generation:** <10s per clip pair (FFmpeg overlay)
- **Export Time:** <15s for 30-second split-screen video
- **Concurrent Users:** Support 100+ simultaneous processing jobs (Celery workers)

### Optimization Strategies
1. **Video Transcoding:** Use FFmpeg's `-preset ultrafast` for initial processing, `medium` for final export
2. **Frame Sampling:** Send every 2nd or 3rd frame to M2 (not every frame) to reduce API calls
3. **Caching:** Cache M2 embeddings in PostgreSQL (avoid re-analyzing same clips)
4. **CDN Delivery:** Serve all video assets via Supabase CDN with aggressive caching headers
5. **Progressive Loading:** Stream video previews as they're generated (don't wait for full render)

### Monitoring & Logging
- **Sentry:** Error tracking and performance monitoring
- **LogTail/Datadog:** Centralized logging for debugging
- **Metrics Dashboard:** 
  - Videos processed per hour
  - Average M2 API response time
  - User engagement (clips created, exports downloaded)
  - Error rates by component

---

## 🧪 TESTING & QUALITY ASSURANCE

### Automated Test Suite
```bash
# Frontend Tests (Jest + React Testing Library)
- Component rendering tests (80%+ coverage)
- User interaction flows (upload, preview, export)
- API integration tests (mocked M2 responses)

# Backend Tests (Pytest)
- Video processing pipeline (sample videos in test fixtures)
- M2 API integration (mock responses for deterministic tests)
- Clip scoring accuracy (compare against manual labels)
- Edge cases: corrupt videos, unsupported formats, oversized files

# E2E Tests (Playwright)
- Full user journey: upload → analyze → splice → export
- Cross-browser testing (Chrome, Firefox, Safari)
- Mobile responsiveness (iOS Safari, Chrome Android)
```

### Manual QA Checklist
- [ ] Upload 10 different video formats (MP4, MOV, AVI, etc.)
- [ ] Test with videos of varying lengths (30s, 5min, 30min, 1hr)
- [ ] Verify M2 attention scoring on known viral clips (should score >0.8)
- [ ] Check semantic pairing accuracy (10 test pairs, manual relevance rating)
- [ ] Export quality verification (1080p sharpness, audio sync)
- [ ] Mobile UI/UX on 3 different devices
- [ ] Accessibility audit (keyboard navigation, screen readers)

---

## 🚀 DEPLOYMENT & LAUNCH

### Development Setup
```bash
# 1. Clone and install dependencies
git clone https://github.com/aetherpro/clipsmart.git
cd clipsmart
npm install  # Frontend
pip install -r requirements.txt  # Backend

# 2. Environment configuration
cp .env.example .env
# Fill in API keys: MINIMAX_API_KEY, YOUTUBE_API_KEY, etc.

# 3. Start services with Docker Compose
docker-compose up -d  # Postgres, Redis, Backend, Frontend

# 4. Access app
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

### Production Deployment
```bash
# Frontend (Vercel)
vercel --prod

# Backend (Railway.app)
railway up --environment production

# Database migrations
npx prisma migrate deploy

# Environment variables (set in Vercel/Railway dashboards)
MINIMAX_API_KEY=sk-xxx
SUPABASE_URL=https://xxx.supabase.co
# ... etc.
```

### Post-Launch Monitoring
- Set up Sentry alerts for critical errors (API failures, processing timeouts)
- Monitor M2 API quota usage (set alerts at 80% threshold)
- Track user metrics in Supabase Analytics
- Weekly review of top error logs and user feedback

---

## 🔮 AETHERPRO ECOSYSTEM INTEGRATION

### Phase 1 (Current Build)
- **Branding:** AetherPro color scheme (ethereal blues, neon purple accents, dark mode default)
- **Footer:** "Powered by AetherPro Technologies LLC & MiniMax-M2"
- **Stub Environment Variables:**
  ```bash
  AETHER_OS_API_URL=https://api.aetherpro.com  # Future hook
  AETHER_AGENT_FORGE_TOKEN=xxx  # Marketplace integration
  AETHER_GRID_WEBHOOK=https://grid.aetherpro.com/webhook  # Agent swarm
  ```

### Phase 2 (Future Roadmap)
- **AetherAgentForge Marketplace:** List ClipSmart as an AI agent workflow
- **AetherInterface Integration:** Embed ClipSmart as a module in AetherInterface dashboard
- **AetherGrid Agentic Remixing:** Deploy agent swarm to auto-remix viral trends from ClipSmart library
- **N8N Workflow Hooks:** Trigger ClipSmart processing from N8N automation workflows

---

## 📋 OUTPUT DELIVERABLES

Generate the following in sequential order:

### 1. Project Specification Document (Markdown)
**Filename:** `CLIPSMART_SPEC.md`
- Executive summary (1 paragraph)
- User personas (3 types: Content Creators, Marketers, Casual Users)
- Wireframes (ASCII art or detailed descriptions for Figma)
- API endpoint specifications:
  - `POST /api/upload` (multipart file upload)
  - `POST /api/analyze` (M2 clip extraction)
  - `POST /api/splice` (generate split-screen video)
  - `GET /api/library` (user's clip library)
  - `POST /api/export` (final video generation)
- Database schema (PostgreSQL tables: users, videos, clips, splices, exports)
- Data models (TypeScript interfaces + Pydantic models)

### 2. Code Scaffold
**Folder Structure:**
```
clipsmart/
├── frontend/
│   ├── app/
│   │   ├── page.tsx              # Landing page
│   │   ├── upload/page.tsx       # Video upload UI
│   │   ├── analyze/page.tsx      # Clip extraction UI
│   │   ├── splice/page.tsx       # Splice editor UI
│   │   └── library/page.tsx      # User's clip library
│   ├── components/
│   │   ├── VideoPlayer.tsx
│   │   ├── ClipGrid.tsx
│   │   ├── SpliceEditor.tsx
│   │   └── ExportModal.tsx
│   ├── lib/
│   │   ├── api.ts                # API client
│   │   ├── supabase.ts           # Supabase client
│   │   └── stores/               # Zustand stores
│   ├── styles/
│   │   └── aetherpro-theme.css   # Custom AetherPro theme
│   └── package.json
├── backend/
│   ├── app/
│   │   ├── main.py               # FastAPI app entry
│   │   ├── api/
│   │   │   ├── upload.py         # Upload endpoints
│   │   │   ├── analyze.py        # M2 analysis endpoints
│   │   │   ├── splice.py         # Splice generation endpoints
│   │   │   └── export.py         # Export endpoints
│   │   ├── services/
│   │   │   ├── minimax_m2.py     # M2 API integration
│   │   │   ├── video_processor.py # FFmpeg + OpenCV
│   │   │   ├── audio_analyzer.py  # PyDub audio analysis
│   │   │   └── clip_scorer.py     # Attention scoring logic
│   │   ├── models/
│   │   │   └── schemas.py        # Pydantic models
│   │   ├── db/
│   │   │   └── database.py       # SQLAlchemy setup
│   │   └── tasks/
│   │       └── celery_tasks.py   # Async video processing
│   ├── requirements.txt
│   └── Dockerfile
├── docker-compose.yml
├── .env.example
├── README.md
└── DEPLOYMENT_GUIDE.md
```

### 3. Full Implementation
**Requirements:**
- Complete, runnable code for all components
- ESLint + Prettier configured (frontend)
- Black + isort configured (backend)
- Environment variable validation (Zod for TS, Pydantic for Python)
- Mock M2 API responses for local testing (JSON fixtures)
- Dockerfile for backend with multi-stage build
- Docker Compose with Postgres, Redis, Backend, Frontend services

### 4. Testing & Validation
**Included Tests:**
- Frontend: Jest tests for 3 key components (VideoPlayer, ClipGrid, SpliceEditor)
- Backend: Pytest tests for M2 integration, video processing, clip scoring
- E2E: Playwright script for full user flow (upload → export)
- Performance: Load test script (simulate 10 concurrent users processing videos)

**Validation Run Simulation:**
```bash
# Pseudo-execution on sample input
INPUT_VIDEO_1: "https://youtube.com/watch?v=tech_tutorial_123"
INPUT_VIDEO_2: "https://youtube.com/watch?v=viral_hack_456"

EXPECTED_OUTPUT:
- 8 clips extracted from video 1 (avg score: 0.82)
- 6 clips extracted from video 2 (avg score: 0.79)
- 12 splice pairs generated (Semantic mode: 4, Eclectic: 4, Trending: 4)
- 3 exports created (720x1280, 30fps, H.264, total size: 45MB)
- Processing time: 28 seconds
- M2 API calls: 47 (within quota)

STATUS: ✅ Build complete - Ready for deployment
NEXT STEP: Deploy to Vercel (frontend) + Railway (backend) for beta testing
```

### 5. Documentation
**README.md Sections:**
- Project overview (1 paragraph with ClipSmart value prop)
- Tech stack (bullet list with versions)
- Prerequisites (Node 18+, Python 3.11+, Docker, API keys)
- Installation (step-by-step with commands)
- Usage (screenshots or ASCII diagrams of UI flow)
- API documentation (link to FastAPI `/docs` endpoint)
- Deployment (Vercel + Railway instructions)
- Troubleshooting (common errors + fixes)
- Contributing (if open-source in future)
- License (MIT or proprietary)

---

## 🎯 CRITICAL SUCCESS FACTORS

### Non-Negotiables (Must-Haves)
1. ✅ **Production Quality:** Clean, maintainable code with 80%+ test coverage
2. ✅ **MiniMax-M2 Integration:** Functional API calls with error handling and fallbacks
3. ✅ **Video Processing:** Accurate clip extraction and smooth split-screen composition
4. ✅ **User Experience:** Intuitive UI with real-time feedback (no blank loading screens)
5. ✅ **Scalability:** Handle 100+ concurrent users without degradation
6. ✅ **Security:** GDPR-compliant data handling, secure API key management

### Nice-to-Haves (Enhancements)
- 🌟 Auto-generated voiceovers using M2 text-to-speech
- 🌟 Text overlay suggestions based on M2 content analysis
- 🌟 Social media scheduling (post directly to TikTok/YouTube)
- 🌟 AI-generated thumbnails with click-optimization scoring
- 🌟 Collaborative editing (share splice projects with team)

### Innovation Opportunities
- 💡 **Agentic Remixing:** Deploy AI agents to continuously generate new splice combinations from user library
- 💡 **Virality Prediction:** Train M2 on viral video dataset to predict engagement before posting
- 💡 **Trend Surfing:** Auto-detect trending topics via Tavily and suggest relevant splices
- 💡 **Personalized Recommendations:** Use user watch history to suggest optimal splice pairings

---

## 🏁 FINAL NOTES FOR MINIMAX-M2 AGENT

**Execution Priorities:**
1. Reliability over novelty (stable > flashy)
2. M2 integration is core (not optional)
3. Modular code (easy to extend/replace components)
4. User feedback loops (progress bars, error messages, tooltips)
5. AetherPro branding (consistent visual identity)

**Code Quality Standards:**
- Every function has docstrings (Google style for Python, JSDoc for TypeScript)
- No hardcoded values (use environment variables or config files)
- Error logging for all external API calls (M2, YouTube, Tavily)
- Graceful degradation (app should work even if M2 API is down)

**Time Management:**
- Spec doc: 30 minutes
- Code scaffold: 1 hour
- Full implementation: 4-6 hours
- Testing & docs: 1.5 hours
- **Total:** ~8 hours of focused development

**Output Format:**
- Generate as ZIP file or GitHub repo
- Include `RUN_INSTRUCTIONS.md` with copy-paste commands for setup
- Provide sample `.env` file with placeholder API keys
- Include 2 sample videos (5MB each, Creative Commons licensed) for testing

---

## 🚀 EXECUTE NOW

This is ClipSmart - AetherPro's viral content engine. Build it with precision, innovation, and enterprise-grade reliability. Make it unbreakable. Make it viral. Make it Aether.

**GO TIME!** 🔥
