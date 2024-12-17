import React, { useState } from "react";
import StudentSidebar from "../../components/StudentDashboard/StudentSidebar/StudentSidebar";
import StudentGreeting from "../../components/StudentDashboard/StudentGreeting/StudentGreeting";
import StudentEnrollCourses from "../../components/StudentDashboard/StudentEnrollCourses/StudentEnrollCourses";
import AnnouncementsAndTeachers from "../../components/StudentDashboard/AnnouncementsAndTeachers/AnnouncementsAndTeachers";
import PerformanceChart from "../../components/StudentDashboard/PerformanceChart/PerformanceChart";
import Timetable from "../../components/StudentDashboard/Timetable/Timetable";

import "./StudentDashboard.css";

function StudentDashboard() {
    const [activeMenu, setActiveMenu] = useState("home");

    const handleMenuClick = (menu) => {
        setActiveMenu(menu);
        if (menu === "logout") {
            const confirmed = window.confirm("Are you sure you want to log out?");
            if (confirmed) {
                sessionStorage.clear();
                window.location.href = "/";
            }
        }
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
                    </div>
                )}
                {activeMenu === "courses" && <StudentEnrollCourses />}
                {activeMenu === "assessments" && <div>Assessments Content</div>}
            </div>
        </div>
    );
}

export default StudentDashboard;
