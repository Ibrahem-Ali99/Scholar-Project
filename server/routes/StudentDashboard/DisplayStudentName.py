from flask import Blueprint, jsonify, request
from models import Student
from sqlalchemy.exc import SQLAlchemyError

student_name_bp = Blueprint("studentname", __name__)

@student_name_bp.route('/studentname', methods=['GET'])
def get_student_name():
    student_id = request.args.get('student_id', type=int)
    if not student_id:
        return jsonify({"error": "Student ID is required"}), 400

    try:
        if not Student.query.session:
            raise SQLAlchemyError("Database connection is not active.")

        student = Student.query.get(student_id)
        if not student:
            return jsonify({"error": "Not Found"}), 404

        return jsonify({"student_name": student.name}), 200

    except SQLAlchemyError as db_err:
        print(f"Database Error: {db_err}")
        return jsonify({"error": "Database connection error"}), 500

    except Exception as e:
        print(f"Unhandled Exception: {e}")
        return jsonify({"error": f"Internal Server Error: {str(e)}"}), 500
