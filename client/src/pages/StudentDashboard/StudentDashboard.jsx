import React from "react";
import Header from "../../components/Header/Header";
import MainBanner from "../../components/MainBanner/MainBanner";
import FeatureOffering from "../../components/FeatureOffering/FeatureOffering";


function StudentDashboard() {
  return (
    <div className="student-dashboard">
      <Header />
      <MainBanner />
      <FeatureOffering />
    </div>
  );
}

export default StudentDashboard;
