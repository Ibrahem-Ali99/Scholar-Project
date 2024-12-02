from utils.db import db

class BaseUser(db.Model):
    __abstract__ = True
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(100), nullable=False)  

class Student(BaseUser):
    __tablename__ = 'student'
    student_id = db.Column(db.Integer, primary_key=True)

    # Relationships
    enrollments = db.relationship('Enrollment', backref='student', lazy=True)
    payments = db.relationship('Payment', backref='student', lazy=True)
    badges = db.relationship('StudentBadge', backref='student', lazy=True)

class Teacher(BaseUser):
    __tablename__ = 'teacher'
    teacher_id = db.Column(db.Integer, primary_key=True)
    profile_picture = db.Column(db.String(255))  
    designation = db.Column(db.String(100))     
    facebook_url = db.Column(db.String(255))   
    twitter_url = db.Column(db.String(255))    
    linkedin_url = db.Column(db.String(255))    

    # Relationships
    courses = db.relationship('Course', backref='teacher', lazy=True)

class Parent(BaseUser):
    __tablename__ = 'parent'
    parent_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'))

    # Relationships
    student = db.relationship('Student', backref=db.backref('parents', lazy=True))

class Admin(BaseUser):
    __tablename__ = 'admin'
    admin_id = db.Column(db.Integer, primary_key=True)
