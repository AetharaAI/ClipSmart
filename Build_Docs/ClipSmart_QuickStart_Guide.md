# 🚀 ClipSmart Build - Quick Start Guide

## How to Use This Prompt with MiniMax-M2 Agent (Before Nov 7th!)

---

## ⚡ Step 1: Prepare Your Environment

### Before You Hit M2's Agent Builder:

1. **Gather Your API Keys** (you'll need these in the output):
   ```bash
   MINIMAX_API_KEY=sk-xxx          # Get from MiniMax dashboard
   YOUTUBE_API_KEY=AIza-xxx         # Get from Google Cloud Console
   TAVILY_API_KEY=tvly-xxx          # Get from Tavily.com
   SUPABASE_URL=https://xxx.supabase.co
   SUPABASE_ANON_KEY=eyJh-xxx
   OPENROUTER_API_KEY=sk-xxx        # For AetherInterface integration
   ```

2. **Set Up Your Local Dev Environment**:
   ```bash
   # Install prerequisites
   - Node.js 18+ (https://nodejs.org)
   - Python 3.11+ (https://python.org)
   - Docker Desktop (https://docker.com/products/docker-desktop)
   - Git (https://git-scm.com)
   - FFmpeg (brew install ffmpeg or apt-get install ffmpeg)
   
   # Verify installations
   node --version    # Should be v18+
   python --version  # Should be 3.11+
   docker --version  # Should be 20+
   ffmpeg -version   # Should be 6.0+
   ```

3. **Create a GitHub Repo** (optional but recommended):
   ```bash
   # On GitHub, create new repo: aetherpro/clipsmart
   # Don't initialize with README (M2 will generate it)
   ```

---

## 📝 Step 2: Feed the Prompt to MiniMax-M2

### Option A: Direct Copy-Paste (Recommended)
1. Open MiniMax-M2 Agent Builder: https://hailuoai.com (or their agent platform)
2. Click "New Agent Project" or "Build Application"
3. **Paste the entire contents** of `ClipSmart_MiniMaxM2_BuildPrompt_REFINED.md`
4. **Important:** If there's a character limit:
   - Paste in sections (Architecture, then User Flow, then Output Deliverables)
   - OR use their file upload feature to upload the .md file

### Option B: Chunked Prompting (If Character Limit)
If M2 has a prompt length limit, use this sequence:

**Prompt 1: Project Setup**
```
You are building ClipSmart for AetherPro Technologies. 
Read the attached specification document and generate:
1. Complete folder structure
2. package.json and requirements.txt
3. docker-compose.yml with all services
4. .env.example with all required keys

[Paste Architecture & Tech Stack section only]
```

**Prompt 2: Frontend Implementation**
```
Continue ClipSmart build. Generate all frontend components:
- Next.js pages (upload, analyze, splice, library)
- React components (VideoPlayer, ClipGrid, SpliceEditor, ExportModal)
- Tailwind theme with AetherPro branding
- Zustand stores for state management

[Paste User Flow & Features section only]
```

**Prompt 3: Backend Implementation**
```
Continue ClipSmart build. Generate backend API:
- FastAPI endpoints (upload, analyze, splice, export, library)
- MiniMax-M2 integration service
- Video processing with FFmpeg + OpenCV
- Celery async tasks for heavy processing

[Paste MiniMax-M2 Integration Details section only]
```

**Prompt 4: Testing & Documentation**
```
Complete ClipSmart build with:
- Jest tests for frontend components
- Pytest tests for backend services
- Playwright E2E test
- Complete README.md with setup instructions
- Quality checklist validation

[Paste Testing & Quality Assurance section only]
```

---

## 📦 Step 3: Receive & Extract Output

M2 should provide output in one of these formats:

### Format 1: ZIP File
```bash
# Download the ZIP
# Extract locally
unzip clipsmart-build.zip
cd clipsmart
```

### Format 2: GitHub Repo Link
```bash
# Clone the repo
git clone https://github.com/minimax-agent/clipsmart-output.git
cd clipsmart-output
```

### Format 3: Inline Code Blocks
If M2 returns code in markdown blocks:
```bash
# Create project folder
mkdir clipsmart
cd clipsmart

# Copy each file manually from M2's response
# OR use this helper script:
```

**Helper Script (save as `extract_m2_output.py`):**
```python
import re
import os

# Paste M2's entire response as a string
m2_response = """
[PASTE M2'S FULL RESPONSE HERE]
"""

# Extract code blocks with filenames
pattern = r'```[\w]*\s*\n# File: (.+?)\n(.*?)```'
matches = re.findall(pattern, m2_response, re.DOTALL)

for filepath, content in matches:
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w') as f:
        f.write(content.strip())
    print(f"✅ Created {filepath}")

print(f"\n✅ Extracted {len(matches)} files!")
```

---

## 🔧 Step 4: Initial Setup (5 minutes)

### 1. Configure Environment Variables
```bash
# Copy example and fill in real values
cp .env.example .env

# Edit .env with your actual API keys
nano .env  # or use your preferred editor
```

**Required Variables:**
```bash
# MiniMax M2
MINIMAX_API_KEY=sk-your-actual-key-here

# YouTube (for video fetching)
YOUTUBE_API_KEY=AIza-your-actual-key-here

# Tavily (for trending video discovery)
TAVILY_API_KEY=tvly-your-actual-key-here

# Supabase (database, auth, storage)
SUPABASE_URL=https://yourproject.supabase.co
SUPABASE_ANON_KEY=eyJh-your-actual-key-here
SUPABASE_SERVICE_ROLE_KEY=eyJh-your-service-key-here

# Redis (for Celery task queue)
REDIS_URL=redis://localhost:6379

# App Config
NEXT_PUBLIC_API_URL=http://localhost:8000
FRONTEND_URL=http://localhost:3000

# AetherPro Ecosystem (stubs for future)
AETHER_OS_API_URL=https://api.aetherpro.com
AETHER_AGENT_FORGE_TOKEN=xxx
AETHER_GRID_WEBHOOK=https://grid.aetherpro.com/webhook
```

### 2. Install Dependencies
```bash
# Frontend dependencies
cd frontend
npm install
cd ..

# Backend dependencies
cd backend
pip install -r requirements.txt --break-system-packages
cd ..
```

### 3. Start Services with Docker
```bash
# From project root
docker-compose up -d

# Check if all services are running
docker-compose ps

# Should see:
# - clipsmart-postgres (PostgreSQL database)
# - clipsmart-redis (Redis for Celery)
# - clipsmart-backend (FastAPI server)
# - clipsmart-frontend (Next.js app)
```

### 4. Run Database Migrations
```bash
# If using Prisma (frontend)
cd frontend
npx prisma migrate deploy
npx prisma generate

# If using Alembic (backend)
cd backend
alembic upgrade head
```

---

## ✅ Step 5: Verify Everything Works

### Test 1: Frontend Access
```bash
# Open browser
http://localhost:3000

# You should see:
✅ ClipSmart landing page with AetherPro branding
✅ "Upload Video" button
✅ Dark mode with ethereal blue theme
```

### Test 2: Backend API
```bash
# Check API docs
http://localhost:8000/docs

# You should see:
✅ Swagger UI with all endpoints
✅ POST /api/upload
✅ POST /api/analyze
✅ POST /api/splice
✅ POST /api/export
✅ GET /api/library
```

### Test 3: MiniMax-M2 Integration
```bash
# Test M2 API connection
curl -X POST http://localhost:8000/api/test-m2 \
  -H "Content-Type: application/json" \
  -d '{"test": "connection"}'

# Expected response:
{"status": "ok", "m2_available": true}
```

### Test 4: Video Upload
```bash
# Upload a test video (use sample provided or your own)
# In browser: http://localhost:3000/upload
# 1. Click "Upload Video" or drag-and-drop
# 2. Upload should show progress bar
# 3. On completion, should redirect to /analyze

✅ If upload completes without errors: SUCCESS!
```

### Test 5: Full User Flow (E2E Test)
```bash
# Run automated E2E test
cd frontend
npx playwright test

# Or manually:
# 1. Upload video
# 2. Wait for analysis (should see clip grid)
# 3. Select 2 clips
# 4. Click "Create Splice" with Semantic mode
# 5. Preview split-screen video
# 6. Click "Export"
# 7. Download MP4 file

✅ If you can download a split-screen video: SUCCESS!
```

---

## 🐛 Step 6: Troubleshooting Common Issues

### Issue 1: Docker Containers Won't Start
```bash
# Check Docker logs
docker-compose logs

# Common fixes:
# - Port 3000 already in use: Change FRONTEND_PORT in .env
# - Port 8000 already in use: Change BACKEND_PORT in .env
# - Postgres connection failed: Check SUPABASE_URL is correct
```

### Issue 2: M2 API Returns 401 Unauthorized
```bash
# Verify API key
echo $MINIMAX_API_KEY  # Should print your key

# Test directly
curl -X POST https://api.minimax.chat/v1/analyze \
  -H "Authorization: Bearer $MINIMAX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"test": "auth"}'

# If still fails: Key may be invalid, regenerate in M2 dashboard
```

### Issue 3: Video Processing Hangs
```bash
# Check Celery worker logs
docker-compose logs clipsmart-celery

# Common fixes:
# - FFmpeg not found: Install FFmpeg in Docker container
# - Redis connection failed: Check REDIS_URL in .env
# - Out of memory: Increase Docker memory limit (8GB+ recommended)
```

### Issue 4: Frontend Build Errors
```bash
# Clear node_modules and reinstall
cd frontend
rm -rf node_modules package-lock.json
npm install

# If TypeScript errors:
npm run type-check  # See specific errors
# Fix type issues in reported files
```

### Issue 5: "Module not found" Errors (Backend)
```bash
# Rebuild backend container
cd backend
docker-compose build clipsmart-backend
docker-compose up -d clipsmart-backend

# Or install manually:
pip install [missing-module] --break-system-packages
```

---

## 📊 Step 7: Run Quality Checklist

Use the `ClipSmart_Quality_Checklist.md` file:

```bash
# Open checklist
cat /path/to/ClipSmart_Quality_Checklist.md

# Score each section (0-10, 0-12, 0-15, etc.)
# Total score out of 95

Target Score: 80+ for deployment readiness
```

**If Score < 80:** Identify missing components and create focused prompts for M2 to fill gaps.

---

## 🚀 Step 8: Deploy to Production (Optional)

### Deploy Frontend (Vercel)
```bash
# Install Vercel CLI
npm install -g vercel

# From frontend folder
cd frontend
vercel login
vercel --prod

# Set environment variables in Vercel dashboard:
# NEXT_PUBLIC_API_URL=https://your-backend.railway.app
# SUPABASE_URL=...
# SUPABASE_ANON_KEY=...
```

### Deploy Backend (Railway.app)
```bash
# Install Railway CLI
npm install -g @railway/cli

# From backend folder
cd backend
railway login
railway init  # Create new project
railway up    # Deploy

# Set environment variables in Railway dashboard:
# MINIMAX_API_KEY=...
# SUPABASE_URL=...
# etc.
```

---

## 🎯 Step 9: Test with Real Videos

### Recommended Test Videos (5-10 min each):
1. **Tech Tutorial:** https://youtube.com/watch?v=[tech-tutorial-id]
2. **DIY Hack:** https://youtube.com/watch?v=[diy-hack-id]
3. **Viral Reaction:** https://youtube.com/watch?v=[viral-reaction-id]

### Testing Checklist:
- [ ] Upload each video (or use YouTube URL)
- [ ] Verify analysis extracts 8-12 clips
- [ ] Check clip scores are diverse (0.6-0.9 range)
- [ ] Test all 3 splice modes:
  - [ ] Semantic Relevance (should pair related clips)
  - [ ] Eclectic Contrast (should pair contrasting clips)
  - [ ] Trending Fusion (should fetch viral content)
- [ ] Verify audio mixing works (top/bottom volume sliders)
- [ ] Export at 720x1280 and 1080x1920
- [ ] Check file size is reasonable (<10MB per 30s)
- [ ] Upload to TikTok/YouTube Shorts manually (verify format works)

---

## 📈 Step 10: Iterate & Improve

### After Initial Testing, Consider:

1. **Fine-tune M2 Prompts:**
   - Adjust attention scoring weights if clips aren't viral enough
   - Refine semantic similarity threshold (0.65-0.85 range)

2. **Add Features M2 Might Have Missed:**
   - Auto-generated text overlays with M2 language model
   - AI voiceover narration for hooks
   - Background music suggestions from royalty-free library

3. **Optimize Performance:**
   - Profile slow endpoints (use FastAPI's `/metrics`)
   - Add Redis caching for repeated video analyses
   - Implement lazy loading for clip grid

4. **Integrate with Aether Ecosystem:**
   - Connect to AetherAgentForge marketplace
   - Add model selector for 359 models from AetherInterface
   - Enable N8N workflow triggers

---

## 🎓 Advanced: Custom M2 Training (Future)

Once ClipSmart is stable, consider fine-tuning M2 on viral clips:

```python
# Collect training data
training_data = []
for clip in viral_clips_dataset:
    training_data.append({
        "frames": clip.frames,
        "audio": clip.audio_transcript,
        "label": clip.virality_score  # 0-1 scale
    })

# Fine-tune M2 (pseudocode - check M2 docs)
m2_finetuned = finetune_minimax_m2(
    training_data=training_data,
    epochs=10,
    learning_rate=1e-4
)

# Deploy fine-tuned model
MINIMAX_API_KEY_FINETUNED=sk-your-finetuned-model
```

---

## 🆘 Need Help?

### Resources:
- **MiniMax-M2 Docs:** https://docs.minimax.chat (check their agent builder guide)
- **ClipSmart Issues:** Paste error logs back to me (Claude) for debugging
- **AetherPro Support:** https://aetherprotech.com/support
- **Community:** Join AetherPro Discord (if exists)

### When to Ask for Help:
- ❌ M2 output is incomplete (<60 quality score)
- ❌ Critical errors prevent app from starting
- ❌ M2 API integration not working after troubleshooting
- ❌ Docker containers repeatedly crash

### How to Ask for Help Effectively:
```markdown
**Problem:** [Brief description]

**Expected:** [What should happen]

**Actual:** [What actually happens]

**Error Log:**
```
[Paste full error log here]
```

**Environment:**
- OS: [macOS/Windows/Linux]
- Docker Version: [x.x.x]
- Node Version: [x.x.x]
- Python Version: [x.x.x]

**Steps to Reproduce:**
1. [Step 1]
2. [Step 2]
3. [Error occurs]
```

---

## 🎉 Success Criteria

You'll know ClipSmart is ready when:

✅ You can upload a 5-minute video
✅ M2 extracts 8-12 high-quality clips (score >0.75)
✅ Splice editor generates 3+ relevant pairs
✅ Export produces a TikTok-ready 9:16 video
✅ File downloads without corruption
✅ Video plays correctly on mobile devices

**At that point: You have a production-ready ClipSmart! 🚀**

---

## ⏰ Timeline Reminder

- **Today (Nov 6th):** Feed prompt to M2, get output, run initial setup
- **Tonight:** Test full user flow, identify gaps, iterate with M2
- **Nov 7th (Before trial ends):** Final bug fixes, deploy to staging
- **Post-Nov 7th:** Continue development with free M2 tier or paid plan

**Don't wait - start now! The free pro trial ends tomorrow! 🔥**

---

**Ready? Copy the refined prompt and paste it into MiniMax-M2 Agent Builder NOW! ⚡**
