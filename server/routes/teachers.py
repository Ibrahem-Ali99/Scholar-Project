from flask import Blueprint, jsonify
from models.user import Teacher

teacher_bp = Blueprint('teacher', __name__)

@teacher_bp.route('/teachers', methods=['GET'])
def get_teachers():
    teachers = Teacher.query.all()
    teachers_list = [
        {
            "teacher_id": teacher.teacher_id,
            "name": teacher.name,
            "designation": teacher.designation,
            "profile_picture": teacher.profile_picture,
            "facebook_url": teacher.facebook_url,
            "twitter_url": teacher.twitter_url,
            "linkedin_url": teacher.linkedin_url,
        }
        for teacher in teachers
    ]
    return jsonify(teachers_list)
