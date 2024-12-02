import { lazy, Suspense } from 'react'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import '@mui/material'

const LandingPage = lazy(() => import('./pages/LandingPage/LandingPage'));
const Login = lazy(() => import('./pages/Register/Login/Login'));
const SignUp = lazy(() => import('./pages/Register/SignUp/SignUp'));
const ResetPassword = lazy(() => import('./pages/Register/ResetPassword/ResetPassword'));
const ForgotPassword = lazy(() => import('./pages/Register/ForgotPassword/ForgotPassword'));
const GoogleCallback = lazy(() => import('./components/GoogleCallback/GoogleCallback'));
const CoursePage = lazy(() => import('./pages/CoursePage/CoursePage'));
const StudentDashboard = lazy(() => import('./pages/StudentDashboard/StudentDashboard'));
const Dashboard = lazy(() => import('./pages/TeacherDashboard/dashboard/Dashboard'));
const Calendar = lazy(() => import('./pages/TeacherDashboard/calendar/Calendar'));
const Course = lazy(() => import('./pages/TeacherDashboard/course/Course'));
const Student = lazy(() => import('./pages/TeacherDashboard/students/Student'));
const BarChart = lazy(() => import('./pages/TeacherDashboard/barChart/BarChart'));
const PieChart = lazy(() => import('./pages/TeacherDashboard/pieChart/PieChart'));
const LineChart = lazy(() => import('./pages/TeacherDashboard/lineChart/LineChart'));
const DashApp = lazy(() => import('./pages/TeacherDashboard/DashApp.jsx'));
// const AdminDashboard = lazy(() => import('./pages/AdminDashboard/AdminDashboard'));

import '@fortawesome/fontawesome-free/css/all.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';

// import pages from './pages/AdminDashboard/pages/pages'





function App() {
    return (
        <Router>
            <Suspense>
                <Routes>
                    <Route path="/" element={<LandingPage />} />
                    <Route path="/login" element={<Login />} />
                    <Route path="/signup" element={<SignUp />} />
                    <Route path="/reset-password/:token" element={<ResetPassword />} />
                    <Route path="/forgot-password" element={<ForgotPassword />} />
                    <Route path="/google/callback" element={<GoogleCallback />} />
                    <Route path="/course/:courseId" element={<CoursePage />} />
                    <Route path="/course/:courseId" element={<CoursePage />} />
                    <Route path="/pages/dashboard/Dashboard" element={<Dashboard />} />

                    <Route path="/teacher-dashboard/*" element={<DashApp />} />
                    <Route path="/bar" element={<BarChart />} />
                    <Route path="/pie" element={<PieChart />} />
                    <Route path="/line" element={<LineChart />} />
                    <Route path="/calendar" element={<Calendar />} />
                    <Route path="/students" element={<Student />} />
                    <Route path="courses" element={<Course />} />
                    <Route path="/student-dashboard" element={<StudentDashboard />} />

                    {/* <Route path='/admin' element={<AdminDashboard />}>
                        {
                            pages.map(page => (
                                <Route path={`/admin${page.path}`} element={page.page} />
                            ))
                        }
                    </Route> */}

                    <Route path="*" element={<LandingPage />} />
                </Routes>
            </Suspense>
        </Router>
    );
}

export default App;
