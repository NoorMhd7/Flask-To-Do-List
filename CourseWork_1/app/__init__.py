from flask import Flask
from .models import db  # Ensure this import is correct
from .routes import main

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Change to your DB
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()  # Creates database tables

    app.register_blueprint(main)


    return app