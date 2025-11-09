# Quick Start Guide - Running Locally

Follow these steps to run the application on your laptop.

## Step 1: Install Node.js (if not already installed)

1. Check if Node.js is installed:
   ```bash
   node --version
   npm --version
   ```

2. If not installed, download and install from [nodejs.org](https://nodejs.org/)
   - Download the LTS version (v18 or higher recommended)
   - Run the installer and follow the instructions
   - Restart your terminal/command prompt after installation

## Step 2: Navigate to Project Directory

Open your terminal/command prompt and navigate to the project folder:

```bash
cd HackUTDProject
```

## Step 3: Install Dependencies

Install all required packages:

```bash
npm install
```

This will install:
- React and React DOM
- React Router
- Vite (build tool)
- Other dependencies

**Note**: This may take a few minutes on first run.

## Step 4: Start the Development Server

Run the following command:

```bash
npm run dev
```

You should see output like:
```
  VITE v5.0.8  ready in 500 ms

  ➜  Local:   http://localhost:3000/
  ➜  Network: use --host to expose
```

## Step 5: Open in Browser

Open your web browser and navigate to:
```
http://localhost:3000
```

You should see the book-style landing page!

## That's It! 🎉

The application is now running. You can:
- Navigate between book pages on the landing page
- Click "Go to Dashboard" to access the dashboard
- Click on chatbot pages to view individual pages

## Troubleshooting

### Issue: "npm: command not found"
**Solution**: Node.js is not installed. Install it from [nodejs.org](https://nodejs.org/)

### Issue: "Port 3000 is already in use"
**Solution**: Either:
- Close the application using port 3000
- Or change the port in `vite.config.js`:
  ```js
  server: {
    port: 3001, // Change to a different port
  }
  ```

### Issue: "Module not found" errors
**Solution**: 
- Delete `node_modules` folder and `package-lock.json`
- Run `npm install` again

### Issue: Blank page or errors
**Solution**:
- Check browser console (F12) for errors
- Make sure all dependencies are installed
- Verify you're running `npm run dev` from the correct directory

## Useful Commands

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `Ctrl + C` - Stop the development server

## Need Help?

- Check the `README.md` for more detailed information
- Check browser console (F12) for error messages
