import React from "react";
import "./StudentHeader.css";

function StudentHeader() {
  return (
    <header className="student-header">
      <div className="logo">
        <img src="PLACEHOLDER_LOGO" alt="Logo" />
        <h2>
          U<span className="danger">M</span>S
        </h2>
      </div>
      <div className="navbar">
        <a href="#home" className="active">
          <span className="material-icons-sharp">home</span>
          <h3>Home</h3>
        </a>
        <a href="#timetable">
          <span className="material-icons-sharp">today</span>
          <h3>Time Table</h3>
        </a>
        <a href="#exam">
          <span className="material-icons-sharp">grid_view</span>
          <h3>Examination</h3>
        </a>
        <a href="#password">
          <span className="material-icons-sharp">password</span>
          <h3>Change Password</h3>
        </a>
        <a href="#logout">
          <span className="material-icons-sharp">logout</span>
          <h3>Logout</h3>
        </a>
      </div>
      <div className="theme-toggler">
        <span className="material-icons-sharp active">light_mode</span>
        <span className="material-icons-sharp">dark_mode</span>
      </div>
    </header>
  );
}

export default StudentHeader;
