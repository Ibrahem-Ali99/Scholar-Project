import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.db import db

COURSE_FOREIGN_KEY = 'course.course_id'  

class Course(db.Model):
    __tablename__ = 'course'
    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(100), nullable=False)
    course_description = db.Column(db.Text)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.teacher_id'))
    price = db.Column(db.Float, nullable=False)  
    image_url = db.Column(db.String(255), nullable=False) 
    
    # Relationships
    enrollments = db.relationship('Enrollment', backref='course', lazy=True)
    contents = db.relationship('CourseContent', backref='course', lazy=True)
    assessments = db.relationship('CourseAssessment', backref='course', lazy=True)
    ratings = db.relationship('CourseRating', back_populates='course', lazy=True)  
    
class CourseContent(db.Model):
    __tablename__ = 'course_content'
    content_id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey(COURSE_FOREIGN_KEY), nullable=False)  
    title = db.Column(db.String(100), nullable=False)
    content_type = db.Column(db.String(50), nullable=False)
    post_date = db.Column(db.Date, nullable=False)

class CourseAssessment(db.Model):
    __tablename__ = 'course_assessment'
    assessment_id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey(COURSE_FOREIGN_KEY), nullable=False)  
    title = db.Column(db.String(100), nullable=False)
    max_score = db.Column(db.Integer, nullable=False)
    post_date = db.Column(db.Date, nullable=False)
    deadline = db.Column(db.Date, nullable=False)

class CourseRating(db.Model):
    __tablename__ = 'course_rating'
    rating_id = db.Column(db.Integer, primary_key=True)
    rated_by = db.Column(db.Integer, db.ForeignKey('student.student_id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey(COURSE_FOREIGN_KEY), nullable=False)  
    rating = db.Column(db.Integer, nullable=False)
    feedback = db.Column(db.Text)
    
    student = db.relationship('Student', backref='course_ratings', lazy=True)
    course = db.relationship('Course', back_populates='ratings', lazy=True)
