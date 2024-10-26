from flask import Blueprint, render_template, redirect, url_for, flash, request
from .models import db, Assessment  
from datetime import datetime


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
        
        # Convert the deadline input to a datetime object
        deadline_str = request.form['deadline']
        deadline = datetime.strptime(deadline_str, '%Y-%m-%d')
        
        description = request.form['description']
        status = request.form['status']
        
        # Create a new assessment object with the datetime-converted deadline
        new_assessment = Assessment(title=title, module_code=module_code, 
                                    deadline=deadline, description=description, 
                                    status=status)
        db.session.add(new_assessment)
        db.session.commit()
        return redirect(url_for('main.home'))

    return render_template('create.html')  # Render the form template
@main.route('/pending')
def pending():
    # Fetch pending assessments from the database
    pending_assessments = Assessment.query.filter_by(status='pending').all()
    return render_template('pending.html', assessments=pending_assessments)  # Create a separate template for pending assessments

@main.route('/completed')
def completed():
    completed_assessments = Assessment.query.filter_by(status='completed').all()
    return render_template('completed.html', assessments=completed_assessments)  # Create a separate template for completed assessments

@main.route('/update_status/<int:assessment_id>', methods=['POST'])
def update_status(assessment_id):
    # Update logic here
    assessment = Assessment.query.get(assessment_id)
    if assessment and assessment.status == 'pending':
        assessment.status = 'completed'
        db.session.commit()
        flash("Assessment marked as completed!", "success")
    else:
        flash("Assessment not found or already completed.", "error")
    
    return redirect(url_for('main.pending'))


@main.route('/delete/<int:id>', methods=['POST'])
def delete_task(id):
    task_to_delete = Assessment.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        flash("Task deleted successfully!", "success")
    except Exception as e:
        db.session.rollback()
        flash("There was an issue deleting the task.", "danger")
    return redirect(url_for('main.home'))