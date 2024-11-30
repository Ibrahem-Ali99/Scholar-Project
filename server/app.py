from flask import Flask
from flask_cors import CORS
from utils.db import db, init_db
from routes.LandingPageCourses import course_bp
from routes.teachers import teacher_bp  
from routes.feedback import feedback_bp  
from config import Config, ProductionConfig, DevelopmentConfig
import os
from routes.auth import auth

app = Flask(__name__)

# Load the appropriate configuration
if os.getenv("FLASK_ENV") == "production":
    app.config.from_object(ProductionConfig)
elif os.getenv("FLASK_ENV") == "development":
    app.config.from_object(DevelopmentConfig)
else:
    app.config.from_object(Config)

from dotenv import load_dotenv
load_dotenv()
app.config['GOOGLE_CLIENT_ID'] = os.getenv('GOOGLE_CLIENT_ID')
app.config['GOOGLE_CLIENT_SECRET'] = os.getenv('GOOGLE_CLIENT_SECRET')
 
 
CORS(app)  # Ensure CORS is enabled
init_db(app)  # Initialize SQLAlchemy

from flask_mail import Mail

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  
app.config['MAIL_PORT'] = 587  
app.config['MAIL_USE_TLS'] = True  
app.config['MAIL_USE_SSL'] = False  
app.config['MAIL_USERNAME'] =   Config.MAIL_USERNAME
app.config['MAIL_PASSWORD'] = Config.MAIL_PASSWORD
app.config['MAIL_DEFAULT_SENDER'] = Config.MAIL_DEFAULT_SENDER
app.config['FRONTEND_URL'] = os.getenv("FRONTEND_URL") 

mail = Mail(app)


# Register blueprints
app.register_blueprint(course_bp)
app.register_blueprint(teacher_bp)  # Register the teacher blueprint
app.register_blueprint(feedback_bp)  # Register the feedback blueprint
app.register_blueprint(auth, url_prefix="/auth")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Ensure tables are created
    app.run(debug=True)
