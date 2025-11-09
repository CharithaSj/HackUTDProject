# Auth0 Setup Guide - Step by Step

Follow these exact steps to set up Auth0 for your application.

## Step 1: Create Auth0 Account

1. Go to https://auth0.com/
2. Click **"Sign Up"** in the top right corner
3. Sign up with:
   - Email address
   - Password
   - Or use Google/GitHub login
4. Verify your email if prompted

## Step 2: Create a New Application

1. Once logged in, you'll see the **Auth0 Dashboard**
2. In the left sidebar, click **"Applications"**
3. Click the **"+ Create Application"** button (top right)
4. You'll see a popup:
   - **Name**: Enter `HackUTD Project` (or any name you prefer)
   - **Application Type**: Select **"Single Page Web Applications"**
   - Click **"Create"**

## Step 3: Configure Application Settings

1. You'll be taken to your application's settings page
2. Scroll down to find **"Application URIs"** section
3. Set the following URLs:

   **Allowed Callback URLs:**
   ```
   http://localhost:3000
   ```

   **Allowed Logout URLs:**
   ```
   http://localhost:3000
   ```

   **Allowed Web Origins:**
   ```
   http://localhost:3000
   ```

4. Scroll up and click **"Save Changes"** button

## Step 4: Copy Your Credentials

On the same settings page, you'll see:

1. **Domain**: 
   - Look for a field labeled **"Domain"**
   - It looks like: `dev-xxxxxx.us.auth0.com` or `your-app.auth0.com`
   - **Copy this value**

2. **Client ID**:
   - Look for a field labeled **"Client ID"**
   - It's a long alphanumeric string
   - **Copy this value**

## Step 5: Update Your .env File

1. Open the `.env` file in the `HackUTDProject` folder
2. Replace the placeholder values:

   ```env
   VITE_AUTH0_DOMAIN=paste-your-domain-here
   VITE_AUTH0_CLIENT_ID=paste-your-client-id-here
   VITE_API_BASE_URL=http://localhost:8000/api
   ```

3. **Important**: 
   - Remove any quotes around the values
   - Don't include `https://` in the domain
   - Save the file

## Step 6: Verify Your Setup

Your `.env` file should look like this (with your actual values):

```env
VITE_AUTH0_DOMAIN=dev-abc123.us.auth0.com
VITE_AUTH0_CLIENT_ID=abc123xyz789def456ghi012
VITE_API_BASE_URL=http://localhost:8000/api
```

## Step 7: Test the Application

1. Make sure your `.env` file is saved
2. Restart your development server:
   - Stop the server (Ctrl+C)
   - Run `npm run dev` again
3. Open http://localhost:3000
4. Click "Log In / Sign Up"
5. You should see the Auth0 login page!

## Troubleshooting

### Issue: "Invalid callback URL"
**Solution**: Make sure you added `http://localhost:3000` to Allowed Callback URLs in Auth0 settings

### Issue: "Application error" or blank page
**Solution**: 
- Check that your `.env` file has the correct values
- Make sure there are no extra spaces or quotes
- Restart the development server after changing `.env`

### Issue: Can't find Domain or Client ID
**Solution**: 
- They're on the main settings page of your application
- Domain is usually near the top
- Client ID is in the "Basic Information" section

### Issue: Auth0 page doesn't load
**Solution**:
- Check your internet connection
- Verify the domain in `.env` is correct
- Make sure you saved the Auth0 application settings

## Visual Guide

### Where to Find Settings in Auth0 Dashboard:

```
Auth0 Dashboard
├── Applications (left sidebar)
│   └── Your Application Name
│       ├── Settings (tab)
│       │   ├── Domain: [Copy this]
│       │   ├── Client ID: [Copy this]
│       │   └── Application URIs (scroll down)
│       │       ├── Allowed Callback URLs: http://localhost:3000
│       │       ├── Allowed Logout URLs: http://localhost:3000
│       │       └── Allowed Web Origins: http://localhost:3000
```

## Quick Checklist

- [ ] Created Auth0 account
- [ ] Created new Application (Single Page Web Application)
- [ ] Set Allowed Callback URLs to `http://localhost:3000`
- [ ] Set Allowed Logout URLs to `http://localhost:3000`
- [ ] Set Allowed Web Origins to `http://localhost:3000`
- [ ] Saved changes in Auth0
- [ ] Copied Domain from Auth0
- [ ] Copied Client ID from Auth0
- [ ] Updated `.env` file with credentials
- [ ] Restarted development server
- [ ] Tested login functionality

## Need Help?

If you're stuck:
1. Check the browser console (F12) for error messages
2. Verify your `.env` file format is correct
3. Make sure you saved all Auth0 settings
4. Try restarting the development server

