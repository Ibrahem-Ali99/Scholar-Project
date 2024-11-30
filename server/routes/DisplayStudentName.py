from flask import Blueprint, jsonify
from models import  Student, Course, Enrollment

student_bp = Blueprint('student', __name__)

@student_bp.route('/student', methods=['GET'])
def get_student_info():
    student_id = 1  
    
    student = Student.query.get_or_404(student_id)
    
    enrollments = Enrollment.query.filter_by(student_id=student_id).all()
    courses = []
    for enrollment in enrollments:
        course = Course.query.get(enrollment.course_id)
        courses.append({
            'course_id': course.course_id,
            'course_name': course.course_name
        })

    return jsonify({
        'student_name': student.name,
        'courses': courses
    })