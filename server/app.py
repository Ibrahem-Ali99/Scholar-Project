from flask import Flask
from utils.db import init_db
from extensions import init_extensions
from routes.courses import course_bp
from routes.teachers import teacher_bp
import os

# Import configuration classes
from config import DevelopmentConfig, ProductionConfig

# Create Flask app
app = Flask(__name__)

# Load the appropriate configuration
if os.getenv("FLASK_ENV") == "production":
    app.config.from_object(ProductionConfig)
else:
    app.config.from_object(DevelopmentConfig)


# Initialize extensions
init_extensions(app)  # Initialize other extensions (OAuth, JWT, Mail, CORS)
init_db(app)  # Initialize SQLAlchemy

from routes.auth import auth

# Register blueprints
app.register_blueprint(course_bp)
app.register_blueprint(teacher_bp)
app.register_blueprint(auth, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
