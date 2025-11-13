# ClipSmart Build - Quality Validation Checklist

## 📋 Use this checklist to verify MiniMax-M2's output

### 🏗️ Architecture & Setup (10 items)

- [ ] **Folder structure** matches specification (frontend/, backend/, docker-compose.yml)
- [ ] **Tech stack versions** are correct (Next.js 14+, Python 3.11+, etc.)
- [ ] **.env.example** file included with all required keys
- [ ] **Docker Compose** file with Postgres, Redis, Backend, Frontend services
- [ ] **Package.json** (frontend) with all dependencies listed
- [ ] **Requirements.txt** (backend) with pinned versions
- [ ] **README.md** with clear setup instructions
- [ ] **Dockerfile** for backend with multi-stage build
- [ ] **TypeScript** configured (tsconfig.json)
- [ ] **ESLint/Prettier** (frontend) and **Black/isort** (backend) configs present

**Score:** ___/10

---

### 🎨 Frontend Implementation (12 items)

- [ ] **Landing page** (app/page.tsx) with AetherPro branding
- [ ] **Upload page** with drag-and-drop + file picker
- [ ] **Analyze page** with clip grid and real-time previews
- [ ] **Splice editor** with drag-and-drop interface
- [ ] **Library page** for user's saved clips
- [ ] **VideoPlayer component** with custom controls
- [ ] **ClipGrid component** with thumbnails and scores
- [ ] **SpliceEditor component** with audio mixing controls
- [ ] **ExportModal component** with format options
- [ ] **Tailwind CSS** with AetherPro theme (blues, purples, dark mode)
- [ ] **Zustand stores** for state management
- [ ] **Supabase Auth** integration (login/signup)

**Score:** ___/12

---

### ⚙️ Backend Implementation (15 items)

- [ ] **FastAPI app** (main.py) with CORS and middleware
- [ ] **Upload endpoint** (/api/upload) with chunked upload support
- [ ] **Analyze endpoint** (/api/analyze) calling M2 API
- [ ] **Splice endpoint** (/api/splice) generating split-screen videos
- [ ] **Export endpoint** (/api/export) with format options
- [ ] **Library endpoint** (/api/library) returning user's clips
- [ ] **MiniMax-M2 integration** (minimax_m2.py service)
- [ ] **Video processor** (video_processor.py) using FFmpeg + OpenCV
- [ ] **Audio analyzer** (audio_analyzer.py) using PyDub
- [ ] **Clip scorer** (clip_scorer.py) with attention algorithm
- [ ] **Celery tasks** (celery_tasks.py) for async processing
- [ ] **Pydantic models** (schemas.py) for request/response validation
- [ ] **SQLAlchemy setup** (database.py) with Supabase connection
- [ ] **Error handling** for M2 API failures with fallbacks
- [ ] **Rate limiting** logic for M2 API calls

**Score:** ___/15

---

### 🤖 MiniMax-M2 Integration (8 items)

- [ ] **M2 API client** with proper authentication (MINIMAX_API_KEY)
- [ ] **Attention scoring** request with frames + audio transcript
- [ ] **Embedding generation** request for semantic similarity
- [ ] **Response parsing** for attention scores, emotions, hooks
- [ ] **Rate limit handling** with retry logic
- [ ] **Fallback to OpenCV** when M2 quota exceeded
- [ ] **Error logging** for all M2 API failures
- [ ] **Caching** of M2 embeddings in PostgreSQL

**Score:** ___/8

---

### 🎬 Video Processing (10 items)

- [ ] **Scene segmentation** into 5-15s chunks
- [ ] **Clip extraction** using FFmpeg
- [ ] **Motion detection** using OpenCV
- [ ] **Audio peak detection** using PyDub
- [ ] **Attention scoring** with weighted components (0.35/0.30/0.20/0.15)
- [ ] **Semantic relevance** mode (0.65-0.85 similarity)
- [ ] **Eclectic contrast** mode (<0.3 similarity)
- [ ] **Trending fusion** mode (Tavily API integration)
- [ ] **Split-screen composition** with FFmpeg overlay
- [ ] **Export optimization** (720x1280, H.264, 30fps, 5-8Mbps)

**Score:** ___/10

---

### 🧪 Testing & Quality (8 items)

- [ ] **Jest tests** for 3+ React components
- [ ] **Pytest tests** for M2 integration
- [ ] **Pytest tests** for video processing pipeline
- [ ] **Pytest tests** for clip scoring accuracy
- [ ] **Playwright E2E test** for full user flow
- [ ] **Test fixtures** with sample videos
- [ ] **Mock M2 responses** for deterministic tests
- [ ] **Test coverage** reports configured (80%+ target)

**Score:** ___/8

---

### 🔐 Security & Privacy (7 items)

- [ ] **Environment variables** validation (Zod for TS, Pydantic for Python)
- [ ] **API keys** never hardcoded (all from .env)
- [ ] **Content moderation** using M2 safety checks
- [ ] **GDPR compliance** features (consent, delete, export)
- [ ] **Isolated processing** (Docker containers, auto-delete after 24h)
- [ ] **Error logging** with Sentry integration
- [ ] **Rate limiting** on API endpoints

