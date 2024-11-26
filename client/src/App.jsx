import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './pages/login/login';
import Signup from './pages/signup/signup';
import ForgotPassword from './pages/forgotPassword/forgotPassword'; 
import ResetPassword from "./pages/resetPassword/resetPassword";
import './App.css'; 

function App() {
  return (
    <Router>
      {/* Main Routing Logic */}
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/forgot-password" element={<ForgotPassword />} />
        <Route path="/reset-password/:token" element={<ResetPassword />} />
      </Routes>
    </Router>
  );
}

export default App;
