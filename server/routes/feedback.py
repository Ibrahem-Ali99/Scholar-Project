from flask import Blueprint, jsonify
from models import CourseRating

feedback_bp = Blueprint('feedback', __name__)

@feedback_bp.route('/ratings', methods=['GET'])
def get_all_feedbacks():
    feedbacks = CourseRating.query.all()  # Fetch all feedbacks from the CourseRating table
    feedback_list = []
    
    # Loop through the feedbacks and extract necessary information
    for feedback in feedbacks:
        feedback_list.append({
            'rating_id': feedback.rating_id,
            'student_name': feedback.student.name,  # Assuming 'name' is a column in the 'Student' table
            'rating': feedback.rating,
            'comment': feedback.comment,
            'course_name': feedback.course.course_name  # Assuming 'course_name' is a column in the 'Course' table
        })
    
    return jsonify(feedback_list)
