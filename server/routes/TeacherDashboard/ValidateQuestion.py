from flask import Blueprint, request, jsonify
from models import Quiz, Course
from utils.db  import singleton_db
from utils.role_access import role_required
db = singleton_db.get_db
validate_quiz_creation_bp = Blueprint('validate_quiz_creation_bp', __name__)

@validate_quiz_creation_bp.route('/course/validate/<int:course_id>', methods=['GET'])
@role_required(['teacher', 'admin'])
def validate_course(course_id):
    course = Course.query.get(course_id)
    if not course:
        return jsonify({"error": "Invalid Course ID"}), 400
    return jsonify({"message": "Valid Course ID"}), 200

@validate_quiz_creation_bp.route('/quiz/create', methods=['POST'])
@role_required(['teacher', 'admin'])
def create_quiz():
    data = request.get_json()
    if not Course.query.get(data.get('course_id')):
        return jsonify({"error": "Invalid Course ID"}), 400

    quiz = Quiz(**data)
    db.session.add(quiz)
    db.session.commit()
    return jsonify({"message": "Quiz created successfully!"}), 201
