import os
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


app = Flask(__name__)

app.config.from_object(Config)

CORS(app)  
mail = Mail(app)  
db.init_app(app)  

app.register_blueprint(course_bp)
app.register_blueprint(teacher_bp)  
app.register_blueprint(feedback_bp) 
app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(course_page)


if __name__ == "__main__":
    app.run(debug=True)
