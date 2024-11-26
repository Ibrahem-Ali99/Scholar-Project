import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Signup.css';
import { signup } from '../../api/api';

function Signup() {
  const [userType, setUserType] = useState('student');
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleSignup = async (e) => {
    e.preventDefault();
    setLoading(true);
  
    const formData = {
      role: userType,
      name: e.target.name.value,
      email: e.target.email.value,
      password: e.target.password.value,
    };
  
    // Validate user input
    if (!['student', 'parent', 'teacher'].includes(userType)) {
      setError('Invalid user type selected.');
      setLoading(false);
      return;
    }
  
    if (formData.password.length < 8) {
      setError('Password must be at least 8 characters long.');
      setLoading(false);
      return;
    }
  
    try {
      // Use the imported signup function
      const response = await signup(formData);
      setSuccess(response.message || 'Signup successful!');
      setError('');
      setTimeout(() => navigate('/login'), 2000); // Redirect after success
    } catch (err) {
      console.error('Signup Error:', err.response?.data || err.message);
      setError(err.response?.data?.message || 'Network error. Please try again later.');
      setSuccess('');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="signup-page auth-container">
      <div className="auth-card">
        <div className="left">
          <h1 className="title">Scholar</h1>
          <div className="social-signup">
            <button
              className="google"
              onClick={() => {
                window.location.href = 'http://localhost:5000/auth/google-login';
              }}
              aria-label="Sign Up with Google"
            >
              Sign Up with Google
            </button>
          </div>
          <p className="or">or sign up with your email</p>
          <form onSubmit={handleSignup}>
          {error && <p className="error">{error}</p>}
          {success && <p className="success">{success}</p>}
          <input
            type="text"
            name="name"
            placeholder="Name"
            aria-label="Full Name"
            required
          />
          <input
            type="email"
            name="email"
            placeholder="Email"
            aria-label="Email Address"
            required
          />
          <input
            type="password"
            name="password"
            placeholder="Password"
            aria-label="Password"
            required
          />
          
          {/* Dropdown for User Type */}
          <div className="dropdown-group">
            <label htmlFor="userType" className="dropdown-label">User Type</label>
            <select
              id="userType"
              name="userType"
              value={userType}
              onChange={(e) => setUserType(e.target.value)}
              required
            >
              <option value="student">Student</option>
              <option value="parent">Parent</option>
              <option value="teacher">Teacher</option>
            </select>
          </div>

          <button
            className="btn"
            type="submit"
            disabled={loading}
            aria-label="Sign Up"
          >
            {loading ? 'Signing Up...' : 'Sign Up'}
          </button>
        </form>
        </div>
        <div className="right">
          <h3>Welcome Back!</h3>
          <p>Sign in with your account to continue exploring amazing features.</p>
          <button
            className="btn"
            onClick={() => navigate('/login')}
            aria-label="Sign In"
          >
            Sign In
          </button>
        </div>
      </div>
    </div>
  );
}

export default Signup;
