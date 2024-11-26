from utils.db import db

class BaseUser(db.Model):
    __abstract__ = True
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

class Student(BaseUser):
    __tablename__ = 'student'
    student_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # Relationships
    enrollments = db.relationship('Enrollment', backref='student', lazy=True) #lazy=True is a shorthand for lazy='select' and it means "Load the related data only when it is accessed"
    payments = db.relationship('Payment', backref='student', lazy=True)
    badges = db.relationship('StudentBadge', backref='student', lazy=True)

class Teacher(BaseUser):
    __tablename__ = 'teacher'
    teacher_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # Relationships
    courses = db.relationship('Course', backref='teacher', lazy=True)

class Parent(BaseUser):
    __tablename__ = 'parent'
    parent_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'))

class Admin(BaseUser):
    __tablename__ = 'admin'
    admin_id = db.Column(db.Integer, primary_key=True)
