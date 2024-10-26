from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Assessment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    module_code = db.Column(db.String(20), nullable=False)
    deadline = db.Column(db.DateTime, nullable=False)  # Ensure this is defined
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(10), nullable=False)

    def __init__(self, title, module_code, deadline, description, status):
        self.title = title
        self.module_code = module_code
        self.deadline = deadline
        self.description = description
        self.status = status
