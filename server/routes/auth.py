from flask import Blueprint, request, jsonify, session, url_for, redirect
from itsdangerous import URLSafeTimedSerializer
from utils.mail import send_reset_email
from utils.db import db
import bcrypt
from models.user import Student, Teacher, Parent, Admin  
import logging
import config


auth = Blueprint('auth', __name__)

ROLE_MODELS = {
    'student': Student,
    'teacher': Teacher,
    'parent': Parent,
    'admin': Admin
}

# serializer for secure token generation
serializer = URLSafeTimedSerializer(config.Config.SECRET_KEY)

# sign up endpoint
@auth.route('/signup', methods=['POST'])
def signup():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    role = data.get('role', '').lower()

    if role == 'teacher':
        existing_teacher = Teacher.query.filter_by(email=email).first()
        if existing_teacher:
            return jsonify({"error": "Email is already taken by another teacher"}), 400
    elif role == 'student':
        existing_student = Student.query.filter_by(email=email).first()
        if existing_student:
            return jsonify({"error": "Email is already taken by another student"}), 400
    elif role == 'parent':
        existing_parent = Parent.query.filter_by(email=email).first()
        if existing_parent:
            return jsonify({"error": "Email is already taken by another parent"}), 400

    try:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        if role == 'parent':
            student_id = data.get('studentId')
            if not student_id:
                return jsonify({"error": "Student ID is required for parent signup"}), 400
            new_user = Parent(name=name,email=email, password=hashed_password, student_id=student_id)
        else:
            new_user = ROLE_MODELS[role](name=name, email=email, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        user_id = None
        if role == 'parent':
            user_id = new_user.parent_id 
        elif role == 'teacher':
            user_id = new_user.teacher_id
        elif role == 'student':
            user_id = new_user.student_id

        return jsonify({"message": "Signup successful", "user_id": user_id}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500



# login endpoint
@auth.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    try:
        user = None
        role = None
        user_roles = {
            'student': Student,
            'teacher': Teacher,
            'parent': Parent,
            'admin': Admin
        }

        for r, model in user_roles.items():
            user = model.query.filter_by(email=email).first()
            if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                role = r
                break

        if not user or not role:
            return jsonify({"error": "Invalid email or password"}), 401

        # store user session
        session['user'] = email
        session['role'] = role
        session['id'] = user.id
        return jsonify({"message": "Login successful", "role": role}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# forgot password endpoint
@auth.route('/forgot-password', methods=['POST'])
def forgot_password():
    data = request.json
    email = data.get('email')

    if not email or not isinstance(email, str):
        return jsonify({"error": "Invalid email"}), 400

    try:
        found = False
        for model in ROLE_MODELS.values():
            user = model.query.filter_by(email=email).first()
            if user:
                found = True
                break

        if not found:
            logging.info(f"Email not found: {email}")
            return jsonify({"error": "Email not found"}), 404

        # generate a password reset token
        reset_token = serializer.dumps(email, salt='password-reset-salt')

        email_sent = send_reset_email(email, reset_token)
        if email_sent:
            logging.info(f"Password reset email sent to: {email}")
            return jsonify({"message": "Password reset email sent"}), 200
        else:
            logging.error(f"Failed to send password reset email to: {email}")
            return jsonify({"error": "Failed to send email"}), 500

    except Exception as e:
        logging.exception("Error in forgot_password route")
        return jsonify({"error": "Internal server error"}), 500
    
 
# reset password endpoint
@auth.route('/reset-password/<token>', methods=['POST'])
def reset_password(token):
    data = request.json
    new_password = data.get('new_password')

    try:
        # Verify the token
        email = serializer.loads(token, salt='password-reset-salt', max_age=3600)  # 3600 -> 1 hour
        hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())

        for model in ROLE_MODELS.values():
            user = model.query.filter_by(email=email).first()
            if user:
                user.password = hashed_password.decode('utf-8')
                db.session.commit()
                return jsonify({"message": "Password successfully reset"}), 200

        return jsonify({"error": "User not found"}), 404
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500   
    
# logoiut
@auth.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({"message": "Logged out successfully"}), 200
