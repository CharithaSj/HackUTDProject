# HackUTD Project - Book Chatbot Application

A beautiful web application featuring an interactive book-style interface with chatbot integration.

## Features

- **Book-Style Landing Page**: Beautiful open book interface with page navigation
- **Interactive Pages**: Two swipable pages with chatbot placeholders
- **Dashboard**: Centralized navigation to all features
- **Python Backend Compatible**: API structure ready for Python backend integration

## Tech Stack

- **Frontend**: React.js with Vite
- **Routing**: React Router DOM
- **Styling**: CSS3 with modern design

## Setup Instructions

### Prerequisites

- Node.js (v16 or higher)
- npm or yarn

### Installation

1. **Navigate to the project directory**:
   ```bash
   cd HackUTDProject
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Start the development server**:
   ```bash
   npm run dev
   ```

4. **Open your browser** and navigate to `http://localhost:3000`

## Project Structure

```
HackUTDProject/
├── src/
│   ├── components/
│   │   ├── LandingPage.jsx      # Book-style landing page
│   │   ├── Dashboard.jsx        # User dashboard
│   │   ├── BookPage.jsx         # Individual book pages
│   │   └── Loading.jsx          # Loading component
│   ├── utils/
│   │   └── api.js               # API utilities for Python backend
│   ├── App.jsx                  # Main app component with routing
│   ├── main.jsx                 # Entry point
│   └── index.css                # Global styles
├── package.json
├── vite.config.js
└── README.md
```

## Python Backend Integration

The application is designed to work with a Python backend. The API utilities in `src/utils/api.js` are set up to communicate with a Python backend running on `http://localhost:8000/api`.

### Expected API Endpoints

The frontend expects the following API endpoints:

1. **POST `/api/chatbot/{pageNumber}/message`**
   - Send a message to the chatbot
   - Body: `{ "message": "user message" }`
   - Returns: `{ "response": "chatbot response" }`

2. **GET `/api/chatbot/{pageNumber}/history`**
   - Get chat history for a page
   - Returns: `{ "history": [...] }`

3. **DELETE `/api/chatbot/{pageNumber}/history`**
   - Clear chat history for a page
   - Returns: `{ "success": true }`

### Example Python Backend Setup (Flask)

```python
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/chatbot/<int:page_number>/message', methods=['POST'])
def chatbot_message(page_number):
    data = request.get_json()
    message = data.get('message', '')
    # Process message with your chatbot logic
    response = f"Response to: {message}"
    return jsonify({'response': response})

@app.route('/api/chatbot/<int:page_number>/history', methods=['GET'])
def get_history(page_number):
    # Retrieve chat history
    return jsonify({'history': []})

@app.route('/api/chatbot/<int:page_number>/history', methods=['DELETE'])
def clear_history(page_number):
    # Clear chat history
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(port=8000, debug=True)
```

## Usage

1. **Landing Page**: Visit the home page (`http://localhost:3000`) to see the book interface. You can navigate between pages using the navigation buttons.

2. **Dashboard**: Click "Go to Dashboard" to access the dashboard where you can:
   - Access the landing page
   - Navigate to individual chatbot pages (Page 1 and Page 2)

3. **Book Pages**: Click on any chatbot page from the dashboard to view the full-page book interface with chatbot placeholders.

## Development

### Available Scripts

- `npm run dev`: Start development server
- `npm run build`: Build for production
- `npm run preview`: Preview production build

## Future Enhancements

- Integrate actual chatbot functionality
- Add authentication (Auth0 or other)
- Add more pages to the book
- Implement swipe gestures for mobile devices
- Add page animations and transitions
- Implement chat history persistence

## License

This project is part of HackUTD 2025.
