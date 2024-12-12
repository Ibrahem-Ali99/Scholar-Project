import React from "react";
import "./StudentSidebar.css";

function StudentSidebar({ handleMenuClick }) {
    return (
        <div className="sidebar">
            <div className="sidebar-header">
                <h3 className="brand">
                    <span>SCHOLAR</span>
                </h3>
            </div>
            <ul className="nav-links">
                <li>
                    <a href="#home" className="nav-item" onClick={() => handleMenuClick("home")}>
                        <span className="nav-icon">
                            <i className="fas fa-home"></i>
                        </span>
                        <span>Home</span>
                    </a>
                </li>
                <li>
                    <a href="#courses" className="nav-item" onClick={() => handleMenuClick("courses")}>
                        <span className="nav-icon">
                            <i className="fas fa-book"></i>
                        </span>
                        <span>Courses</span>
                    </a>
                </li>
                <li>
                    <a href="#assessments" className="nav-item" onClick={() => handleMenuClick("assessments")}>
                        <span className="nav-icon">
                            <i className="fas fa-file-alt"></i>
                        </span>
                        <span>Assessments</span>
                    </a>
                </li>
            </ul>
            <div className="logout">
                <a href="#logout" className="nav-item">
                    <span className="nav-icon">
                        <i className="fas fa-sign-out-alt"></i>
                    </span>
                    <span>Logout</span>
                </a>
            </div>
        </div>
    );
}

export default StudentSidebar;
