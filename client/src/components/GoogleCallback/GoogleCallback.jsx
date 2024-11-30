import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

const GoogleCallback = () => {
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    const handleGoogleCallback = async () => {
      try {
        const response = await fetch('http://localhost:5000/auth/google/callback', {
          method: 'GET',
        });

        const data = await response.json();

        if (response.ok) {
          // Perform the redirection based on the backend response
          navigate(data.redirect); // Programmatically navigate to the dashboard URL
        } else {
          setError(data.error || 'Google login failed.');
        }
      } catch (error) {
        setError('Network error occurred. Please try again.', error);
      } finally {
        setLoading(false);
      }
    };

    handleGoogleCallback();
  }, [navigate]);

  return (
    <div>
      {loading && <p>Loading...</p>}
      {error && <p>{error}</p>}
    </div>
  );
};

export default GoogleCallback;
