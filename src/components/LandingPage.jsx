import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import './LandingPage.css'

function LandingPage() {
  const navigate = useNavigate()
  const [currentPage, setCurrentPage] = useState(1)
  const totalPages = 2

  const nextPage = () => {
    if (currentPage < totalPages) {
      setCurrentPage(currentPage + 1)
    }
  }

  const prevPage = () => {
    if (currentPage > 1) {
      setCurrentPage(currentPage - 1)
    }
  }

  return (
    <div className="landing-container">
      <div className="book-container">
        {/* Left Page */}
        <div className="book-page left-page">
          <div className="page-content">
            <h2>Welcome to Book Chatbot</h2>
            <p className="book-text">
              Turn the pages to explore our interactive chatbot experiences.
              Each page offers a unique conversation journey.
            </p>
            <div className="page-number">{currentPage}</div>
          </div>
        </div>

        {/* Right Page */}
        <div className="book-page right-page">
          <div className="page-content">
            <div className="chatbot-placeholder">
              <div className="chatbot-header">
                <h3>Chatbot {currentPage}</h3>
              </div>
              <div className="chatbot-area">
                <p>Chatbot interface will be placed here</p>
                <div className="chatbot-icon">💬</div>
              </div>
            </div>
            <div className="page-number">{currentPage + 1}</div>
          </div>
        </div>

        {/* Book Spine */}
        <div className="book-spine"></div>
      </div>

      {/* Navigation Controls */}
      <div className="book-navigation">
        <button 
          onClick={prevPage} 
          disabled={currentPage === 1}
          className="nav-button prev-button"
        >
          ← Previous Page
        </button>
        <span className="page-indicator">
          Page {currentPage} of {totalPages}
        </span>
        <button 
          onClick={nextPage} 
          disabled={currentPage === totalPages}
          className="nav-button next-button"
        >
          Next Page →
        </button>
      </div>

      {/* Navigation Button */}
      <div className="landing-auth">
        <button onClick={() => navigate('/dashboard')} className="auth-button">
          Go to Dashboard
        </button>
      </div>
    </div>
  )
}

export default LandingPage

