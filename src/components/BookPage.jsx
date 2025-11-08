import { useParams, useNavigate } from 'react-router-dom'
import './BookPage.css'

function BookPage() {
  const { pageNumber } = useParams()
  const navigate = useNavigate()
  const pageNum = parseInt(pageNumber) || 1
  const totalPages = 2

  const nextPage = () => {
    if (pageNum < totalPages) {
      navigate(`/book/page/${pageNum + 1}`)
    }
  }

  const prevPage = () => {
    if (pageNum > 1) {
      navigate(`/book/page/${pageNum - 1}`)
    }
  }

  return (
    <div className="book-page-container">
      <div className="book-page-header">
        <button onClick={() => navigate('/dashboard')} className="back-button">
          ← Back to Dashboard
        </button>
        <h1>Chatbot Page {pageNum}</h1>
      </div>

      <div className="book-page-content">
        <div className="book-page-wrapper">
          {/* Left Page */}
          <div className="book-page-left">
            <div className="page-content-left">
              <h2>Page {pageNum}</h2>
              <p className="page-text">
                This is page {pageNum} of your interactive book. 
                Navigate between pages to access different chatbot experiences.
              </p>
              <div className="page-number-left">{pageNum}</div>
            </div>
          </div>

          {/* Right Page */}
          <div className="book-page-right">
            <div className="page-content-right">
              <div className="chatbot-placeholder-full">
                <div className="chatbot-header-full">
                  <h3>Chatbot {pageNum}</h3>
                </div>
                <div className="chatbot-area-full">
                  <p>Chatbot interface will be placed here</p>
                  <div className="chatbot-icon-large">💬</div>
                  <p className="chatbot-subtitle">Ready for integration</p>
                </div>
              </div>
              <div className="page-number-right">{pageNum + 1}</div>
            </div>
          </div>
        </div>

        {/* Navigation */}
        <div className="book-page-navigation">
          <button 
            onClick={prevPage} 
            disabled={pageNum === 1}
            className="page-nav-button prev-nav-button"
          >
            ← Previous Page
          </button>
          <span className="page-indicator-nav">
            Page {pageNum} of {totalPages}
          </span>
          <button 
            onClick={nextPage} 
            disabled={pageNum === totalPages}
            className="page-nav-button next-nav-button"
          >
            Next Page →
          </button>
        </div>
      </div>
    </div>
  )
}

export default BookPage

