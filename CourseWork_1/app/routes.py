from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('base.html')

@main.route('/create')
def create():
    return render_template('create.html')

@main.route('/pending')
def pending():
    return render_template('pending.html')

@main.route('/completed')
def completed():
    return render_template('completed.html')
