from authlib.integrations.flask_client import OAuth
from flask_mail import Mail
from flask_cors import CORS

# Flask Extensions
oauth = OAuth()
mail = Mail()
cors = CORS()

# Google OAuth Global Variable
google = None  # Initialize google at the module level

from flask import current_app

def init_extensions(app):
    """
    Initialize all Flask extensions with the given Flask app.
    """
    global google  # Declare google as global to update it inside the function

    with app.app_context():
        print("Current App Name:", current_app.name)
        oauth.init_app(app)
        mail.init_app(app)
        cors.init_app(app)

        # Register Google OAuth
        google = oauth.register(
            name='google',
            client_id=app.config.get('GOOGLE_CLIENT_ID'),
            client_secret=app.config.get('GOOGLE_CLIENT_SECRET'),
            access_token_url='https://accounts.google.com/o/oauth2/token',
            authorize_url='https://accounts.google.com/o/oauth2/auth',
            api_base_url='https://www.googleapis.com/oauth2/v1/',
            client_kwargs={'scope': 'email profile'},
        )

    print("Google OAuth initialized inside app context:", google is not None)
    print("Google OAuth initialized:", google)
