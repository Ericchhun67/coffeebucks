from flask_sqlalchemy import SQLAlchemy
from extensions import db


class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    description = db.Column(db.String(500), nullable=True)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)  # e.g., 'Coffee', 'Tea', 'Pastry'
    
    def __repr__(self):
        return f'<MenuItem {self.name}>'
    