import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.db import db
# models/hiring_request.py
class HiringRequest(db.Model):
    __tablename__ = 'hiring_request'
    request_id = db.Column(db.Integer, primary_key=True)  # Changed from Request_id
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.teacher_id'), nullable=False)  # Changed from Teacher_id
    status = db.Column(db.Enum('pending', 'approved', 'rejected'), nullable=False)
    request_date = db.Column(db.Date, nullable=False)
    reviewed_by = db.Column(db.Integer, db.ForeignKey('admin.admin_id'))
    reviewed_date = db.Column(db.Date)