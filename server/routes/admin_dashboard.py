from flask import Blueprint, jsonify
from models.user import Student, Teacher, Parent, Admin
from models.course import Course
from models.enrollment import Enrollment
from models.payment import Payment
from models.hiring_requests import HiringRequest
from sqlalchemy import func
from datetime import datetime, date

dash_home_bp = Blueprint('dash_home_bp', __name__)

@dash_home_bp.route('/admin', methods=['GET'])
def get_dashboard_data():
    try:
        # Total Users
        total_students = Student.query.count()
        total_teachers = Teacher.query.count()
        total_parents = Parent.query.count()
        total_admins = Admin.query.count()
        total_users = {
            'students': total_students,
            'teachers': total_teachers,
            'parents': total_parents,
            'admins': total_admins
        }

        active_courses = Course.query.count()

        pending_approvals = HiringRequest.query.filter_by(status='pending').count()

        today = date.today()
        daily_active_users = Payment.query.filter(Payment.payment_date == today).count()

        enrollments = Enrollment.query.with_entities(
            func.extract('year', Enrollment.enrollment_date).label('year'),
            func.count(Enrollment.enrollment_id).label('count')
        ).group_by(
            func.extract('year', Enrollment.enrollment_date)
        ).order_by('year').all()

        enrollments_data = [
            {'year': int(year), 'count': count}
            for year, count in enrollments
        ]

        dashboard_data = {
            'total_users': total_users,
            'active_courses': active_courses,
            'pending_approvals': pending_approvals,
            'daily_active_users': daily_active_users,
            'enrollments_over_time': enrollments_data
        }

        return jsonify(dashboard_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
