# sign up testing
def test_signup_success(client):
    payload = {
        "name": "Test User",
        "email": "testman2@example.com",
        "password": "password123",
        "role": "student"
    }
    response = client.post('/auth/signup', json=payload)
    assert response.status_code == 201
    assert response.json['message'] == "Signup successful"

def test_signup_missing_fields(client):
    payload = {"email": "testman2@example.com", "password": "password123"}
    response = client.post('/auth/signup', json=payload)
    assert response.status_code == 400
    assert "All fields" in response.json['error']


# login testing
def test_login_success(client):
    client.post('/auth/signup', json={
        "name": "Test User",
        "email": "testman2@example.com",
        "password": "password123",
        "role": "student"
    })
    payload = {"email": "testman2@example.com", "password": "password123"}
    response = client.post('/auth/login', json=payload)
    assert response.status_code == 200
    assert response.json['message'] == "Login successful"

def test_login_invalid_credentials(client):
    payload = {"email": "nonexistent@example.com", "password": "wrongpassword"}
    response = client.post('/auth/login', json=payload)
    assert response.status_code == 401
    assert "Invalid email or password" in response.json['error']


# forgot password testing
def test_forgot_password_success(client, mocker):
    mocker.patch("utils.mail.send_reset_email", return_value=True)

    client.post('/auth/signup', json={
        "name": "Reset User",
        "email": "resetuser@example.com",
        "password": "password123",
        "role": "teacher"
    })
    payload = {"email": "resetuser@example.com"}
    response = client.post('/auth/forgot-password', json=payload)
    assert response.status_code == 200
    assert response.json['message'] == "Password reset email sent"

def test_forgot_password_email_not_found(client):
    payload = {"email": "unknown@example.com"}
    response = client.post('/auth/forgot-password', json=payload)
    assert response.status_code == 404
    assert "Email not found" in response.json['error']


# reset password testing
def test_reset_password_success(client, mocker):
    mocker.patch("utils.mail.send_reset_email", return_value=True)
    client.post('/auth/signup', json={
        "name": "Reset User",
        "email": "resetuser@example.com",
        "password": "password123",
        "role": "teacher"
    })

    mock_token = "mocked_token"
    mocker.patch("itsdangerous.URLSafeTimedSerializer.dumps", return_value=mock_token)
    mocker.patch("itsdangerous.URLSafeTimedSerializer.loads", return_value="resetuser@example.com")

    payload = {"new_password": "newpassword123"}
    response = client.post(f'/auth/reset-password/{mock_token}', json=payload)
    assert response.status_code == 200
    assert response.json['message'] == "Password successfully reset"


# logout testing
def test_logout_success(client):
    client.post('/auth/login', json={"email": "testman2@example.com", "password": "password123"})
    response = client.post('/auth/logout')
    assert response.status_code == 200
    assert response.json['message'] == "Logged out successfully"
