""" 
Date: June 19, 2026
order.py
Purpose: Model for handling order-related operations in the Good Days Coffee application.

"""


from flask_sqlalchemy import SQLAlchemy
from extensions import db





class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    menu_item_id = db.Column(db.Integer, db.ForeignKey('menu_item.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    status = db.Column(db.String(20), nullable=False, default='pending')
    
    user = db.relationship('User', backref=db.backref('orders', lazy=True))
    menu_item = db.relationship('MenuItem', backref=db.backref('orders', lazy=True))
    
    def __repr__(self):
        return f'<Order User: {self.user.username}, MenuItem: {self.menu_item.name}, Quantity: {self.quantity}, Status: {self.status}>'
    
    def total_price(self):
        return self.menu_item.price * self.quantity
    
    def update_status(self, new_status):
        self.status = new_status
        db.session.commit()
        return self.status
    
    
    def cancel_order(self):
        if self.status in ['pending', 'confirmed']:
            self.status = 'canceled'
            db.session.commit()
            return True
        return False
    
    def complete_order(self):
        if self.status == 'confirmed':
            self.status = 'completed'
            db.session.commit()
            return True
        return False
    
    
    def is_active(self):
        return self.status in ['pending', 'confirmed']
    
    def is_canceled(self):
        return self.status == 'canceled'
    
    def is_completed(self):
        return self.status == 'completed'
    
    
    def delete_order(self):
        db.session.delete(self)
        db.session.commit()
        
        

    
    

    
    