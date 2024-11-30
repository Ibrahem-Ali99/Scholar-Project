from flask import Flask
from flask_cors import CORS
from utils.db import db
from routes.LandingPageCourses import course_bp
from routes.teachers import teacher_bp  
from routes.feedback import feedback_bp  
from config import Config
from routes.DisplayStudentName import student_bp 
app = Flask(__name__)

# Configuration
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
CORS(app)  # Enable Cross-Origin Resource Sharing for frontend-backend communication

# Register Blueprints
app.register_blueprint(course_bp)
app.register_blueprint(teacher_bp)  # Register the teacher blueprint
app.register_blueprint(feedback_bp)  # Register the feedback blueprint
app.register_blueprint(student_bp)
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Ensure tables are created
    app.run(debug=True)
