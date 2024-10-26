from flask import Flask
from .models import db  # Make sure your models are imported

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
db.init_app(app)

with app.app_context():
    db.create_all()  # Create tables

from . import routes  # Import routes after creating app context
