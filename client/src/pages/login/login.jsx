import './Login.css';
import { useState } from 'react';
import { login } from '../../api/api';
import { useNavigate } from 'react-router-dom';

function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await login({ email, password });
      setSuccess(response.message);
      setError('');
      
      // Redirect based on user type
      if (response.user_type === 'student') {
        navigate('/student-dashboard');
      } else if (response.user_type === 'teacher') {
        navigate('/teacher-dashboard');
      }
    } catch (err) {
      if (err.response && err.response.status === 401) {
        setError('Invalid email or password.');
      } else {
        setError('Something went wrong. Please try again.');
      }
    }
  };

  const handleGoogleLogin = () => {
    window.location.href = 'http://localhost:5000/auth/google-login';
  };

  return (
    <div className="auth-container">
      <div className="auth-card">
        <div className="left">
          <h1 className="title">Scholar</h1>
          <div className="social-login">
            <button className="google" onClick={handleGoogleLogin}>
              Sign in with Google
            </button>
          </div>
          <p className="or">or use your email password</p>
          <form onSubmit={handleSubmit}>
            {error && <p className="error">{error}</p>}
            {success && <p className="success">{success}</p>}
            <input
              type="email"
              placeholder="Email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
            <input
              type="password"
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
            <p className="forgot" onClick={() => navigate('/forgot-password')}>
              Forgot Your Password?
            </p>
            <button type="submit" className="btn">
              Sign In
            </button>
          </form>
        </div>
        <div className="right">
          <h3>Hello!</h3>
          <p>Register with your personal details to use all of our site features.</p>
          <button className="btn" onClick={() => navigate('/signup')}>
            Sign Up
          </button>
        </div>
      </div>
    </div>
  );
}

export default Login;
