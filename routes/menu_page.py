from flask import Blueprint, render_template
from extensions import db
from models.menu_items import MenuItem

menu_bp = Blueprint('menu', __name__)

@menu_bp.route('/menu')
def menu():
    # Fetch all menu items from the database
    menu_items = MenuItem.query.all()
    return render_template('menu.html', menu_items=menu_items)