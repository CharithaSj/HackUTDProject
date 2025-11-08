# 🔐 Auth0 Setup - Simple Guide

I can't create the Auth0 account for you (that requires your email), but I've made it super easy! Here's what I've set up:

## ✅ What I've Done For You

1. ✅ Created `.env.template` file with the correct structure
2. ✅ Created detailed setup guides
3. ✅ Created a setup checker script
4. ✅ Created a PowerShell helper script (for Windows)

## 🚀 Easiest Way to Set Up (Choose One)

### Option 1: Use the PowerShell Script (Windows - Easiest!)

1. Open PowerShell in the `HackUTDProject` folder
2. Run:
   ```powershell
   .\setup-auth0.ps1
   ```
3. Follow the prompts - it will ask for your Auth0 credentials
4. Done!

### Option 2: Manual Setup

1. **Create `.env` file**:
   - Copy `.env.template` to `.env`
   - Or create a new file named `.env`

2. **Get Auth0 Credentials** (5 minutes):
   - Go to https://auth0.com/signup (free account)
   - Create Application → Single Page Web Application
   - Configure URLs (see SETUP_AUTH0.md)
   - Copy Domain and Client ID

3. **Update `.env` file**:
   ```env
   VITE_AUTH0_DOMAIN=your-domain-here
   VITE_AUTH0_CLIENT_ID=your-client-id-here
   VITE_API_BASE_URL=http://localhost:8000/api
   ```

4. **Verify**:
   ```bash
   npm run check-auth0
   ```

## 📚 Detailed Guides

- **`SETUP_AUTH0.md`** - Quick 5-minute setup guide
- **`AUTH0_SETUP_GUIDE.md`** - Detailed step-by-step instructions

## 🎯 What You Need to Do

Since I can't create accounts for you, you need to:

1. **Sign up for Auth0** (2 minutes)
   - Go to https://auth0.com/signup
   - Use your email or Google/GitHub

2. **Create an Application** (1 minute)
   - Click "Applications" → "Create Application"
   - Choose "Single Page Web Applications"

3. **Configure URLs** (1 minute)
   - Add `http://localhost:3000` to:
     - Allowed Callback URLs
     - Allowed Logout URLs
     - Allowed Web Origins

4. **Copy Credentials** (1 minute)
   - Copy Domain and Client ID
   - Paste into `.env` file

**Total time: ~5 minutes!**

## ✅ Quick Checklist

- [ ] Created `.env` file (use `.env.template` as reference)
- [ ] Signed up for Auth0
- [ ] Created Application (Single Page Web Application)
- [ ] Configured URLs in Auth0
- [ ] Copied Domain and Client ID
- [ ] Updated `.env` file
- [ ] Ran `npm run check-auth0` to verify

## 🆘 Need Help?

Run the setup checker:
```bash
npm run check-auth0
```

This will tell you exactly what's missing!

---

**Note**: The `.env` file is in `.gitignore` so it won't be committed to git (which is good for security!).

