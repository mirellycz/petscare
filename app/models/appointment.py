from app import db

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    pet_name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    service_type = db.Column(db.String(100), nullable=False)  # Ex: banho, tosa