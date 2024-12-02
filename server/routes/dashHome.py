# routes/dash_home.py
from flask import Blueprint, jsonify
from models.user import Student, Teacher, Parent, Admin
from models.course import Course
from models.enrollment import Enrollment

dash_home_bp = Blueprint('dash_home_bp', __name__)

@dash_home_bp.route('/api/admin', methods=['GET'])
def get_dashboard_data():
    try:
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
        pending_approvals = 0  # Implement logic for pending approvals
        daily_active_users = 0  # Implement logic for daily active users

        dashboard_data = {
            'total_users': total_users,
            'active_courses': active_courses,
            'pending_approvals': pending_approvals,
            'daily_active_users': daily_active_users
        }

        return jsonify(dashboard_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500