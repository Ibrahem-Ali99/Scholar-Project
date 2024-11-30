import { useEffect, useState } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import styles from './Login.module.css';

function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const navigate = useNavigate();
  const location = useLocation();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setSuccess('');

    try {
      // Login function using fetch
      const response = await fetch('http://localhost:5000/auth/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
      });

      const result = await response.json(); // Parse the response as JSON

      if (response.ok) {
        setSuccess(result.message); // Display the success message

        // Redirect based on user role (student, teacher, or parent)
        if (result.role === 'student') {
          navigate('/student-dashboard');
        } else if (result.role === 'teacher') {
          navigate('/teacher-dashboard');
        } else if (result.role === 'parent') {
          navigate('/parent-dashboard');
        } else {
          setError('Unknown user role.');
        }
      } else {
        setError(result.message || 'Something went wrong');
      }
    } catch (err) {
      console.error('Error during login:', err);
      setError('Something went wrong. Please try again.');
    }
  };

  // Google login redirect to backend
  const handleGoogleLogin = () => {
    window.location.href = 'http://localhost:5000/auth/google-login'; 
  };

  useEffect(() => {
    // Check if we're on the callback URL
    if (location.pathname === '/auth/google/callback') {
      // Get the role from the query string
      const role = new URLSearchParams(window.location.search).get('role');
      
      if (!role) {
        setError('No role found in URL.');
        return;
      }

      // Redirect based on the role
      if (role === 'student') {
        navigate('/student-dashboard');
      } else if (role === 'teacher') {
        navigate('/teacher-dashboard');
      } else if (role === 'parent') {
        navigate('/parent-dashboard');
      } else {
        setError('Unknown role.');
      }
    }
  }, [location, navigate]);

  return (
    <div className={styles.authContainer}>
      <div className={styles.authCard}>
        <div className={styles.left}>
          <h1 className={styles.title}>Scholar</h1>
          <div className={styles.socialLogin}>
            <button className={styles.google} onClick={handleGoogleLogin}>
              Sign in with Google
            </button>
          </div>
          <p className={styles.or}>or use your email password</p>
          <form onSubmit={handleSubmit} className={styles.form}>
            {error && <p className={styles.error}>{error}</p>}
            {success && <p className={styles.success}>{success}</p>}
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
            <p className={styles.forgot} onClick={() => navigate('/forgot-password')}>
              Forgot Your Password?
            </p>
            <button type="submit" className={styles.btn}>
              Sign In
            </button>
          </form>
        </div>
        <div className={styles.right}>
          <h3>Hello!</h3>
          <p>Register with your personal details to use all of our site features.</p>
          <button className={styles.btn} onClick={() => navigate('/signup')}>
            Sign Up
          </button>
        </div>
      </div>
    </div>
  );
}

export default Login;
