# src/models/inventory.py
from src.main import db

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    serial_number = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), default='Pending')
