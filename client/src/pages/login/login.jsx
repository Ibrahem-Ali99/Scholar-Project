/* eslint-disable no-unused-vars */
import './Login.css';
import { useState } from 'react';
import { login } from '../../api/api';

function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await login({ email, password });
      setSuccess(response.message); // Show success message
      setError(''); // Clear error
      console.log('User Type:', response.user_type); // Example: Redirect based on user type
    } catch (err) {
      setError(err.message || 'An error occurred'); // Show error message
    }
  };

  const handleForgotPassword = () => {
    // Redirect to the forgot password page
    window.location.href = '/forgot-password';
  };

  return (
    <div className="auth-container">
      <div className="auth-card">
        <div className="left">
          <h1 className="title">Scholar</h1>
          <div className="social-login">
            <button className="google">Sign in with Google</button>
          </div>
          <p className="or">or use your email password</p>
          <form onSubmit={handleSubmit}>
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
            <p className="forgot" onClick={handleForgotPassword}>
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
          <button className="btn" onClick={() => (window.location.href = '/signup')}>
            Sign Up
          </button>
        </div>
      </div>
    </div>
  );
}

export default Login;
