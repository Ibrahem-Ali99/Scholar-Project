import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import StudentDashboard from './pages/StudentDashboard/StudentDashboard';
import Login from './pages/Login/Login';
import SignUp from './pages/SignUp/SignUp';
import ResetPassword from './pages/ResetPassword/ResetPassword'; 
import ForgotPassword from './pages/ForgotPassword/ForgotPassword';
import GoogleCallback from './components/GoogleCallback/GoogleCallback';
import CoursePage from './pages/CoursePage/CoursePage';  

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<SignUp />} />
        <Route path="/student-dashboard" element={<StudentDashboard />} />
        <Route path="/reset-password/:token" element={<ResetPassword />} /> 
        <Route path="/forgot-password" element={<ForgotPassword />} /> 
        <Route path="/google/callback" element={<GoogleCallback />} /> 
        <Route path="/course/:courseId" element={<CoursePage />} /> 
        {/* Add other routes as needed */}
        {/* Add a default route (e.g., home or a redirect page) */}
      </Routes>
    </Router>
  );
}

export default App;
