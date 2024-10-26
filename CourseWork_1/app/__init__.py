from flask import Flask
from .models import db  # Import the database
from .routes import main  # Import your blueprint

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Set database URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking for performance
    app.config['SECRET_KEY'] = '000'

    db.init_app(app)  # Initialize the database with the app

    with app.app_context():
        db.create_all()  # Create tables if they don't exist

    app.register_blueprint(main)  # Register blueprint for routes

    return app
