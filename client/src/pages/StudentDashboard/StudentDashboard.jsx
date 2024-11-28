import Header from "../../components/Header/Header";
import MainBanner from "../../components/MainBanner/MainBanner";
import FeatureOffering from "../../components/FeatureOffering/FeatureOffering";
import AboutUs from "../../components/AboutUs/AboutUs"; 
import Courses from "../../components/Courses/Courses";
import Teachers from "../../components/Teachers/Teachers";

function StudentDashboard() {
  return (
    <div className="student-dashboard">
      <Header />
      <MainBanner />
      <FeatureOffering />
      <AboutUs  />
      <Courses />
      <Teachers />
    </div>
  );
}

export default StudentDashboard;
