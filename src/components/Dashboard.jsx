import { useNavigate } from 'react-router-dom'
import './Dashboard.css'

function Dashboard() {
  const navigate = useNavigate()

  return (
    <div className="dashboard-container">
      <header className="dashboard-header">
        <h1>My Dashboard</h1>
        <div className="user-info">
          <button onClick={() => navigate('/')} className="home-button">
            Home
          </button>
        </div>
      </header>

      <main className="dashboard-main">
        <div className="dashboard-grid">
          <div className="dashboard-card" onClick={() => navigate('/')}>
            <div className="card-icon">📖</div>
            <h2>Landing Page</h2>
            <p>View the interactive book interface</p>
          </div>

          <div className="dashboard-card" onClick={() => navigate('/book/page/1')}>
            <div className="card-icon">💬</div>
            <h2>Chatbot Page 1</h2>
            <p>Access the first chatbot interface</p>
          </div>

          <div className="dashboard-card" onClick={() => navigate('/book/page/2')}>
            <div className="card-icon">💬</div>
            <h2>Chatbot Page 2</h2>
            <p>Access the second chatbot interface</p>
          </div>
        </div>
      </main>
    </div>
  )
}

export default Dashboard

