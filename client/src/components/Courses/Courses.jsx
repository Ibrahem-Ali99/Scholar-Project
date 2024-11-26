import React from "react";
import "./Courses.css";
import webdesignImage from "../../assets/Webdesign.avif";
import developmentImage from "../../assets/Programming.webp";
import wordpressImage from "../../assets/vite.svg";

function Courses() {
  const filters = [
    { id: "all", label: "Show All" },
    { id: "webdesign", label: "Webdesign" },
    { id: "development", label: "Development" },
    { id: "wordpress", label: "Wordpress" },
  ];

  const courses = [
    {
      id: "1",
      category: "webdesign",
      image: webdesignImage,
      price: "$160",
      title: "Learn Web Design",
    },
    {
      id: "2",
      category: "development",
      image: developmentImage,
      price: "$340",
      title: "Foundations of Programming",
    },
    {
      id: "3",
      category: "wordpress",
      image: wordpressImage,
      price: "$640",
      title: "Random Course",
    },
  ];

  return (
    <section className="courses">
      <div className="container">
        <div className="section-heading">
          <h2>Courses</h2>
        </div>
        <ul className="event_filter">
          {filters.map((filter) => (
            <li key={filter.id}>
              <a href="#!">{filter.label}</a>
            </li>
          ))}
        </ul>
        <div className="row">
          {courses.map((course) => (
            <div className="col-lg-4 col-md-6 course-card" key={course.id}>
              <div className="events_item">
                <div className="thumb">
                  <img src={course.image} alt={course.title} />
                  <span className="category">{course.category.toUpperCase()}</span>
                  <span className="price">
                    <h6>{course.price}</h6>
                  </span>
                </div>
                <div className="down-content">
                  <h4>{course.title}</h4>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

export default Courses;
