from flask import Flask
from flask_cors import CORS
from utils.db import db
from routes.LandingPageCourses import landing_course_bp
from routes.teachers import teacher_bp  
from routes.feedback import feedback_bp  
from config import Config
from routes.auth import auth
from flask_mail import Mail
from routes.dashboard import dashboard_bp
from routes.courses import course_bp
from routes.student import student_bp
from routes.dashHome import dash_home_bp
from routes.course_list import course_list_bp
from flask_swagger_ui import get_swaggerui_blueprint
from routes.coursepage import course_page

app = Flask(__name__)

app.config.from_object(Config)
SWAGGER_URL = '/api/docs'
API_URL = '/static/SCHOLAR.postman_collection.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Test application"
    },
)

CORS(app)  
mail = Mail(app)  
db.init_app(app)  
app.register_blueprint(landing_course_bp)
app.register_blueprint(course_bp)
app.register_blueprint(teacher_bp) 
app.register_blueprint(feedback_bp) 
app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(dashboard_bp)
app.register_blueprint(student_bp)
app.register_blueprint(swaggerui_blueprint)
app.register_blueprint(dash_home_bp, url_prefix='/api') 
app.register_blueprint(course_list_bp, url_prefix='') 
app.register_blueprint(course_page)

@app.route('/')
def main_page():
    return "<h1>This is the main page of the server</h1>"

if __name__ == "__main__":
    app.run(debug=True)
