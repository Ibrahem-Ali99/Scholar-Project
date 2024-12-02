# server/routes/dashboard.py
from flask import Blueprint, jsonify, request
from utils.db import db
from models import Student, Payment, StudentProgress, Enrollment, Course

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard/students-enrolled', methods=['GET'])
def get_students_enrolled():
    teacher_id = request.args.get('teacher_id')
    if not teacher_id:
        return jsonify({"error": "teacher_id is required"}), 400

    course_ids = db.session.query(Course.course_id).filter_by(teacher_id=teacher_id).all()
    course_ids = [cid[0] for cid in course_ids]

    student_count = db.session.query(Enrollment.student_id).filter(Enrollment.course_id.in_(course_ids)).distinct().count()
    return jsonify({"title": f"{student_count:,}", "subTitle": "Students Enrolled"})

@dashboard_bp.route('/dashboard/money-obtained', methods=['GET'])
def get_money_obtained():
    teacher_id = request.args.get('teacher_id')
    if not teacher_id:
        return jsonify({"error": "teacher_id is required"}), 400

    course_ids = db.session.query(Course.course_id).filter_by(teacher_id=teacher_id).all()
    course_ids = [cid[0] for cid in course_ids]

    total_amount = db.session.query(db.func.sum(Payment.amount)).filter(Payment.course_id.in_(course_ids)).scalar()
    total_amount = total_amount if total_amount else 0.00
    return jsonify({"title": f"{total_amount:,.2f}", "subTitle": "Money Obtained"})
