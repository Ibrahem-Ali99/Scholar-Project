from flask import Flask
from flask_cors import CORS
from utils.db import db
from routes.courses import course_bp
from config import Config

app = Flask(__name__)

# Configuration
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
CORS(app)  # Enable Cross-Origin Resource Sharing for frontend-backend communication

# Register Blueprints
app.register_blueprint(course_bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Ensure tables are created
    app.run(debug=True)
