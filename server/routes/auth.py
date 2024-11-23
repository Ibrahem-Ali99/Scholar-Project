from flask import Blueprint, request, jsonify, redirect
from utils.db import get_db_connection
from utils.encryption import hash_password, check_password
from requests import get

auth = Blueprint('auth', __name__)



# Replace these with your Google credentials
GOOGLE_CLIENT_ID = "your_google_client_id"
GOOGLE_CLIENT_SECRET = "your_google_client_secret"
GOOGLE_REDIRECT_URI = "http://localhost:5000/auth/google/callback"


# OAuth endpoint
@auth.route('/google')
def google_login():
    google_auth_url = (
        "https://accounts.google.com/o/oauth2/auth"
        f"?client_id={GOOGLE_CLIENT_ID}"
        f"&redirect_uri={GOOGLE_REDIRECT_URI}"
        "&response_type=code"
        "&scope=email profile"
    )
    return redirect(google_auth_url)

# Google OAuth callback
@auth.route('/google/callback')
def google_callback():
    code = request.args.get('code')
    token_url = "https://oauth2.googleapis.com/token"
    token_data = {
        "code": code,
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "redirect_uri": GOOGLE_REDIRECT_URI,
        "grant_type": "authorization_code",
    }

    # Exchange code for access token
    token_response = get(token_url, params=token_data)
    token_json = token_response.json()
    access_token = token_json.get("access_token")

    # Get user info
    user_info_url = "https://www.googleapis.com/oauth2/v2/userinfo"
    user_info_response = get(user_info_url, headers={"Authorization": f"Bearer {access_token}"})
    user_info = user_info_response.json()

    # Extract user data
    email = user_info.get("email")
    name = user_info.get("name")

    # Save user in the database (if not already exists)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Student WHERE email = %s", (email,))
    existing_user = cursor.fetchone()

    if not existing_user:
        cursor.execute("INSERT INTO Student (name, email) VALUES (%s, %s)", (name, email))
        conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "User logged in with Google", "user": user_info})




# SIGNUP Endpoint
@auth.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    user_type = data.get('user_type')  # student or teacher
    email = data.get('email')
    name = data.get('name')
    password = data.get('password')

    if not all([user_type, email, name, password]):
        return jsonify({'message': 'All fields are required'}), 400

    hashed_password = hash_password(password)
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        if user_type == 'student':
            cursor.execute("INSERT INTO Student (name, email, password) VALUES (%s, %s, %s)", (name, email, hashed_password))
        elif user_type == 'teacher':
            cursor.execute("INSERT INTO Teacher (name, email, password) VALUES (%s, %s, %s)", (name, email, hashed_password))
        else:
            return jsonify({'message': 'Invalid user type'}), 400

        conn.commit()
        return jsonify({'message': f'{user_type.capitalize()} account created successfully'}), 201
    except Exception as e:
        conn.rollback()
        return jsonify({'message': str(e)}), 500
    finally:
        cursor.close()
        conn.close()


# LOGIN Endpoint
@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not all([email, password]):
        return jsonify({'message': 'Email and password are required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Check the user in all tables
        cursor.execute(
            """
            SELECT 'student' AS user_type, Student_id AS id, password FROM Student WHERE email = %s
            UNION ALL
            SELECT 'teacher' AS user_type, teacher_id AS id, password FROM Teacher WHERE email = %s
            UNION ALL
            SELECT 'admin' AS user_type, admin_id AS id, password FROM Admin WHERE email = %s
            """,
            (email, email, email)
        )
        user = cursor.fetchone()

        if not user or not check_password(password, user['password']):
            return jsonify({'message': 'Invalid credentials'}), 401

        return jsonify({'message': f"Welcome {user['user_type']}!", 'user_type': user['user_type']}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500
    finally:
        cursor.close()
        conn.close()


# FORGOT PASSWORD Endpoint
@auth.route('/forgot-password', methods=['POST'])
def forgot_password():
    data = request.get_json()
    email = data.get('email')

    if not email:
        return jsonify({'message': 'Email is required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Check if the email exists in any table
        cursor.execute(
            """
            SELECT email FROM Student WHERE email = %s
            UNION ALL
            SELECT email FROM Teacher WHERE email = %s
            """,
            (email, email)
        )
        user = cursor.fetchone()

        if not user:
            return jsonify({'message': 'No account found with this email'}), 404

        # Generate a reset link (placeholder, replace with actual email logic)
        reset_link = f"http://localhost:3000/reset-password?email={email}"
        print(f"Password reset link: {reset_link}")  # Simulate sending an email

        return jsonify({'message': 'Password reset link sent to your email'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500
    finally:
        cursor.close()
        conn.close()
