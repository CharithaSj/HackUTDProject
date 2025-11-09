import { useState, useRef, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import './DashboardDropdown.css'

function DashboardDropdown() {
  const [isOpen, setIsOpen] = useState(false)
  const dropdownRef = useRef(null)
  const navigate = useNavigate()

  useEffect(() => {
    const handleClickOutside = (event) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
        setIsOpen(false)
      }
    }

    if (isOpen) {
      document.addEventListener('mousedown', handleClickOutside)
    }

    return () => {
      document.removeEventListener('mousedown', handleClickOutside)
    }
  }, [isOpen])

  const handleNavigate = (path) => {
    navigate(path)
    setIsOpen(false)
  }

  return (
    <div className="dashboard-dropdown" ref={dropdownRef}>
      <button 
        className="dropdown-toggle"
        onClick={() => setIsOpen(!isOpen)}
        aria-label="Dashboard menu"
      >
        <span className="dropdown-icon">☰</span>
        <span className="dropdown-text">Dashboard</span>
      </button>
      
      {isOpen && (
        <div className="dropdown-menu">
          <button 
            className="dropdown-item"
            onClick={() => handleNavigate('/')}
          >
            <span className="item-icon">📖</span>
            <span>Landing Page</span>
          </button>
          <button 
            className="dropdown-item"
            onClick={() => handleNavigate('/book/page/1')}
          >
            <span className="item-icon">💬</span>
            <span>Chatbot Page 1</span>
          </button>
          <button 
            className="dropdown-item"
            onClick={() => handleNavigate('/book/page/2')}
          >
            <span className="item-icon">💬</span>
            <span>Chatbot Page 2</span>
          </button>
        </div>
      )}
    </div>
  )
}

export default DashboardDropdown

