import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import styles from './SignUp.module.css';

function Signup() {
  const [userType, setUserType] = useState(null); // Initially no user type selected
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleSignup = async (e) => {
    e.preventDefault();
    setLoading(true);

    // Check if a user type is selected
    if (!userType) {
      setError('Please select a user type before proceeding.');
      setLoading(false);
      return;
    }

    const formData = {
      role: userType,
      name: e.target.name.value,
      email: e.target.email.value,
      password: e.target.password.value,
    };

    // Validate user input
    if (formData.password.length < 8) {
      setError('Password must be at least 8 characters long.');
      setLoading(false);
      return;
    }

    try {
      const response = await fetch('http://localhost:5000/auth/signup', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      const result = await response.json();

      if (response.ok) {
        setSuccess(result.message || 'Signup successful!');
        setError('');
        setTimeout(() => navigate('/login'), 2000); // Redirect after success
      } else {
        setError(result.error || 'Signup failed. Please try again.');
        setSuccess('');
      }
    } catch (err) {
      setError('Network error. Please try again later.', err);
      setSuccess('');
    } finally {
      setLoading(false);
    }
  };


  
  const handleGoogleSignup = async () => {
    if (!userType) {
        setError('Please select a user type before signing up with Google.');
        return;
    }

    if (userType === 'parent') {
        const studentId = document.querySelector('input[name="student_id"]').value;

        if (!studentId) {
            setError('Student ID is required for parent signup.');
            return;
        }

        try {
            console.log("Student ID:", studentId);
            const response = await fetch('http://localhost:5000/auth/set-student-id', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ student_id: studentId }),
            });

            const data = await response.json();
            if (!response.ok) {
                setError(data.error || 'Failed to initiate Google signup.');
                return;
            }
            window.location.href = 'http://localhost:5000/auth/google-login';
        } catch (error) {
            setError('An unexpected error occurred. Please try again.');
            console.error(error);
        }
    } else {
        window.location.href = 'http://localhost:5000/auth/google-login';
    }
};



  return (
    <div className={styles.signupPage}>
      <div className={styles.authCard}>
        <div className={styles.left}>
          <h1 className={styles.title}>Scholar</h1>
          <div className={styles.socialSignup}>
            <button
              className={styles.google}
              onClick={handleGoogleSignup}
              aria-label="Sign Up with Google"
            >
              Sign Up with Google
            </button>
          </div>
          <p className={styles.or}>or sign up with your email</p>
          <form onSubmit={handleSignup}>
            {error && <p className={styles.error}>{error}</p>}
            {success && <p className={styles.success}>{success}</p>}
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
            <div className={styles.dropdownGroup}>
              <label htmlFor="userType" className={styles.dropdownLabel}>User Type</label>
              <select
                id="userType"
                name="userType"
                value={userType || ''}
                onChange={(e) => setUserType(e.target.value)}
                required
              >
                <option value="">Select User Type</option>
                <option value="student">Student</option>
                <option value="parent">Parent</option>
                <option value="teacher">Teacher</option>
              </select>
            </div>

            {/* Conditionally render the student ID input field */}
            {userType === 'parent' && (
              <input
                type="text"
                name="student_id"
                placeholder="Student ID"
                aria-label="Student ID"
                required
              />
            )}

            <button
              className={styles.btn}
              type="submit"
              disabled={loading} // Keep disabled if loading
              aria-label="Sign Up"
            >
              {loading ? 'Signing Up...' : 'Sign Up'}
            </button>
          </form>
        </div>
        <div className={styles.right}>
          <h3>Welcome Back!</h3>
          <p>Sign in with your account to continue exploring amazing features.</p>
          <button
            className={styles.btn}
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
