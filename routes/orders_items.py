"""
Date: June 19, 2026
orders-items.py
Purpose: Routes for handling order-related operations in the Good Days Coffee application.

"""


from flask import Blueprint, request, render_template, redirect, url_for
from extensions import db
from models.order import Order
from models.menu_items import MenuItem
from models.user import User
from models.favorite_items import FavoriteItem


orders_bp = Blueprint('orders', __name__)



@orders_bp.route('/orders')
def get_all_orders():
    user_id = 1 
    
    order = Order.query.filter_by(user_id=user_id).all()
    
    return render_template('orders.html', orders=order)



@orders_bp.route('/orders/edit/<int:order_id>', methods=['GET', 'POST'])
def edit_order(order_id):
    order = Order.query.get(order_id)
    
    if request.method == 'POST':
        new_quantity = request.form.get('quantity')
        
        # Validate the new quantity items order status
        if order.status in ['pending', 'confirmed']:
            order.quantity = int(new_quantity)
            db.session.commit()
            return redirect(url_for('orders.get_all_orders'))
        else:
            # if the order is not in a state that allows editing, return an error messages
            return "Error: Cannot edit order with status '{}'".format(order.status), 400
    return render_template('edit_order.html', order=order)



# route for updating order status
@orders_bp.route('/orders/update_status/<int:order_id>', methods=['POST'])
def update_order_status(order_id):
    order = Order.query.get(order_id)
    
    new_order_status = request.form.get('status')
    # check if the new order status is valid and if the order is in a state that allows status updates
    if new_order_status in ['pending', 'confirmed', 'canceled', 'completed']:
        # update the new order status
        order.update_status(new_order_status)
        db.session.commit() # commit the changes to the database
        return redirect(url_for('orders.get_all_orders'))
    else:
        return "Error: Invalid order status", 400