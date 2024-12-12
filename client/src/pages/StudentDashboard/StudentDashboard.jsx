import React, { useState } from "react";
import StudentSidebar from "../../components/StudentDashboard/StudentSidebar/StudentSidebar";
import StudentGreeting from "../../components/StudentDashboard/StudentGreeting/StudentGreeting";
import StudentEnrollCourses from "../../components/StudentDashboard/StudentEnrollCourses/StudentEnrollCourses";
import AnnouncementsAndTeachers from "../../components/StudentDashboard/AnnouncementsAndTeachers/AnnouncementsAndTeachers";

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
