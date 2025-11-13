# ClipSmart Deployment Guide

This guide covers deployment of ClipSmart to production environments using Vercel (frontend) and Railway.app/Render (backend).

## 🚀 Pre-Deployment Checklist

### Environment Variables
Ensure all required environment variables are configured:

#### Required for Backend
```bash
# Core Application
ENVIRONMENT=production
SECRET_KEY=your-super-secret-jwt-key-min-32-chars
DEBUG=false

# Database
DATABASE_URL=postgresql+asyncpg://user:password@host:port/database

# Redis
REDIS_URL=redis://host:port/db

# MiniMax-M2 API
MINIMAX_API_KEY=sk-your-minimax-api-key
MINIMAX_API_BASE_URL=https://api.minimax.chat/v1

# Supabase
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_SERVICE_ROLE_KEY=your-supabase-service-role-key
SUPABASE_ANON_KEY=your-supabase-anon-key

# External APIs
YOUTUBE_API_KEY=your-youtube-data-api-v3-key
TAVILY_API_KEY=your-tavily-search-api-key

# File Storage
UPLOAD_DIR=/app/uploads
EXPORT_DIR=/app/exports

# Rate Limiting
RATE_LIMIT_PER_MINUTE=60
RATE_LIMIT_PER_HOUR=1000
```

#### Required for Frontend
```bash
NEXT_PUBLIC_API_URL=https://your-backend-domain.com
NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-supabase-anon-key
NEXT_PUBLIC_APP_URL=https://clipsmart.aetherpro.com
```

### Database Setup
1. Create PostgreSQL database
2. Run migrations (handled automatically on startup)
3. Set up pgvector extension for embeddings:
   ```sql
   CREATE EXTENSION IF NOT EXISTS vector;
   ```

### Redis Setup
1. Create Redis instance
2. Configure persistent storage
3. Set appropriate memory limits

## 🌐 Frontend Deployment (Vercel)

### 1. Prepare Repository
```bash
# Ensure your repository is ready
git add .
git commit -m "Deploy ClipSmart frontend"
git push origin main
```

### 2. Deploy to Vercel
```bash
# Install Vercel CLI
npm i -g vercel

# Login to Vercel
vercel login

# Deploy
vercel --prod
```

### 3. Configure Environment Variables
In Vercel Dashboard:
1. Go to Project Settings → Environment Variables
2. Add all `NEXT_PUBLIC_*` variables
3. Ensure `NEXT_PUBLIC_API_URL` points to your backend

### 4. Configure Domain
```bash
# Add custom domain in Vercel Dashboard
# Domain: clipsmart.aetherpro.com
# SSL: Automatically managed
```

### 5. Configure Build Settings
```json
{
  "buildCommand": "npm run build",
  "outputDirectory": ".next",
  "installCommand": "npm install",
  "devCommand": "npm run dev"
}
```

## 🚂 Backend Deployment (Railway.app)

### 1. Prepare Repository
```bash
# Ensure Dockerfile exists and is optimized
# Create railway.json if needed
```

### 2. Deploy to Railway
```bash
# Install Railway CLI
npm install -g @railway/cli

# Login and deploy
railway login
railway link
railway up
```

### 3. Configure Environment
```bash
# Set environment variables
railway variables set ENVIRONMENT=production
railway variables set DATABASE_URL=your-database-url
railway variables set REDIS_URL=your-redis-url
railway variables set MINIMAX_API_KEY=your-key
# ... add all other variables
```

### 4. Configure Database
```bash
# Add PostgreSQL plugin
railway add postgresql

# Add Redis plugin
railway add redis

# Get connection strings
railway variables
```

### 5. Configure Domain
```bash
# In Railway Dashboard:
# Settings → Domains → Add Domain
# Backend URL: api.clipsmart.aetherpro.com
```

## 🔧 Alternative Backend Deployment (Render.com)

### 1. Create Web Service
1. Connect GitHub repository
2. Select backend folder
3. Configure build command: `pip install -r requirements.txt`
4. Configure start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

### 2. Environment Variables
Add all production environment variables in Render Dashboard.

### 3. Database
Create PostgreSQL database and get connection string.

### 4. Redis
Create Redis instance or use managed service.

## 🗄️ Database Migrations

### Initial Setup
```bash
# Run migrations (handled automatically)
# Database tables created on first startup
```

### Vector Extension
```sql
-- Enable pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;

-- Index for similarity search
CREATE INDEX IF NOT EXISTS clips_embedding_idx ON clips 
USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);
```

## 🔐 SSL/TLS Configuration

### Frontend (Vercel)
- SSL automatically provided by Vercel
- Let's Encrypt certificates
- Automatic renewal

### Backend (Railway/Render)
- SSL automatically provided
- HTTPS enforced
- HSTS headers configured

