import os
from flask import Flask
from flask_cors import CORS
from flask_mail import Mail
from utils.db import db
from routes.LandingPageCourses import course_bp
from routes.teachers import teacher_bp
from routes.feedback import feedback_bp
from config import Config, ProductionConfig, DevelopmentConfig
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables from .env
load_dotenv()

# Load the appropriate configuration
if os.getenv("FLASK_ENV") == "production":
    app.config.from_object(ProductionConfig)
elif os.getenv("FLASK_ENV") == "development":
    app.config.from_object(DevelopmentConfig)
else:
    app.config.from_object(Config)

# Set up Google OAuth credentials from environment variables
app.config['GOOGLE_CLIENT_ID'] = os.getenv('GOOGLE_CLIENT_ID')
app.config['GOOGLE_CLIENT_SECRET'] = os.getenv('GOOGLE_CLIENT_SECRET')

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = Config.MAIL_USERNAME
app.config['MAIL_PASSWORD'] = Config.MAIL_PASSWORD
app.config['MAIL_DEFAULT_SENDER'] = Config.MAIL_DEFAULT_SENDER
app.config['FRONTEND_URL'] = os.getenv("FRONTEND_URL")

# Initialize extensions
CORS(app)  # Ensure CORS is enabled
mail = Mail(app)  # Initialize Flask-Mail
db.init_app(app)  # Initialize SQLAlchemy

# Register blueprints
app.register_blueprint(course_bp)
app.register_blueprint(teacher_bp)
app.register_blueprint(feedback_bp)



if __name__ == "__main__":
    app.run(debug=True)
