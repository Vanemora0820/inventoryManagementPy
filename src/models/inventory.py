from datetime import datetime
from config import db

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    quantity = db.Column(db.Integer, nullable=False)
    serial_number = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), default='Disponible')
    product_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
