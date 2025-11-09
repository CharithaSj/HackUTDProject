import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { motion, AnimatePresence } from 'framer-motion'
import GoalGarden from './GoalGarden'
import ChatbotGuide from './ChatbotGuide'
import Bookshelf from './Bookshelf'
import DashboardDropdown from './DashboardDropdown'
import './LandingPage.css'

function LandingPage() {
  const navigate = useNavigate()
  const [currentPage, setCurrentPage] = useState(1)
  const [isFlipping, setIsFlipping] = useState(false)
  const [growth, setGrowth] = useState(15)
  const [messageCount, setMessageCount] = useState(0)
  const [inputValue, setInputValue] = useState('')
  const totalPages = 2

  const nextPage = () => {
    if (currentPage < totalPages && !isFlipping) {
      setIsFlipping(true)
      setTimeout(() => {
        setCurrentPage(currentPage + 1)
        setIsFlipping(false)
      }, 800)
    }
  }

  const prevPage = () => {
    if (currentPage > 1 && !isFlipping) {
      setIsFlipping(true)
      setTimeout(() => {
        setCurrentPage(currentPage - 1)
        setIsFlipping(false)
      }, 800)
    }
  }

  const handleSendMessage = () => {
    if (!inputValue.trim()) return
    // Increase growth when message is sent
    setMessageCount(prev => prev + 1)
    setGrowth(prev => Math.min(prev + 5, 100))
    setInputValue('') // Clear input after sending
  }

  return (
    <div className="landing-container">
      <DashboardDropdown />
      <Bookshelf />
      <div className="vintage-background"></div>
      
      <div className="main-content-wrapper">
        {/* Goal Garden - Left of book */}
        <div className="garden-container-left">
          <GoalGarden growth={growth} pageNumber={currentPage} />
        </div>

        <div className="book-wrapper">
          <div className="book-container">
            {/* Book Cover/Spine with vintage look */}
            <div className="book-spine-vintage"></div>
            
            {/* Left Page - Guide (static, doesn't flip) */}
            <div className="book-page left-page vintage-page">
              <div className="page-content">
                <div className="page-decorative-top"></div>
                <ChatbotGuide pageNumber={currentPage} />
                <div className="page-number-vintage">{currentPage}</div>
              </div>
            </div>

          {/* Right Page - Chatbot (flips like a book) */}
          <div className="right-page-wrapper">
            <AnimatePresence mode="wait">
              <motion.div
                key={currentPage}
                className="book-page right-page vintage-page"
                initial={{ 
                  rotateY: 0,
                  transformOrigin: 'left center',
                  zIndex: 1
                }}
                animate={{ 
                  rotateY: 0,
                  transformOrigin: 'left center',
                  zIndex: 1
                }}
                exit={{ 
                  rotateY: -180,
                  transformOrigin: 'left center',
                  zIndex: 2,
                  transition: { 
                    duration: 0.8, 
                    ease: [0.4, 0.0, 0.2, 1],
                  }
                }}
                transition={{ 
                  duration: 0.8, 
                  ease: [0.4, 0.0, 0.2, 1],
                }}
                style={{ 
                  transformStyle: 'preserve-3d',
                  backfaceVisibility: 'hidden'
                }}
              >
                <div className="page-content">
                  <div className="page-decorative-top"></div>
                  
                  <div className="right-page-content">
                    {/* Chatbot Area - Full width */}
                    <div className="chatbot-area-vintage">
                      <div className="chatbot-header-vintage">
                        <h3>Chatbot {currentPage}</h3>
                        <div className="chatbot-status">● Active</div>
                      </div>
                      <div className="chatbot-interface">
                        <div className="chatbot-message-area">
                          <div className="message-bubble bot-message">
                            <p>Hello! I'm here to help you grow your goals. What would you like to achieve today?</p>
                          </div>
                        </div>
                        <div className="chatbot-input-area">
                          <input 
                            type="text" 
                            placeholder="Type your message here..."
                            className="chatbot-input"
                            value={inputValue}
                            onChange={(e) => setInputValue(e.target.value)}
                            onKeyPress={(e) => {
                              if (e.key === 'Enter' && inputValue.trim()) {
                                handleSendMessage()
                              }
                            }}
                          />
                          <button 
                            className={`send-button ${!inputValue.trim() ? 'disabled' : ''}`} 
                            onClick={handleSendMessage}
                            disabled={!inputValue.trim()}
                          >
                            Send
                          </button>
                        </div>
                      </div>
                    </div>
                  </div>
                  
                  <div className="page-number-vintage">{currentPage + 1}</div>
                </div>
              </motion.div>
            </AnimatePresence>
          </div>

            {/* Vintage book shadows and effects */}
            <div className="book-shadow"></div>
            <div className="book-highlight"></div>
          </div>
        </div>
      </div>

      {/* Navigation Controls */}
      <div className="book-navigation">
        <button 
          onClick={prevPage} 
          disabled={currentPage === 1 || isFlipping}
          className="nav-button-vintage prev-button"
        >
          <span className="button-icon">←</span>
          <span>Previous Page</span>
        </button>
        <div className="page-indicator-vintage">
          <span className="page-current">{currentPage}</span>
          <span className="page-separator">/</span>
          <span className="page-total">{totalPages}</span>
        </div>
        <button 
          onClick={nextPage} 
          disabled={currentPage === totalPages || isFlipping}
          className="nav-button-vintage next-button"
        >
          <span>Next Page</span>
          <span className="button-icon">→</span>
        </button>
      </div>

    </div>
  )
}

export default LandingPage
