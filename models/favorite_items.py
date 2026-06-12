from flask_sqlalchemy import SQLAlchemy
from extensions import db









class FavoriteItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    menu_item_id = db.Column(db.Integer, db.ForeignKey('menu_item.id'), nullable=False)
    
    user = db.relationship('User', backref=db.backref('favorite_items', lazy=True))
    menu_item = db.relationship('MenuItem', backref=db.backref('favorited_by', lazy=True))
    
    def __repr__(self):
        return f'<FavoriteItem User: {self.user.username}, MenuItem: {self.menu_item.name}>'
    

