""" 
Date: June-7-2026
Purpose: the user.py
users model database table for the login and registration system of the 
Good Days coffee website.

"""

from flask_sqlalchemy import SQLAlchemy
from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

# User model for the database, representing users of the website
class User(db.Model):
    # id: unique identifier for each user, primary key in the database
    id = db.Column(db.Integer, primary_key=True)
    # Username: unique username for each user, cannot be null
    username = db.Column(db.String(150), unique=True, nullable=False)
    # Email: unique email address for each user, cannot be null
    email = db.Column(db.String(150), unique=True, nullable=False)
    # Password: hashed password for each user, cannot be null
    password = db.Column(db.String(256), nullable=False)
    
    

    def __repr__(self):
        return f'<User {self.username}>'
    

    def user_info(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }
        
    def set_password(self, password):
        self.password = generate_password_hash(password)
        
        
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
        
    
