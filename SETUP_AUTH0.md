# 🚀 Quick Auth0 Setup - 5 Minutes

I've prepared everything for you! Just follow these simple steps:

## ⚡ Quick Steps

### 1. Create the .env file
Copy the template file:
```bash
copy .env.template .env
```
(Or manually create `.env` file with the content from `.env.template`)

### 2. Sign up for Auth0 (Free)
- Go to: https://auth0.com/signup
- Sign up with email or use Google/GitHub
- Verify your email if needed

### 3. Create Application in Auth0
1. After logging in, click **"Applications"** in left sidebar
2. Click **"+ Create Application"** button
3. Enter name: `HackUTD Project`
4. Select: **"Single Page Web Applications"**
5. Click **"Create"**

### 4. Configure URLs (IMPORTANT!)
Scroll down to **"Application URIs"** and add:

- **Allowed Callback URLs**: `http://localhost:3000`
- **Allowed Logout URLs**: `http://localhost:3000`  
- **Allowed Web Origins**: `http://localhost:3000`

Click **"Save Changes"**!

### 5. Copy Your Credentials
On the same page, find and copy:
- **Domain** (looks like: `dev-xxxxxx.us.auth0.com`)
- **Client ID** (long alphanumeric string)

### 6. Update .env File
Open `.env` file and replace:
```env
VITE_AUTH0_DOMAIN=paste-your-domain-here
VITE_AUTH0_CLIENT_ID=paste-your-client-id-here
```

### 7. Verify Setup
Run this command to check:
```bash
npm run check-auth0
```

### 8. Start the App!
```bash
npm run dev
```

## 📋 Checklist

- [ ] Created `.env` file from `.env.template`
- [ ] Signed up for Auth0 account
- [ ] Created new Application (Single Page Web Application)
- [ ] Added `http://localhost:3000` to all three URL fields
- [ ] Saved changes in Auth0
- [ ] Copied Domain and Client ID
- [ ] Updated `.env` file
- [ ] Ran `npm run check-auth0` to verify
- [ ] Started app with `npm run dev`

## 🆘 Need Help?

- See `AUTH0_SETUP_GUIDE.md` for detailed instructions with screenshots descriptions
- Run `npm run check-auth0` to verify your configuration
- Check browser console (F12) for error messages

## ⚠️ Common Mistakes

1. **Forgetting to save changes** in Auth0 dashboard
2. **Adding quotes** around values in .env file (don't!)
3. **Including https://** in the domain (don't!)
4. **Not restarting** the dev server after changing .env

---

**That's it!** Once you complete these steps, your app will have working authentication! 🎉

