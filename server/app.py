import os
from flask import Flask
from flask_cors import CORS
from utils.db import db
from routes.LandingPageCourses import course_bp
from routes.teachers import teacher_bp  
from routes.feedback import feedback_bp  
from config import Config, ProductionConfig, DevelopmentConfig
import os
from routes.auth import auth
from flask_mail import Mail
from dotenv import load_dotenv
from routes.courses import course_bp
from routes.student import student_bp


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

CORS(app)  
mail = Mail(app)  
db.init_app(app) 

app.register_blueprint(course_bp)
app.register_blueprint(teacher_bp) 
app.register_blueprint(feedback_bp) 
app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(student_bp) 

@app.route('/')
def main_page():
    return "<h1>This is the main page of the server</h1>"

if __name__ == "__main__":
    app.run(debug=True)
