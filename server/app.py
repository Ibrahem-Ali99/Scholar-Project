from flask import Flask
from flask_cors import CORS
from utils.db import db
from routes.LandingPageCourses import course_bp
from routes.teachers import teacher_bp  
from routes.feedback import feedback_bp  
from config import Config
from routes.auth import auth
from flask_mail import Mail
from routes.CoursePage import course_page
from routes.student import student_bp
from routes.dashboard import dashboard_bp

app = Flask(__name__)

app.config.from_object(Config)

CORS(app)  
mail = Mail(app)  
db.init_app(app)  

app.register_blueprint(course_bp)
app.register_blueprint(teacher_bp) 
app.register_blueprint(feedback_bp) 
app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(student_bp) 
app.register_blueprint(dashboard_bp)
app.register_blueprint(course_page)

@app.route('/')
def main_page():
    return "<h1>This is the main page of the server</h1>"

if __name__ == "__main__":
    app.run(debug=True)
