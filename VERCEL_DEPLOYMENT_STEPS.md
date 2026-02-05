# 🚀 TripSmart - Vercel Deployment Guide

## Prerequisites
- ✅ Your code is already on GitHub
- ✅ You have a Vercel account (if not, sign up at https://vercel.com)

---

## 🎯 Deployment Steps

### **Method 1: Deploy via Vercel Dashboard (Recommended - Easiest)**

#### Step 1: Sign in to Vercel
1. Go to **https://vercel.com**
2. Click **"Sign Up"** or **"Log In"**
3. Sign in with your **GitHub account** (recommended for easy integration)

#### Step 2: Import Your GitHub Repository
1. Once logged in, click **"Add New..."** button (top right)
2. Select **"Project"**
3. You'll see a list of your GitHub repositories
4. Find **"tripsmart"** (or whatever you named your repo)
5. Click **"Import"** next to it

#### Step 3: Configure Project Settings
Vercel will auto-detect most settings, but verify these:

- **Framework Preset**: Should auto-detect as "Other" (this is correct for Flask)
- **Root Directory**: `./` (leave as default)
- **Build Command**: Leave empty
- **Output Directory**: Leave empty
- **Install Command**: `pip install -r requirements.txt` (should auto-detect)

#### Step 4: Deploy!
1. Click the **"Deploy"** button
2. Wait for the build to complete (usually 1-2 minutes)
3. 🎉 You'll get a live URL like: `https://tripsmart-xxxxx.vercel.app`

---

### **Method 2: Deploy via Vercel CLI (Alternative)**

If you prefer using the command line:

#### Step 1: Install Vercel CLI
```bash
npm install -g vercel
```

#### Step 2: Login to Vercel
```bash
vercel login
```
Follow the prompts to authenticate.

#### Step 3: Deploy
```bash
cd c:\Users\omprakash\Videos\tripsmart\tripsmart
vercel
```

Follow the interactive prompts:
- **Set up and deploy?** → Yes
- **Which scope?** → Select your account
- **Link to existing project?** → No (first time)
- **Project name?** → tripsmart (or your preferred name)
- **Directory?** → `./`
- **Override settings?** → No

#### Step 4: Deploy to Production
```bash
vercel --prod
```

---

## 📋 Important Configuration Files (Already Set Up)

Your project already has these files configured:

### 1. `vercel.json`
```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```
✅ This tells Vercel to treat your Flask app as a Python serverless function.

### 2. `requirements.txt`
```
flask
pandas
scikit-learn
numpy
requests
```
✅ All dependencies are listed.

### 3. `.vercelignore`
```
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.DS_Store
*.log
```
✅ Excludes unnecessary files from deployment.

---

## 🔧 After Deployment

### Access Your App
After successful deployment, Vercel provides:
- **Production URL**: `https://your-project.vercel.app`
- **Deployment Dashboard**: Monitor logs, analytics, and performance

### Test Your Application
Visit your URL and test:
- Home page loads correctly
- Recommendation form works
- Results are displayed properly

---

## 🐛 Troubleshooting

### Issue: Build Fails
**Solution:**
1. Check the build logs in Vercel dashboard
2. Ensure all files are committed to GitHub
3. Verify `requirements.txt` has all dependencies

### Issue: "Module not found" Error
**Solution:**
1. Add the missing module to `requirements.txt`
2. Commit and push to GitHub
3. Vercel will auto-redeploy

### Issue: CSV File Not Found
**Solution:**
- Ensure the `data/` folder is committed to GitHub
- Check that `recommender.py` uses correct file paths
- Vercel includes all committed files in deployment

### Issue: Function Timeout (10 seconds limit)
**Solution:**
- Optimize your recommendation algorithm
- Consider caching results
- Upgrade to Vercel Pro for 60-second timeout

### Issue: Cold Start (First Request is Slow)
**Solution:**
- This is normal for serverless functions
- Subsequent requests will be faster
- Consider upgrading to keep functions warm

---

## 🔄 Updating Your Deployment

Vercel automatically redeploys when you push to GitHub:

1. Make changes to your code locally
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Update feature"
   git push
   ```
3. Vercel automatically detects the push and redeploys
4. Check the Vercel dashboard for deployment status

---

## 🌟 Pro Tips

### 1. **Custom Domain** (Optional)
- Go to Project Settings → Domains
- Add your custom domain (e.g., `tripsmart.com`)
- Follow DNS configuration instructions

### 2. **Environment Variables** (If Needed)
- Go to Project Settings → Environment Variables
- Add any API keys or secrets
- Redeploy for changes to take effect

### 3. **Preview Deployments**
- Every GitHub branch gets its own preview URL
- Great for testing before merging to main

### 4. **View Logs**
- Go to Deployments → Click on a deployment
- View real-time logs and function execution details

---

## 📊 Vercel Dashboard Features

After deployment, explore:
- **Analytics**: Track page views and performance
- **Logs**: Debug issues with real-time logs
- **Deployments**: View deployment history
- **Settings**: Configure domains, environment variables, etc.

---

## 🆘 Need Help?

- **Vercel Documentation**: https://vercel.com/docs
- **Vercel Support**: https://vercel.com/support
- **Community**: https://github.com/vercel/vercel/discussions

---

## ✅ Quick Checklist

Before deploying, ensure:
- [ ] Code is pushed to GitHub
- [ ] `vercel.json` exists in root directory
- [ ] `requirements.txt` has all dependencies
- [ ] `data/` folder with CSV is committed
- [ ] `app.py` is in the root directory

After deploying:
- [ ] Visit the production URL
- [ ] Test all features
- [ ] Check Vercel logs for any errors
- [ ] Share your live app! 🎉

---

## 🎉 You're Ready!

Your TripSmart app is configured and ready for Vercel deployment. Just follow the steps above, and you'll have a live URL in minutes!

**Good luck with your deployment! 🚀**
