from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from extensions import db
from routes.auth import auth_bp
from routes.pages import pages_bp
from routes.menu_page import menu_bp
from routes.favorite_item_page import favorite_bp

app = Flask(__name__)
app.config.from_object(Config)


def create_app():
    db.init_app(app)
    
    app.register_blueprint(pages_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(menu_bp)
    app.register_blueprint(favorite_bp)

    
    with app.app_context():
        from models.user import User
        from models.menu_items import MenuItem
        db.create_all()
        
        
    
    return app



if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)