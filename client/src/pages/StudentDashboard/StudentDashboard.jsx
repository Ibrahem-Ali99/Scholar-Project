import React from "react";
import Header from "../../components/Header/Header";
import MainBanner from "../../components/MainBanner/MainBanner";
import FeatureOffering from "../../components/FeatureOffering/FeatureOffering";
import AboutUs from "../../components/AboutUs/AboutUs"; 
import Courses from "../../components/Courses/Courses";
import Teachers from "../../components/Teachers/Teachers";
import Feedback from "../../components/Feedback/Feedback";
function StudentDashboard() {
  return (
    <div className="student-dashboard">
      <Header />
      <MainBanner />
      <FeatureOffering />
      <AboutUs  />
      <Courses />
      <Teachers />
      <Feedback />
    </div>
  );
}

export default StudentDashboard;
