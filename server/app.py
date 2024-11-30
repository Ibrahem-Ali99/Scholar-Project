from flask import Flask
from flask_cors import CORS
from utils.db import db, init_db
from extensions import init_extensions
from routes.courses import course_bp
from routes.teachers import teacher_bp
from routes.feedback import feedback_bp
from routes.auth import auth
import os

# Import configuration classes
from config import DevelopmentConfig, ProductionConfig, Config

# Create Flask app
app = Flask(__name__)

# Load the appropriate configuration
if os.getenv("FLASK_ENV") == "production":
    app.config.from_object(ProductionConfig)
elif os.getenv("FLASK_ENV") == "development":
    app.config.from_object(DevelopmentConfig)
else:
    app.config.from_object(Config)

# Initialize extensions
init_extensions(app)  # Initialize other extensions (OAuth, JWT, Mail, CORS)
CORS(app)  # Ensure CORS is enabled
init_db(app)  # Initialize SQLAlchemy

# Register blueprints
app.register_blueprint(course_bp)
app.register_blueprint(teacher_bp)
app.register_blueprint(feedback_bp)  # Feedback route from the main branch
app.register_blueprint(auth, url_prefix='/auth')  # Auth route from your branch

# Ensure tables are created if needed
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=app.config.get('DEBUG', True))
