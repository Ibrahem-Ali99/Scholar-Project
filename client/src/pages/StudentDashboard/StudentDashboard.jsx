import React, { useState } from "react";
import StudentSidebar from "../../components/StudentSidebar/StudentSidebar";
import StudentGreeting from "../../components/StudentGreeting/StudentGreeting"; 

function StudentDashboard() {
    const [activeMenu, setActiveMenu] = useState("home"); 

    const handleMenuClick = (menu) => {
        setActiveMenu(menu); 
    };

    return (
        <div className="student-dashboard">
            <StudentSidebar handleMenuClick={handleMenuClick} />
            <div className="main-content">
                {activeMenu === "home" && <StudentGreeting />} 
                {activeMenu === "courses" && <div>Courses Content</div>} 
                {activeMenu === "assessments" && <div>Assessments Content</div>} 
            </div>
        </div>
    );
}

export default StudentDashboard;
