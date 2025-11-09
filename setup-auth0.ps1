# PowerShell script to help set up Auth0 configuration
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Auth0 Setup Helper" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if .env file exists
if (Test-Path ".env") {
    Write-Host "✓ .env file already exists" -ForegroundColor Green
    $overwrite = Read-Host "Do you want to overwrite it? (y/n)"
    if ($overwrite -ne "y") {
        Write-Host "Setup cancelled." -ForegroundColor Yellow
        exit
    }
}

Write-Host ""
Write-Host "Please provide your Auth0 credentials:" -ForegroundColor Yellow
Write-Host "(You can find these in your Auth0 Dashboard -> Applications -> Your App -> Settings)" -ForegroundColor Gray
Write-Host ""

# Get Auth0 Domain
$domain = Read-Host "Enter your Auth0 Domain (e.g., dev-xxxxxx.us.auth0.com)"

# Get Auth0 Client ID
$clientId = Read-Host "Enter your Auth0 Client ID"

# Get API Base URL (optional, has default)
$apiUrl = Read-Host "Enter API Base URL (press Enter for default: http://localhost:8000/api)"
if ([string]::IsNullOrWhiteSpace($apiUrl)) {
    $apiUrl = "http://localhost:8000/api"
}

# Create .env file content
$envContent = @"
# Auth0 Configuration
VITE_AUTH0_DOMAIN=$domain
VITE_AUTH0_CLIENT_ID=$clientId
VITE_API_BASE_URL=$apiUrl
"@

# Write to .env file
try {
    $envContent | Out-File -FilePath ".env" -Encoding utf8 -NoNewline
    Write-Host ""
    Write-Host "✓ .env file created successfully!" -ForegroundColor Green
    Write-Host ""
    Write-Host "Next steps:" -ForegroundColor Cyan
    Write-Host "1. Make sure your Auth0 application has these URLs configured:" -ForegroundColor White
    Write-Host "   - Allowed Callback URLs: http://localhost:3000" -ForegroundColor Gray
    Write-Host "   - Allowed Logout URLs: http://localhost:3000" -ForegroundColor Gray
    Write-Host "   - Allowed Web Origins: http://localhost:3000" -ForegroundColor Gray
    Write-Host ""
    Write-Host "2. Run: npm run dev" -ForegroundColor White
    Write-Host ""
    Write-Host "3. Open http://localhost:3000 in your browser" -ForegroundColor White
    Write-Host ""
} catch {
    Write-Host "✗ Error creating .env file: $_" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please manually create .env file with:" -ForegroundColor Yellow
    Write-Host $envContent -ForegroundColor Gray
}

