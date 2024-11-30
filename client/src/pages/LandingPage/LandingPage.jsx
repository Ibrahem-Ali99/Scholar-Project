import React from "react";
import Header from "../../components/Header/Header";
import MainBanner from "../../components/MainBanner/MainBanner";
import FeatureOffering from "../../components/FeatureOffering/FeatureOffering";
import AboutUs from "../../components/AboutUs/AboutUs"; 
import LandingPageCourses from "../../components/LandingPageCourses/LandingPageCourses";
import DisplayTeachers from "../../components/DisplayTeachers/DisplayTeachers";
import Feedback from "../../components/Feedback/Feedback";
import Footer from "../../components/Footer/Footer";

function LandingPage() {
  return (
    <div className="landing-page">
      <Header />
      <MainBanner />
      <FeatureOffering />
      <AboutUs  />
      <LandingPageCourses />
      <DisplayTeachers />
      <Feedback />
      <Footer />
    </div>
  );
}

export default LandingPage;
