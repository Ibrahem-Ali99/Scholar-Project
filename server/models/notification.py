from utils.db import db

class Notification(db.Model):
    __tablename__ = 'notification'
    notification_id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

class StudentNotification(db.Model):
    __tablename__ = 'student_notification'
    student_notification_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), nullable=False)
    notification_id = db.Column(db.Integer, db.ForeignKey('notification.notification_id'), nullable=False)
    is_pushed = db.Column(db.Boolean, default=False)
