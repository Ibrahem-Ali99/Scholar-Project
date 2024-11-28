import { useEffect, useState } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';

function GoogleLoginCallback() {
  const [error, setError] = useState('');
  const navigate = useNavigate();
  const location = useLocation();

  useEffect(() => {
    // Ensure that we have the 'code' from Google in the URL query params
    const code = new URLSearchParams(window.location.search).get('code');
    
    if (!code) {
      setError('No code found in URL');
      return;
    }

    // Send the code to the backend to exchange for user data
    fetch('http://localhost:5000/auth/google/callback', {
      method: 'GET',
    })
      .then((response) => response.json())
      .then((result) => {
        if (result.redirect) {
          // Handle redirection based on the backend response
          navigate(result.redirect);  // This will redirect to the appropriate dashboard
        } else {
          setError('Error during Google login callback: Missing redirect URL.');
        }
      })
      .catch((err) => {
        setError('Error during Google login callback: ' + err.message);
      });
  }, [location, navigate]);

  return (
    <div>
      {error && <p>{error}</p>}
      <p>Processing Google login...</p>
    </div>
  );
}

export default GoogleLoginCallback;