// Quick script to check if Auth0 is configured
// Run with: node check-auth0-setup.js

import { readFileSync } from 'fs';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

try {
  const envPath = join(__dirname, '.env');
  const envContent = readFileSync(envPath, 'utf-8');
  
  const domain = envContent.match(/VITE_AUTH0_DOMAIN=(.+)/)?.[1];
  const clientId = envContent.match(/VITE_AUTH0_CLIENT_ID=(.+)/)?.[1];
  
  console.log('\n========================================');
  console.log('Auth0 Configuration Check');
  console.log('========================================\n');
  
  if (!domain || domain.includes('your-auth0-domain') || domain.trim() === '') {
    console.log('❌ VITE_AUTH0_DOMAIN is not configured');
    console.log('   Please set your Auth0 domain in .env file\n');
  } else {
    console.log('✅ VITE_AUTH0_DOMAIN:', domain);
  }
  
  if (!clientId || clientId.includes('your-auth0-client-id') || clientId.trim() === '') {
    console.log('❌ VITE_AUTH0_CLIENT_ID is not configured');
    console.log('   Please set your Auth0 client ID in .env file\n');
  } else {
    console.log('✅ VITE_AUTH0_CLIENT_ID:', clientId.substring(0, 20) + '...');
  }
  
  if (domain && !domain.includes('your-auth0-domain') && 
      clientId && !clientId.includes('your-auth0-client-id')) {
    console.log('\n✅ Auth0 is properly configured!');
    console.log('   You can now run: npm run dev\n');
  } else {
    console.log('\n⚠️  Please complete the Auth0 setup:');
    console.log('   1. Follow the instructions in AUTH0_SETUP_GUIDE.md');
    console.log('   2. Update your .env file with your Auth0 credentials\n');
  }
  
} catch (error) {
  if (error.code === 'ENOENT') {
    console.log('\n❌ .env file not found!');
    console.log('   Please create a .env file in the project root');
    console.log('   See AUTH0_SETUP_GUIDE.md for instructions\n');
  } else {
    console.log('\n❌ Error reading .env file:', error.message);
  }
}

