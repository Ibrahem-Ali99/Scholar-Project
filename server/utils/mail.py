from flask_mail import Mail, Message

mail = Mail()

from flask_mail import Mail, Message
from flask import current_app

mail = Mail()

def send_reset_email(to_email, reset_token):
    try:
        # Generate the reset URL
        frontend_url = current_app.config.get('FRONTEND_URL', 'http://localhost:5173')
        reset_url = f"{frontend_url}/reset-password/{reset_token}"

        # Email subject and body
        subject = "Password Reset Request"
        body = f"""
        Hello,

        To reset your password, please click the link below:
        {reset_url}

        If you did not request a password reset, please ignore this email.

        Thanks,
        Scholar Team
        """

        msg = Message(subject=subject, recipients=[to_email], body=body)
        mail.send(msg)
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False