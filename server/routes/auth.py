from flask import Blueprint, request, jsonify, session, url_for
from itsdangerous import URLSafeTimedSerializer
from utils.mail import send_reset_email
from utils.db import get_db_connection
import bcrypt
import config
from extensions import google
import logging

# Serializer for creating reset tokens
serializer = URLSafeTimedSerializer(config.SECRET_KEY)

auth = Blueprint('auth', __name__)

ROLE_TABLES = {
    'student': 'Student',
    'teacher': 'Teacher',
    'parent': 'Parent',
    'admin': 'Admin'
}


@auth.route('/signup', methods=['POST'])
def signup():
    data = request.json
    name = data['name']
    email = data['email']
    password = data['password']
    role = data['role'].lower()

    if role not in ROLE_TABLES:
        return jsonify({"error": "Invalid role"}), 400

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        table = ROLE_TABLES[role]
        if role == 'parent':
            student_id = data['student_id']
            cursor.execute(
                f"INSERT INTO {table} (email, password, student_id) VALUES (%s, %s, %s)",
                (email, hashed_password, student_id),
            )
        else:
            cursor.execute(
                f"INSERT INTO {table} (name, email, password) VALUES (%s, %s, %s)",
                (name, email, hashed_password),
            )

        connection.commit()
        return jsonify({"message": "Signup successful"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()

@auth.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    try:
        print(f"Login attempt for email: {email}")

        connection = get_db_connection()
        cursor = connection.cursor()

        # Loop through ROLE_TABLES to find the role by email
        for role, table in ROLE_TABLES.items():
            query = f"SELECT password FROM {table} WHERE email=%s"
            print(f"Executing query: {query}")
            cursor.execute(query, (email,))
            result = cursor.fetchone()

            if result:  # If email is found in this table
                print(f"User found in table: {table}")

                # Check the password
                if bcrypt.checkpw(password.encode('utf-8'), result['password'].encode('utf-8')):
                    session['user'] = email
                    session['role'] = role
                    return jsonify({"message": "Login successful", "role": role}), 200
                else:
                    return jsonify({"error": "Invalid password"}), 401

        # If no role is found for the given email
        return jsonify({"error": "Invalid email or password"}), 401

    except Exception as e:
        print(f"Error during login: {e}")
        return jsonify({"error": str(e)}), 500

    finally:
        connection.close()



@auth.route('/forgot-password', methods=['POST'])
def forgot_password():
    data = request.json
    email = data.get('email')

    # Validate input
    if not email or not isinstance(email, str):
        return jsonify({"error": "Invalid email"}), 400

    try:
        # Connect to the database
        connection = get_db_connection()
        cursor = connection.cursor()

        # Search for the email in all role tables
        found = False
        for role, table in ROLE_TABLES.items():
            cursor.execute(f"SELECT email FROM {table} WHERE email=%s", (email,))
            result = cursor.fetchone()
            if result:
                found = True
                break

        if not found:
            return jsonify({"error": "Email not found"}), 404

        # Generate a password reset token
        reset_token = serializer.dumps(email, salt='password-reset-salt')

        # Send the reset email
        email_sent = send_reset_email(email, reset_token)
        if email_sent:
            return jsonify({"message": "Password reset email sent"}), 200
        else:
            return jsonify({"error": "Failed to send email"}), 500
    except Exception as e:
        logging.error(f"Error in forgot_password: {e}")
        return jsonify({"error": "Internal server error"}), 500
    finally:
        # Ensure the connection is closed
        if 'connection' in locals() and connection:
            connection.close()


@auth.route('/reset-password/<token>', methods=['POST'])
def reset_password(token):
    data = request.json
    new_password = data.get('new_password')

    try:
        # Verify the token
        email = serializer.loads(token, salt='password-reset-salt', max_age=3600)  # Token expires in 1 hour

        connection = get_db_connection()
        cursor = connection.cursor()

        hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
        for role, table in ROLE_TABLES.items():
            cursor.execute(f"UPDATE {table} SET password=%s WHERE email=%s", (hashed_password, email))
            if cursor.rowcount > 0:  # Update successful
                connection.commit()
                return jsonify({"message": "Password successfully reset"}), 200

        return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()


@auth.route('/google-login', methods=['GET'])
def google_login():
    redirect_uri = url_for('auth.google_callback', _external=True)
    return google.authorize_redirect(redirect_uri)

@auth.route('/google/callback', methods=['GET'])
def google_callback():
    try:
        # Retrieve the token and user info from Google
        token = google.authorize_access_token()
        user_info = google.get('userinfo').json()

        email = user_info['email']
        name = user_info.get('name', email.split('@')[0])  
        role = request.args.get('role', 'student').lower()  

        if role not in ROLE_TABLES:
            return jsonify({"error": "Invalid role"}), 400

        # Check if the user already exists in the database
        connection = get_db_connection()
        cursor = connection.cursor()

        table = ROLE_TABLES[role]
        cursor.execute(f"SELECT email FROM {table} WHERE email=%s", (email,))
        result = cursor.fetchone()

        if not result:
            # If the user doesn't exist, sign them up
            cursor.execute(
                f"INSERT INTO {table} (name, email) VALUES (%s, %s)",
                (name, email)
            )
            connection.commit()

        # Log the user in by storing their info in the session
        session['user'] = email
        session['role'] = role

        return jsonify({"message": "Google login/signup successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()

@auth.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({"message": "Logged out successfully"}), 200