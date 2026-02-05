# TripSmart - Vercel Deployment Guide

## Prerequisites
1. A GitHub account
2. A Vercel account (sign up at https://vercel.com)
3. Git installed on your computer

## Step-by-Step Deployment Instructions

### Step 1: Initialize Git Repository (if not already done)
```bash
cd c:\Users\omprakash\Videos\tripsmart\tripsmart
git init
git add .
git commit -m "Initial commit - TripSmart travel recommendation app"
```

### Step 2: Create a GitHub Repository
1. Go to https://github.com/new
2. Create a new repository (e.g., "tripsmart")
3. **DO NOT** initialize with README, .gitignore, or license
4. Copy the repository URL

### Step 3: Push Your Code to GitHub
```bash
git remote add origin YOUR_GITHUB_REPO_URL
git branch -M main
git push -u origin main
```

### Step 4: Deploy to Vercel

#### Option A: Deploy via Vercel Dashboard (Recommended)
1. Go to https://vercel.com and sign in
2. Click "Add New Project"
3. Import your GitHub repository
4. Vercel will auto-detect the settings
5. Click "Deploy"

#### Option B: Deploy via Vercel CLI
```bash
# Install Vercel CLI globally
npm install -g vercel

# Login to Vercel
vercel login

# Deploy
vercel
```

### Step 5: Configure Project Settings (if needed)
- **Framework Preset**: Other
- **Build Command**: (leave empty)
- **Output Directory**: (leave empty)
- **Install Command**: `pip install -r requirements.txt`

## Files Created for Deployment

### 1. `vercel.json`
Configures Vercel to treat your Flask app as a serverless function.

### 2. `requirements.txt`
Lists all Python dependencies (fixed from requirement.txt).

### 3. `.vercelignore`
Excludes unnecessary files from deployment.

## Important Notes

### Serverless Limitations
- **Cold starts**: First request may be slower
- **Execution time**: Max 10 seconds per request (Hobby plan)
- **File system**: Read-only except for /tmp directory

### Data Files
Your CSV file (`data/india_travel_destinations.csv`) will be included in the deployment and accessible via the updated absolute path in `recommender.py`.

### Environment Variables
If you need to add any API keys or secrets:
1. Go to your Vercel project dashboard
2. Settings → Environment Variables
3. Add your variables

## Testing Your Deployment

After deployment, Vercel will provide you with a URL like:
```
https://your-project-name.vercel.app
```

Visit this URL to test your application!

## Troubleshooting

### Issue: Module not found
- Check that all dependencies are in `requirements.txt`
- Redeploy the project

### Issue: CSV file not found
- The path has been updated to use absolute paths
- Ensure the `data` folder is committed to Git

### Issue: Build fails
- Check Vercel build logs in the dashboard
- Ensure Python version compatibility (Vercel uses Python 3.9 by default)

### Issue: Function timeout
- Optimize your recommendation algorithm
- Consider caching results
- Upgrade to a paid Vercel plan for longer execution times

## Alternative: Deploy to Other Platforms

If you encounter issues with Vercel, consider these alternatives:

### 1. **Render** (Recommended for Flask)
- Better suited for traditional Flask apps
- Free tier available
- https://render.com

### 2. **Railway**
- Easy Flask deployment
- Free tier with limitations
- https://railway.app

### 3. **PythonAnywhere**
- Specifically designed for Python web apps
- Free tier available
- https://www.pythonanywhere.com

## Next Steps

1. ✅ Push your code to GitHub
2. ✅ Connect to Vercel
3. ✅ Deploy
4. 🎉 Share your live URL!

## Support

If you encounter any issues during deployment, check:
- Vercel deployment logs
- GitHub Actions (if configured)
- Browser console for frontend errors

Good luck with your deployment! 🚀