**Score:** ___/7

---

### 📊 Performance & Scalability (6 items)

- [ ] **Celery workers** configured for async jobs
- [ ] **Redis** for caching and job queue
- [ ] **CDN delivery** for video assets (Supabase Storage)
- [ ] **Chunked upload** for large files (>500MB)
- [ ] **Frame sampling** optimization (every 2nd/3rd frame to M2)
- [ ] **Progressive loading** of video previews

**Score:** ___/6

---

### 🌐 AetherPro Integration (6 items)

- [ ] **AetherPro branding** (colors, logo, footer)
- [ ] **Stub env vars** for future integration (AETHER_OS_API_URL, etc.)
- [ ] **Dark mode** by default
- [ ] **Ethereal blues + neon purple** color scheme
- [ ] **"Powered by AetherPro & MiniMax-M2"** footer
- [ ] **Modal selector** compatible with AetherInterface 359 models

**Score:** ___/6

---

### 📚 Documentation (7 items)

- [ ] **README.md** with project overview
- [ ] **Setup instructions** (copy-paste commands)
- [ ] **Tech stack** section with versions
- [ ] **API documentation** (link to FastAPI /docs)
- [ ] **Deployment guide** (Vercel + Railway)
- [ ] **Troubleshooting** section (common errors)
- [ ] **CLIPSMART_SPEC.md** with wireframes and data models

**Score:** ___/7

---

### 🚀 Deployment Readiness (6 items)

- [ ] **RUN_INSTRUCTIONS.md** with quick-start commands
- [ ] **Sample videos** included for testing (5MB each, Creative Commons)
- [ ] **Validation run** output with metrics
- [ ] **Vercel deployment** configuration (vercel.json)
- [ ] **Railway deployment** configuration (railway.toml or Dockerfile)
- [ ] **Database migrations** setup (Prisma or Alembic)

**Score:** ___/6

---

## 📈 Overall Quality Assessment

**Total Score:** ___/95

### Scoring Guide:
- **90-95:** 🏆 **Excellent** - Production-ready, deploy immediately
- **80-89:** ✅ **Good** - Minor fixes needed, mostly ready
- **70-79:** ⚠️ **Acceptable** - Several issues to address before deploy
- **60-69:** ❌ **Needs Work** - Significant gaps, major revisions required
- **<60:** 🚫 **Start Over** - Missing too many critical components

---

## 🎯 Critical Must-Haves (Red Flags if Missing)

These 10 items are **non-negotiable** for a functional ClipSmart:

1. ✅ MiniMax-M2 API integration working
2. ✅ FFmpeg video processing functional
3. ✅ Split-screen composition works
4. ✅ Upload/download endpoints operational
5. ✅ Supabase Auth working
6. ✅ Celery async tasks running
7. ✅ Docker Compose starts all services
8. ✅ Frontend and backend communicate properly
9. ✅ Error handling prevents crashes
10. ✅ Basic README with setup instructions

**Critical Items Present:** ___/10

If <8 critical items are present, **do not deploy** - iterate with MiniMax-M2 agent.

---

## 🐛 Common Issues to Watch For

### Based on typical AI code generation problems:

- [ ] **Missing .env variables** - Check if all API keys are documented
- [ ] **Hardcoded localhost URLs** - Should be env vars (API_BASE_URL)
- [ ] **No error boundaries** - React should have error fallbacks
- [ ] **Infinite loops** - Check useEffect dependencies
- [ ] **Memory leaks** - Video elements not properly cleaned up
- [ ] **SQL injection risks** - Use parameterized queries everywhere
- [ ] **CORS issues** - FastAPI needs proper CORS middleware
- [ ] **Race conditions** - Celery tasks need proper locking
- [ ] **Large file crashes** - Check chunked upload implementation
- [ ] **M2 API timeout** - Need request timeouts configured

**Issues Found:** ___ (List them below)

---

---

## 🔄 If Quality Score < 80: Action Plan

1. **Identify missing components** from checklist
2. **Create focused prompts** for each gap:
   ```
   "The current ClipSmart build is missing [X]. Please generate
   a complete implementation of [X] that includes:
   - [Specific requirement 1]
   - [Specific requirement 2]
   - [Integration with existing code at /path/to/file.py]"
   ```
3. **Test incrementally** - Don't wait for everything to be perfect
4. **Iterate quickly** - You have until Nov 7th for free M2 trial

---

## 📞 Need Help? Contact Points

- **AetherPro Support:** https://aetherprotech.com/support
- **MiniMax-M2 Docs:** [Check their API documentation]
- **ClipSmart Issues:** [GitHub repo if created]
- **Me (Claude):** Just paste error logs and I'll help debug!

---

**Ready to validate? Paste MiniMax-M2's output and let's check quality! 🚀**
