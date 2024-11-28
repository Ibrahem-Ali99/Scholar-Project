import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import StudentDashboard from './pages/StudentDashboard/StudentDashboard';
import Login from './pages/Login/Login';
import SignUp from './pages/SignUp/SignUp';
import ResetPassword from './pages/ResetPassword/ResetPassword'; 
import ForgotPassword from './pages/ForgotPassword/ForgotPassword';
import GoogleLoginCallback from './components/Auth/GoogleLoginCallback';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<SignUp />} />
        <Route path="/student-dashboard" element={<StudentDashboard />} />
        <Route path="/reset-password/:token" element={<ResetPassword />} /> {/* Tokenized route */}
        <Route path="/forgot-password" element={<ForgotPassword />} /> {/* Forgot Password route */}
        <Route path="/auth/google/callback" element={<GoogleLoginCallback />} />
        {/* Add other routes as needed */}
        {/* Add a default route (e.g., home or a redirect page) */}
      </Routes>
    </Router>
  );
}

export default App;
