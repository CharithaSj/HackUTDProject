import { useState } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { motion, AnimatePresence } from 'framer-motion'
import GoalGarden from './GoalGarden'
import ChatbotGuide from './ChatbotGuide'
import Bookshelf from './Bookshelf'
import DashboardDropdown from './DashboardDropdown'
import './BookPage.css'

function BookPage() {
  const { pageNumber } = useParams()
  const navigate = useNavigate()
  const pageNum = parseInt(pageNumber) || 1
  const totalPages = 2
  const [isFlipping, setIsFlipping] = useState(false)
  const [growth, setGrowth] = useState(15)
  const [messageCount, setMessageCount] = useState(0)
  const [inputValue, setInputValue] = useState('')

  const nextPage = () => {
    if (pageNum < totalPages && !isFlipping) {
      setIsFlipping(true)
      setTimeout(() => {
        navigate(`/book/page/${pageNum + 1}`)
        setIsFlipping(false)
      }, 800)
    }
  }

  const prevPage = () => {
    if (pageNum > 1 && !isFlipping) {
      setIsFlipping(true)
      setTimeout(() => {
        navigate(`/book/page/${pageNum - 1}`)
        setIsFlipping(false)
      }, 800)
    }
  }

  const handleSendMessage = () => {
    if (!inputValue.trim()) return
    // Increase growth when message is sent - NOT on page flip
    setMessageCount(prev => prev + 1)
    setGrowth(prev => Math.min(prev + 5, 100))
    setInputValue('') // Clear input after sending
  }

  return (
    <div className="book-page-container">
      <DashboardDropdown />
      <Bookshelf />
      <div className="vintage-background"></div>
      
      <div className="book-page-header">
        <h1>Chatbot Page {pageNum}</h1>
      </div>

      <div className="book-page-content">
        <div className="main-content-wrapper">
          {/* Goal Garden - Left of book */}
          <div className="garden-container-left">
            <GoalGarden growth={growth} pageNumber={pageNum} />
          </div>

          <div className="book-wrapper">
            <div className="book-container">
              <div className="book-spine-vintage"></div>
              
              {/* Left Page - Guide (static, doesn't flip) */}
              <div className="book-page left-page vintage-page">
                <div className="page-content">
                  <div className="page-decorative-top"></div>
                  <ChatbotGuide pageNumber={pageNum} />
                  <div className="page-number-vintage">{pageNum}</div>
                </div>
              </div>

            {/* Right Page - Chatbot (flips like a book) */}
            <div className="right-page-wrapper">
              <AnimatePresence mode="wait">
                <motion.div
                  key={pageNum}
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
                          <h3>Chatbot {pageNum}</h3>
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
                    
                    <div className="page-number-vintage">{pageNum + 1}</div>
                  </div>
                </motion.div>
              </AnimatePresence>
            </div>

              <div className="book-shadow"></div>
              <div className="book-highlight"></div>
            </div>
          </div>
        </div>

        {/* Navigation */}
        <div className="book-page-navigation">
          <button 
            onClick={prevPage} 
            disabled={pageNum === 1 || isFlipping}
            className="nav-button-vintage prev-button"
          >
            <span className="button-icon">←</span>
            <span>Previous Page</span>
          </button>
          <div className="page-indicator-vintage">
            <span className="page-current">{pageNum}</span>
            <span className="page-separator">/</span>
            <span className="page-total">{totalPages}</span>
          </div>
          <button 
            onClick={nextPage} 
            disabled={pageNum === totalPages || isFlipping}
            className="nav-button-vintage next-button"
          >
            <span>Next Page</span>
            <span className="button-icon">→</span>
          </button>
        </div>
      </div>
    </div>
  )
}

export default BookPage
