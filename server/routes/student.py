from flask import Blueprint, jsonify, request
from models.user import Student
from models.course import Course
from models.enrollment import Enrollment

student_bp = Blueprint('students', __name__)

@student_bp.route('/students', methods=['GET'])
def get_students():
    teacher_id = request.args.get('teacher_id')
    if not teacher_id:
        return jsonify({"error": "teacher_id is required"}), 400

    try:
        # Example query: Get students enrolled in courses taught by the teacher
        courses = Course.query.filter_by(teacher_id=teacher_id).all()
        course_ids = [course.course_id for course in courses]
        students = Student.query.join(Enrollment).filter(Enrollment.course_id.in_(course_ids)).all()

        students_list = [{
            'id': student.id,  # Uses the 'id' property from BaseUser
            'name': student.name,
            'email': student.email
        } for student in students]

        return jsonify(students_list), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500