from flask import Blueprint, jsonify, request, session
from models import StudentQuizProgress, Quiz, Student
from utils.role_access import role_required

student_progress_bp = Blueprint("student_progress", __name__)

@student_progress_bp.route('/student/progress', methods=['GET'])
@role_required(["student", "admin", "parent"])
def get_student_progress():
    student_id = request.args.get('student_id', type=int)

    if not student_id:
        return jsonify({"error": "Student ID is required"}), 400

    try:
        if session.get("role") == "student":
            if session.get("user_id") != student_id:
                return jsonify({"error": "Unauthorized access"}), 403

        elif session.get("role") == "parent":
            parent_id = session.get("user_id")
            child = Student.query.filter_by(student_id=student_id, parent_id=parent_id).first()
            if not child:
                return jsonify({"error": "Unauthorized access: This student is not your child"}), 403

        progress = StudentQuizProgress.query.filter_by(student_id=student_id).all()
        if not progress:
            return jsonify({"progress": []}), 200
        quiz_ids = [entry.quiz_id for entry in progress]
        quizzes = Quiz.query.filter(Quiz.quiz_id.in_(quiz_ids)).all()
        quiz_map = {quiz.quiz_id: quiz for quiz in quizzes}

        progress_data = [
            {
                "quiz_title": quiz_map[entry.quiz_id].title if entry.quiz_id in quiz_map else "N/A",
                "current_score": entry.current_score,
                "max_score": quiz_map[entry.quiz_id].max_score if entry.quiz_id in quiz_map else "N/A",
                "status": entry.status,
                "completion_date": entry.completion_date.isoformat() if entry.completion_date else "N/A",
            }
            for entry in progress
        ]

        return jsonify({"progress": progress_data}), 200

    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500
