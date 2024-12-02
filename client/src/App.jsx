import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import LandingPage from './pages/LandingPage/LandingPage';
import Login from './pages/Register/Login/Login';
import SignUp from './pages/Register/SignUp/SignUp';
import ResetPassword from './pages/Register/ResetPassword/ResetPassword';
import ForgotPassword from './pages/Register/ForgotPassword/ForgotPassword';
import GoogleCallback from './components/GoogleCallback/GoogleCallback';
import CoursePage from './pages/CoursePage/CoursePage';
import '@fortawesome/fontawesome-free/css/all.css';
import StudentDashboard from "./pages/StudentDashboard/StudentDashboard";


import Dashboard from "./pages/TeacherDashboard/dashboard/Dashboard";
import Calendar from "./pages/TeacherDashboard/calendar/Calendar";
import Course from "./pages/TeacherDashboard/course/Course";
import Student from "./pages/TeacherDashboard/students/Student";
import BarChart from "./pages/TeacherDashboard/barChart/BarChart";
import PieChart from "./pages/TeacherDashboard/pieChart/PieChart";
import LineChart from "./pages/TeacherDashboard/lineChart/LineChart";

import DashApp from './pages/TeacherDashboard/DashApp.jsx';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';



function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<LandingPage/>}/>
                <Route path="/login" element={<Login/>}/>
                <Route path="/signup" element={<SignUp/>}/>
                <Route path="/reset-password/:token" element={<ResetPassword/>}/>
                <Route path="/forgot-password" element={<ForgotPassword/>}/>
                <Route path="/google/callback" element={<GoogleCallback/>}/>
                <Route path="/course/:courseId" element={<CoursePage/>}/>
                <Route path="/pages/dashboard/Dashboard" element={<Dashboard/>}/>
                
                {/* teacher dashboard */}
                <Route path="/teacher-dashboard/*" element={<DashApp />} /> {/* Add this route */}
                <Route path="/bar" element={<BarChart />} />
                <Route path="/pie" element={<PieChart />} />
                <Route path="/line" element={<LineChart />} />
                <Route path="/calendar" element={<Calendar />} />
                <Route path="/students" element={<Student />} />
                <Route path="courses" element={<Course />} />
                <Route path="/student-dashboard" element={<StudentDashboard />} />
        
                <Route path="*" element={<LandingPage/>}/>
            </Routes>
        </Router>
        
    );
}

export default App;
