import React, { useState, useEffect } from "react";
import "./StudentGreeting.css";

function StudentGreeting() {
    const [studentName, setStudentName] = useState("Guest");  

    useEffect(() => {
        fetch("http://127.0.0.1:5000/student")  
            .then((response) => response.json())
            .then((data) => {
                if (data && data.student_name) {
                    setStudentName(data.student_name);  
                } else {
                    console.error("Student data is invalid or missing name");
                }
            })
            .catch((error) => {
                console.error("Error fetching student data:", error);
            });
    }, []); 

    return (
        <section className="greeting" id="greeting">
            <div className="container">
                <div className="section-heading">
                    <h2>Welcome!</h2>
                </div>
                <div className="row">
                    <div className="col-lg-12">
                        <div className="greeting-card">
                            <h3>Hello, {studentName}!</h3> 
                            <p>We're glad to have you on the Scholar platform. Enjoy your learning journey!</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    );
}

export default StudentGreeting;
