



class Config:
    # Configuration settings for the flask application
    SECRET_KEY = 'your_secret_key_here' # Secret key for session management and security
    SQLALCHEMY_DATABASE_URI = 'sqlite:///coffeebucks.db' # Database URI for SQLAlchemy, 
    # using SQLite for simplicity
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Disable SQLAlchemy event system to save 
    #resources and avoid warnings
    
class developmentConfig(Config):
    # Development-specific configuration settings
    DEBUG = True # Enable debug mode for development, provides detailed error pages 
    # and auto-reloading of the server on code changes




    
    