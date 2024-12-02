from flask import Blueprint, jsonify, request
from models.user import Student
from models.course import Course
from models.enrollment import Enrollment

student_bp = Blueprint('students', __name__)

@student_bp.route('/students', methods=['GET'])
def get_students():
    teacher_id = request.args.get('teacher_id')
    if teacher_id:
        students = Student.query.join(Enrollment, Student.student_id == Enrollment.student_id) \
                                .join(Course, Enrollment.course_id == Course.course_id) \
                                .filter(Course.teacher_id == teacher_id) \
                                .with_entities(Student.student_id, Student.name, Student.email) \
                                .all()
    else:
        students = Student.query.with_entities(Student.student_id, Student.name, Student.email).all()
    
    student_list = [
        {
            "id": student.student_id,
            "name": student.name,
            "email": student.email
        }
        for student in students
    ]
    return jsonify(student_list)