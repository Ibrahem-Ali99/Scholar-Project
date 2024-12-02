import Header from "../../components/Header/Header";
// import MainBanner from "../../components/MainBanner/MainBanner";
import CoursePageBody from "../../components/CoursePageBody/CoursePageBody";
import Footer from "../../components/Footer/Footer";

function CoursePage() {

  return (
    <div className="course-page" style={{ paddingTop: "65px" }}>
      <Header/>
      <CoursePageBody />
      <Footer/>
    </div>
  );
}

export default CoursePage;
