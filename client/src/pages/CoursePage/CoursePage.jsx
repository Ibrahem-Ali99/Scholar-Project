/* eslint-disable react/prop-types */
import { useState, useEffect } from 'react';

function CoursePage({ courseId }) {
  const [courseData, setCourseData] = useState(null);  // To hold course data
  const [loading, setLoading] = useState(true);  // To manage loading state
  const [error, setError] = useState(null);  // To handle errors

  // Fetch course data when component mounts
  useEffect(() => {
    const fetchCourseData = async () => {
      try {
        const response = await fetch(`/api/courses/${courseId}`);
        if (!response.ok) {
          throw new Error('Failed to fetch course data');
        }
        const data = await response.json();
        setCourseData(data);  // Set course data
        setLoading(false);  // Set loading state to false after data is fetched
      } catch (err) {
        setError(err.message);  // Handle error
        setLoading(false);  // Set loading state to false if an error occurs
      }
    };

    fetchCourseData();
  }, [courseId]);  // The effect runs when the courseId changes

  if (loading) {
    return <div>Loading...</div>;  // Show loading message while fetching data
  }

  if (error) {
    return <div>Error: {error}</div>;  // Show error if something goes wrong
  }

  // If data is loaded, render course data
  return (
    <div className="course-page">
      <h1>{courseData.course_name}</h1>
      <p>{courseData.course_description}</p>
      <h3>Teacher: {courseData.teacher_name}</h3>
      <p>Price: ${courseData.price}</p>
      <img src={courseData.image_url} alt={courseData.course_name} />
      
      <h2>Course Contents:</h2>
      <ul>
        {courseData.contents.map(content => (
          <li key={content.content_id}>
            <strong>{content.title}</strong> - {content.content_type} (Posted on: {content.post_date})
          </li>
        ))}
      </ul>

      <h2>Assessments:</h2>
      <ul>
        {courseData.assessments.map(assessment => (
          <li key={assessment.assessment_id}>
            {assessment.title} (Max Score: {assessment.max_score}, Deadline: {assessment.deadline})
          </li>
        ))}
      </ul>

      <h2>Ratings:</h2>
      <ul>
        {courseData.ratings.map(rating => (
          <li key={rating.rating_id}>
            Rating: {rating.rating} - {rating.comment}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default CoursePage;
