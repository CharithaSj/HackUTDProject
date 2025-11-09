// API utility functions for Python backend compatibility
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api'

/**
 * Generic API request function
 * @param {string} endpoint - API endpoint
 * @param {object} options - Fetch options
 * @returns {Promise} - Response data
 */
export async function apiRequest(endpoint, options = {}) {
  const url = `${API_BASE_URL}${endpoint}`
  const defaultOptions = {
    headers: {
      'Content-Type': 'application/json',
    },
  }

  // Add authentication token if available
  const token = localStorage.getItem('auth_token')
  if (token) {
    defaultOptions.headers.Authorization = `Bearer ${token}`
  }

  const config = {
    ...defaultOptions,
    ...options,
    headers: {
      ...defaultOptions.headers,
      ...options.headers,
    },
  }

  try {
    const response = await fetch(url, config)
    
    if (!response.ok) {
      throw new Error(`API request failed: ${response.statusText}`)
    }

    const data = await response.json()
    return data
  } catch (error) {
    console.error('API request error:', error)
    throw error
  }
}

/**
 * Get chatbot response
 * @param {number} pageNumber - Page number (1 or 2)
 * @param {string} message - User message
 * @returns {Promise} - Chatbot response
 */
export async function sendChatbotMessage(pageNumber, message) {
  return apiRequest(`/chatbot/${pageNumber}/message`, {
    method: 'POST',
    body: JSON.stringify({ message }),
  })
}

/**
 * Get user chat history
 * @param {number} pageNumber - Page number (1 or 2)
 * @returns {Promise} - Chat history
 */
export async function getChatHistory(pageNumber) {
  return apiRequest(`/chatbot/${pageNumber}/history`)
}

/**
 * Clear chat history
 * @param {number} pageNumber - Page number (1 or 2)
 * @returns {Promise} - Success response
 */
export async function clearChatHistory(pageNumber) {
  return apiRequest(`/chatbot/${pageNumber}/history`, {
    method: 'DELETE',
  })
}

