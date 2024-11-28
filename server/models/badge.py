from utils.db import db

class Badge(db.Model):
    __tablename__ = 'badge'
    badge_id = db.Column(db.Integer, primary_key=True)
    badge_name = db.Column(db.String(100), nullable=False)
    badge_description = db.Column(db.Text)