import React from "react";
import Header from "./components/Header";
import './styles/StudentDashboard.css';

function StudentDashboard() {
    return (
        <div className="page-background">
            <Header />
            <div className="welcome-message">Welcome to the Student Dashboard</div>
            <section className="section">
                {/* Other components or sections */}
            </section>
        </div>
    );
}

export default StudentDashboard;
