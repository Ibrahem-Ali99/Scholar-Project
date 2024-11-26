import axios from 'axios';

// Base URL for your Flask backend
const API = axios.create({
  baseURL: 'http://localhost:5000/auth', // Ensure this matches your backend URL
});

export default API;

/**
 * Signup API
 * @param {Object} userData - The user data for signup (name, email, password, role)
 */
export const signup = async (userData) => {
  try {
    const response = await API.post('/signup', userData); // Use API instance
    return response.data;
  } catch (error) {
    throw error.response ? error.response.data : new Error('Network Error');
  }
};

/**
 * Login API
 * @param {Object} userData - The user data for login (email, password)
 */
export const login = async (userData) => {
  try {
    const response = await API.post('/login', userData); // Use API instance
    return response.data;
  } catch (error) {
    throw error.response ? error.response.data : new Error('Network Error');
  }
};

/**
 * Forgot Password API
 * @param {string} email - The email address of the user
 */
export const forgotPassword = async (email) => {
  try {
    const response = await API.post('/forgot-password', { email }); // Use API instance
    return response.data;
  } catch (error) {
    throw error.response ? error.response.data : new Error('Network Error');
  }
};

/**
 * Reset Password API
 * @param {string} token - The reset token from the email
 * @param {Object} data - The new password data { new_password }
 */
export const resetPassword = async (token, data) => {
  try {
    const response = await API.post(`/reset-password/${token}`, data); // Use API instance
    return response.data;
  } catch (error) {
    throw error.response ? error.response.data : new Error('Network Error');
  }
};

/**
 * Google Login Redirect
 * @returns {Promise<string>} The URL to redirect the user to Google Login
 */
export const googleLogin = async () => {
  try {
    const response = await API.get('/google-login'); // Use API instance
    return response.data;
  } catch (error) {
    throw error.response ? error.response.data : new Error('Network Error');
  }
};

/**
 * Google Callback API
 * @param {string} code - The authorization code returned by Google
 */
export const googleCallback = async (code) => {
  try {
    const response = await API.get('/google/callback', {
      params: { code },
    }); // Use API instance
    return response.data;
  } catch (error) {
    throw error.response ? error.response.data : new Error('Network Error');
  }
};

/**
 * Logout API
 */
export const logout = async () => {
  try {
    const response = await API.post('/logout'); // Use API instance
    return response.data;
  } catch (error) {
    throw error.response ? error.response.data : new Error('Network Error');
  }
};
