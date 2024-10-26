from flask import Blueprint, render_template, request, redirect, url_for
from .models import db, Assessment  # Use relative import


main = Blueprint('main', __name__)

@main.route('/')
def home():
    assessments = Assessment.query.all()
    return render_template('base.html', assessments=assessments)

@main.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        module_code = request.form['module_code']
        deadline = request.form['deadline']
        description = request.form['description']
        status = request.form['status']
        
        new_assessment = Assessment(title=title, module_code=module_code, 
                                    deadline=deadline, description=description, 
                                    status=status)
        db.session.add(new_assessment)
        db.session.commit()
        return redirect(url_for('main.home'))

    return render_template('create.html')  # Create a separate template for the form

@main.route('/pending')
def pending():
    # Fetch pending assessments from the database
    pending_assessments = Assessment.query.filter_by(status='pending').all()
    return render_template('pending.html', assessments=pending_assessments)  # Create a separate template for pending assessments

@main.route('/completed')
def completed():
    completed_assessments = Assessment.query.filter_by(status='completed').all()
    return render_template('completed.html', assessments=completed_assessments)  # Create a separate template for completed assessments