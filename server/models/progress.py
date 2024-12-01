import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.db import db

class StudentProgress(db.Model):
    __tablename__ = 'student_progress'
    progress_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), nullable=False)
    assessment_id = db.Column(db.Integer, db.ForeignKey('course_assessment.assessment_id'), nullable=False)
    status = db.Column(db.Enum('pass', 'fail'), nullable=False)
    completion_date = db.Column(db.Date)
    score = db.Column(db.Integer)

class StudentBadge(db.Model):
    __tablename__ = 'student_badge'
    student_badge_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), nullable=False)
    badge_id = db.Column(db.Integer, db.ForeignKey('badge.badge_id'), nullable=False)
    date_awarded = db.Column(db.Date, nullable=False)
