from flask import Flask
from .models import db  # Import the database
from .routes import main  # Import your blueprint
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config.from_object('app.config')
    app.config['SECRET_KEY'] = '000' # ChatGPT helped me with this

    db.init_app(app)  # Initialize the database with the app

    with app.app_context():
        db.create_all()  # Create tables if they don't exist

    app.register_blueprint(main)
    migrate = Migrate(app, db)

    return app