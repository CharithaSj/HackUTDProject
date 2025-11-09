@echo off
echo ========================================
echo HackUTD Project - Setup Script
echo ========================================
echo.

echo Checking Node.js installation...
node --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Node.js is not installed!
    echo Please install Node.js from https://nodejs.org/
    echo.
    pause
    exit /b 1
)

echo Node.js is installed!
echo.

echo Installing dependencies...
echo This may take a few minutes...
echo.
call npm install

if errorlevel 1 (
    echo.
    echo ERROR: Failed to install dependencies!
    echo Please check the error messages above.
    echo.
    pause
    exit /b 1
)

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Create a .env file with your Auth0 credentials
echo    (See ENV_SETUP.md for instructions)
echo 2. Run: npm run dev
echo 3. Open http://localhost:3000 in your browser
echo.
pause

