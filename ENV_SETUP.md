# Environment Variables Setup

Create a `.env` file in the root directory (`HackUTDProject/`) with the following variables:

```env
# Auth0 Configuration
VITE_AUTH0_DOMAIN=your-auth0-domain.auth0.com
VITE_AUTH0_CLIENT_ID=your-auth0-client-id

# API Configuration
VITE_API_BASE_URL=http://localhost:8000/api
```

## How to Get Auth0 Credentials

1. Go to [Auth0 Dashboard](https://manage.auth0.com/)
2. Create a new account or sign in
3. Create a new Application:
   - Click "Applications" → "Create Application"
   - Choose "Single Page Web Applications"
   - Name your application (e.g., "HackUTD Project")
4. Configure Application Settings:
   - Allowed Callback URLs: `http://localhost:3000`
   - Allowed Logout URLs: `http://localhost:3000`
   - Allowed Web Origins: `http://localhost:3000`
5. Copy your Domain and Client ID from the application settings
6. Paste them into your `.env` file

## Important Notes

- Never commit the `.env` file to version control
- The `.env` file is already included in `.gitignore`
- Replace the placeholder values with your actual Auth0 credentials