## 📊 Monitoring Setup

### 1. Error Tracking (Sentry)
```bash
# Backend
SENTRY_DSN=https://your-sentry-dsn@sentry.io/project-id

# Frontend
NEXT_PUBLIC_SENTRY_DSN=https://your-sentry-dsn@sentry.io/project-id
```

### 2. Performance Monitoring
```bash
# Enable metrics in production
ENABLE_METRICS=true

# Configure custom metrics endpoint
METRICS_ENDPOINT=/metrics
```

### 3. Health Checks
```bash
# Configure health check endpoints
# Frontend: /api/health
# Backend: /health
```

## 📝 DNS Configuration

### Domain Setup
```
# DNS Records
clipsmart.aetherpro.com     → A record → Vercel IP
api.clipsmart.aetherpro.com → CNAME → Railway/Render domain
www.clipsmart.aetherpro.com → CNAME → clipsmart.aetherpro.com
```

### Subdomain Configuration
- `clipsmart.aetherpro.com` → Frontend (Vercel)
- `api.clipsmart.aetherpro.com` → Backend (Railway/Render)
- `docs.clipsmart.aetherpro.com` → API Documentation

## 🔄 CI/CD Pipeline

### GitHub Actions
```yaml
# .github/workflows/deploy.yml
name: Deploy ClipSmart

on:
  push:
    branches: [main]

jobs:
  deploy-frontend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Deploy Frontend
        run: vercel --prod --token ${{ secrets.VERCEL_TOKEN }}

  deploy-backend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Deploy Backend
        run: railway up --token ${{ secrets.RAILWAY_TOKEN }}
```

## 📊 Production Scaling

### Frontend (Vercel)
- Automatic scaling based on traffic
- Edge network for global CDN
- Serverless functions for API routes

### Backend (Railway/Render)
- Horizontal scaling with multiple instances
- Auto-scaling based on CPU/memory
- Load balancing for high availability

### Database
- Connection pooling enabled
- Read replicas for scaling
- Automatic backups configured

## 🔍 Health Checks

### Frontend Health Check
```javascript
// pages/api/health.js
export default function handler(req, res) {
  res.status(200).json({
    status: 'healthy',
    timestamp: new Date().toISOString(),
    service: 'clipsmart-frontend'
  });
}
```

### Backend Health Check
```python
# Already implemented in main.py
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "clipsmart-api",
        "version": "2.0.0"
    }
```

## 🚨 Troubleshooting

### Common Issues

#### CORS Errors
- Check `ALLOWED_HOSTS` includes your domain
- Verify frontend `NEXT_PUBLIC_API_URL` is correct

#### Database Connection
- Verify `DATABASE_URL` format
- Check network connectivity
- Ensure database is accessible

#### API Rate Limits
- Monitor MiniMax API usage
- Implement proper error handling
- Consider upgrading API tier

#### File Upload Issues
- Check `MAX_FILE_SIZE_MB` setting
- Verify storage permissions
- Monitor disk space

### Monitoring Commands
```bash
# Check application logs
railway logs
vercel logs

# Monitor database
railway pg connect

# Check Redis
railway redis connect

# View metrics
curl https://api.clipsmart.aetherpro.com/metrics
```

## 🔄 Rollback Strategy

### Frontend Rollback
```bash
# Rollback to previous deployment
vercel rollback

# Rollback specific deployment
vercel rollback [deployment-url]
```

### Backend Rollback
```bash
# Railway rollback
railway rollback [deployment-id]

# Render rollback
# Use dashboard or redeploy previous commit
```

### Database Rollback
```bash
# If using migrations
alembic downgrade [revision]
```

## 📈 Performance Optimization

### Frontend Optimizations
- Image optimization enabled
- Code splitting configured
- CDN caching headers set
- Compression enabled

### Backend Optimizations
- Async/await throughout
- Connection pooling enabled
- Redis caching configured
- API response compression

### Database Optimizations
- Proper indexing strategy
- Connection pooling configured
- Query optimization
- Materialized views for analytics

## 🔒 Security Hardening

### Environment Security
- API keys stored in environment variables
- No hardcoded secrets
- Regular key rotation
- Secure cookie settings

### Application Security
- CORS properly configured
- Rate limiting enabled
- Input validation implemented
- SQL injection prevention

### Infrastructure Security
- HTTPS enforced
- Security headers configured
- Regular security updates
- Access logging enabled

## 📞 Support

For deployment issues:
- Check documentation: [docs.aetherpro.com](https://docs.aetherpro.com)
- Contact support: support@clipsmart.com
- Community Discord: [Join here](https://discord.gg/clipsmart)
- GitHub Issues: [Report here](https://github.com/aetherpro/clipsmart/issues)