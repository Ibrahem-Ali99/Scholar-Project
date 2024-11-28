from flask import Blueprint, request, jsonify, session, url_for
from itsdangerous import URLSafeTimedSerializer
from utils.mail import send_reset_email
from utils.db import db
import bcrypt
from extensions import google
from models.user import Student, Teacher, Parent, Admin  # Import models
import logging

auth = Blueprint('auth', __name__)

# Define role models for querying
ROLE_MODELS = {
    'student': Student,
    'teacher': Teacher,
    'parent': Parent,
    'admin': Admin
}

# Configure a serializer for secure token generation
serializer = URLSafeTimedSerializer("YOUR_SECRET_KEY")

# sign up endpoint
# sign up endpoint
@auth.route('/signup', methods=['POST'])
def signup():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    role = data.get('role', '').lower()

    if role not in ROLE_MODELS:
        return jsonify({"error": "Invalid role"}), 400

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    try:
        # Determine the role and create an instance
        if role == 'parent':
            student_id = data.get('student_id')
            if not student_id:
                return jsonify({"error": "Student ID is required for parent signup"}), 400
            new_user = Parent(email=email, password=hashed_password, student_id=student_id)
        else:
            new_user = ROLE_MODELS[role](name=name, email=email, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "Signup successful", "user_id": new_user.student_id}), 201
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
        # Search the database for the user based on the role
        user = None
        role = None
        user = Student.query.filter_by(email=email).first()
        if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            role = 'student'
        if not user:
            user = Teacher.query.filter_by(email=email).first()
            if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                role = 'teacher'
        if not user:
            user = Parent.query.filter_by(email=email).first()
            if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                role = 'parent'
        if not user:
            user = Admin.query.filter_by(email=email).first()
            if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                role = 'admin'

        if not user or not role:
            return jsonify({"error": "Invalid email or password"}), 401

        print(f"User found: {email}, Role: {role}")

        # Store user session
        session['user'] = email
        session['role'] = role

        # Return the response with the user's role
        return jsonify({"message": "Login successful", "role": role}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# forget password endpoint
@auth.route('/forgot-password', methods=['POST'])
def forgot_password():
    data = request.json
    email = data.get('email')

    if not email or not isinstance(email, str):
        return jsonify({"error": "Invalid email"}), 400

    try:
        # Search for the email in all role models
        found = False
        for model in ROLE_MODELS.values():
            user = model.query.filter_by(email=email).first()
            if user:
                found = True
                break

        if not found:
            logging.info(f"Email not found: {email}")
            return jsonify({"error": "Email not found"}), 404

        # Generate a password reset token
        reset_token = serializer.dumps(email, salt='password-reset-salt')

        # Send the reset email
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
        email = serializer.loads(token, salt='password-reset-salt', max_age=3600)  # Token expires in 1 hour

        hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())

        # Update password in the appropriate role model
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


# Google authentication
# Google OAuth login endpoint
@auth.route('/google-login', methods=['GET'])
def google_login():
    if google is None:
        return jsonify({"error": "Google OAuth is not initialized"}), 500

    redirect_uri = url_for('auth.google_callback', _external=True)
    try:
        return google.authorize_redirect(redirect_uri)
    except Exception as e:
        return jsonify({"error": "Google OAuth redirect failed", "message": str(e)}), 500


@auth.route('/google/callback', methods=['GET'])
def google_callback():
    try:
        # Retrieve the token and user info from Google
        token = google.authorize_access_token()
        user_info = google.get('userinfo').json()

        email = user_info['email']
        name = user_info['name']

        # Try to find the user based on the email
        user = Student.query.filter_by(email=email).first() or \
               Teacher.query.filter_by(email=email).first() or \
               Parent.query.filter_by(email=email).first() or \
               Admin.query.filter_by(email=email).first()

        if user:
            role = user.__class__.__name__.lower()
            session['user'] = email
            session['role'] = role

            # Return a response with the user's role
            return jsonify({"message": "Login successful", "role": role, "redirect": f'/{role}-dashboard'}), 200
        else:
            return jsonify({"error": "User not found in database"}), 404

    except Exception as e:
        logging.exception("Error during Google OAuth callback")
        return jsonify({"error": "Internal server error", "message": str(e)}), 500


# logoiut
@auth.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({"message": "Logged out successfully"}), 200
