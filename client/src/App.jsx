import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import LandingPage from './pages/LandingPage/LandingPage';
import Login from './pages/Login/Login';
import SignUp from './pages/SignUp/SignUp';
import ResetPassword from './pages/ResetPassword/ResetPassword'; 
import ForgotPassword from './pages/ForgotPassword/ForgotPassword';
import GoogleCallback from './components/GoogleCallback/GoogleCallback';
import CoursePage from './pages/CoursePage/CoursePage';  
import '@fortawesome/fontawesome-free/css/all.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<SignUp />} />
        <Route path="/reset-password/:token" element={<ResetPassword />} /> 
        <Route path="/forgot-password" element={<ForgotPassword />} /> 
        <Route path="/google/callback" element={<GoogleCallback />} /> 
        <Route path="/course/:courseId" element={<CoursePage />} /> 
        <Route path="*" element={<LandingPage />} /> {/* Default Route */}
      </Routes>
    </Router>
  );
}

export default App;
