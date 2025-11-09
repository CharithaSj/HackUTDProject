import { useAuth0 } from '@auth0/auth0-react'
import './Login.css'

function Login() {
  const { loginWithRedirect } = useAuth0()

  return (
    <div className="login-container">
      <div className="login-card">
        <h1>Welcome to Book Chatbot</h1>
        <p>Sign in to continue your reading journey</p>
        <button onClick={() => loginWithRedirect()} className="login-button">
          Log In / Sign Up
        </button>
      </div>
    </div>
  )
}

export default Login

