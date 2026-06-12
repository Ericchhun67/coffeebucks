from flask import Blueprint, render_template
from extensions import db
from models.menu_items import MenuItem
from models.favorite_items import FavoriteItem

favorite_bp = Blueprint('favorite', __name__)




@favorite_bp.route('/favorites')
def favorites():
    # For demonstration, we'll assume the user is logged in and has an ID of 1
    user_id = 1  # In a real application, you would get this from the session or authentication system
    
    # Fetch the user's favorite items from the database
    favorite_items = FavoriteItem.query.filter_by(user_id=user_id).all()
    
    # Extract the menu items from the favorite items
    menu_items = [favorite.menu_item for favorite in favorite_items]
    
    return render_template('favorites.html', menu_items=menu_items)


@favorite_bp.route('/favorites/add/<int:menu_item_id>')
def add_favorite(menu_item_id):
    user_id = 1  # In a real application, you would get this from the session or authentication system
    
    # Check if the menu item exists
    menu_item = MenuItem.query.get(menu_item_id)
    if not menu_item:
        return "Menu item not found", 404
    
    # Check if the favorite already exists
    existing_favorite = FavoriteItem.query.filter_by(user_id=user_id, menu_item_id=menu_item_id).first()
    if existing_favorite:
        return "Item already in favorites", 400
    
    # Add the menu item to the user's favorites
    new_favorite = FavoriteItem(user_id=user_id, menu_item_id=menu_item_id)
    db.session.add(new_favorite)
    db.session.commit()
    
    return "Item added to favorites", 200


@favorite_bp.route('/favorites/remove/<int:menu_item_id>')
def remove_favorite(menu_item_id):
    user_id = 1  # In a real application, you would get this from the session or authentication system
    
    # Check if the favorite exists
    favorite = FavoriteItem.query.filter_by(user_id=user_id, menu_item_id=menu_item_id).first()
    if not favorite:
        return "Favorite item not found", 404
    
    # Remove the menu item from the user's favorites
    db.session.delete(favorite)
    db.session.commit()
    
    return "Item removed from favorites", 200