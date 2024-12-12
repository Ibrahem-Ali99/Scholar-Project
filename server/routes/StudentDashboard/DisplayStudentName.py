from flask import Blueprint, jsonify, request
from models import Student

student_name_bp = Blueprint("studentname", __name__)

@student_name_bp.route('/studentname', methods=['GET'])
def get_student_name():
    student_id = request.args.get('student_id', type=int)
    if not student_id:
        return jsonify({"error": "Student ID is required"}), 400

    try:
        # Fetch the student record
        student = Student.query.get_or_404(student_id)

        # Return the student name
        return jsonify({"student_name": student.name}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
