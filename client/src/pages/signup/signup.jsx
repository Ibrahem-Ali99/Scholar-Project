/* eslint-disable no-unused-vars */
import { useState } from 'react';
import './Signup.css';

function Signup() {
  const [userType, setUserType] = useState('student');
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');

  const handleSignup = async (e) => {
    e.preventDefault();

    const formData = {
      user_type: userType,
      name: e.target.name.value,
      email: e.target.email.value,
      password: e.target.password.value,
    };

    try {
      const response = await fetch('http://localhost:5000/auth/signup', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      const data = await response.json();

      if (response.ok) {
        setSuccess(data.message || 'Signup successful!');
        setError('');
      } else {
        setError(data.message || 'Something went wrong.');
        setSuccess('');
      }
    } catch (err) {
      setError('Network error. Please try again later.');
      setSuccess('');
    }
  };

  return (
    <div className="auth-container">
      <div className="auth-card">
        <div className="left">
          <h1 className="title">Scholar</h1>
          <form onSubmit={handleSignup}>
            {error && <p className="error">{error}</p>}
            {success && <p className="success">{success}</p>}
            <input type="text" name="name" placeholder="Name" required />
            <input type="email" name="email" placeholder="Email" required />
            <input type="password" name="password" placeholder="Password" required />
            <div className="radio-group">
              <label className="radio-option">
                <input
                  type="radio"
                  name="userType"
                  value="student"
                  checked={userType === 'student'}
                  onChange={(e) => setUserType(e.target.value)}
                />
                <span>Student</span>
              </label>
              <label className="radio-option">
                <input
                  type="radio"
                  name="userType"
                  value="parent"
                  checked={userType === 'parent'}
                  onChange={(e) => setUserType(e.target.value)}
                />
                <span>Parent</span>
              </label>
              <label className="radio-option">
                <input
                  type="radio"
                  name="userType"
                  value="teacher"
                  checked={userType === 'teacher'}
                  onChange={(e) => setUserType(e.target.value)}
                />
                <span>Teacher</span>
              </label>
            </div>
            <button className="btn" type="submit">
              Sign Up
            </button>
          </form>
        </div>
        <div className="right">
          <h3>Welcome Back!</h3>
          <p>Sign in with your account to continue exploring amazing features.</p>
          <button className="btn" onClick={() => (window.location.href = '/login')}>
            Sign In
          </button>
        </div>
      </div>
    </div>
  );
}

export default Signup;
