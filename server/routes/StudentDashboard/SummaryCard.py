# from flask import Blueprint, jsonify, request
# from models.enrollment import Enrollment
# from models.student_progress import StudentProgress
# from models.course_assessment import CourseAssessment
# from models.attendance import Attendance  # If attendance exists
# from sqlalchemy.sql import func

# performance_bp = Blueprint('performance', __name__)

# @performance_bp.route('/performance_summary', methods=['GET'])
# def performance_summary():
#     student_id = request.args.get('student_id', type=int)
#     if not student_id:
#         return jsonify({"error": "Student ID is required"}), 400

#     total_courses = Enrollment.query.filter_by(student_id=student_id).count()

#     completed_courses = Enrollment.query.filter_by(student_id=student_id, completion_status="completed").count()

#     avg_score = StudentProgress.query.with_entities(func.avg(StudentProgress.score)).filter_by(student_id=student_id).scalar()
#     avg_score = round(avg_score, 2) if avg_score else 0

#     total_assessments = CourseAssessment.query.count()
#     completed_assessments = StudentProgress.query.filter_by(student_id=student_id).count()
#     pending_assessments = total_assessments - completed_assessments

#     attendance = Attendance.query.filter_by(student_id=student_id).with_entities(func.avg(Attendance.percentage)).scalar()
#     attendance = round(attendance, 2) if attendance else 0

#     return jsonify({
#         "total_courses": total_courses,
#         "completed_courses": completed_courses,
#         "avg_score": avg_score,
#         "pending_assessments": pending_assessments,
#         "attendance": attendance
#     })
