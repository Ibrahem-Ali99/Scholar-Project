import React from "react";
import Header from "../../components/Header/Header";
import MainBanner from "../../components/MainBanner/MainBanner";
import FeatureOffering from "../../components/FeatureOffering/FeatureOffering";
import AboutUs from "../../components/AboutUs/AboutUs"; 
import LandingPageCourses from "../../components/LandingPageCourses/LandingPageCourses";
import Teachers from "../../components/Teachers/Teachers";
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
      <Teachers />
      <Feedback />
      <Footer />
    </div>
  );
}

export default LandingPage;
