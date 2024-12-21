import React, { useState } from "react";
import StudentSidebar from "../../components/StudentDashboard/StudentSidebar/StudentSidebar";
import StudentGreeting from "../../components/StudentDashboard/StudentGreeting/StudentGreeting";
import StudentEnrollCourses from "../../components/StudentDashboard/StudentEnrollCourses/StudentEnrollCourses";
import AnnouncementsAndTeachers from "../../components/StudentDashboard/AnnouncementsAndTeachers/AnnouncementsAndTeachers";
import PerformanceChart from "../../components/StudentDashboard/PerformanceChart/PerformanceChart";
import StudentFeedback from "../../components/StudentDashboard/StudentFeedback/StudentFeedback";
import Timetable from "../../components/StudentDashboard/Timetable/Timetable";
// import quiz from "../../components/StudentDashboard/quizpage/quiz"

function StudentDashboard() {
    const [activeMenu, setActiveMenu] = useState("home");

    const handleMenuClick = (menu) => {
        setActiveMenu(menu);
    };

    return (
        <div className="student-dashboard">
            <StudentSidebar handleMenuClick={handleMenuClick} />
            <div className="main-content">
                {activeMenu === "home" && (
                    <div>
                        <StudentGreeting />
                        <PerformanceChart />
                        <Timetable />
                        <AnnouncementsAndTeachers />
                        {/* <quiz/> */}
                    </div>
                )}
                {activeMenu === "courses" && <StudentEnrollCourses />}
                {activeMenu === "assessments" && <div>Assessments Content</div>}
                {activeMenu === "feedback" && <StudentFeedback />} 
            </div>
        </div>
    );
}

export default StudentDashboard;
