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
    
    if request.referrer and request.referrer.endswith(url_for('main.home')):
        return redirect(url_for('main.home'))
    else:
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
    if request.referrer and request.referrer.endswith(url_for('main.home')):
        return redirect(url_for('main.home'))
    elif request.referrer and request.referrer.endswith(url_for('main.completed')):
        return redirect(url_for('main.completed'))
    else:
        return redirect(url_for('main.completed'))

@main.route('/unfinish_status/<int:assessment_id>', methods=['POST'])
def unfinish_status(assessment_id):
    # Update logic here
    assessment = Assessment.query.get(assessment_id)
    if assessment and assessment.status == 'completed':
        assessment.status = 'pending'
        db.session.commit()
        flash("Assessment marked as pending!", "success")
    else:
        flash("Assessment not found or already in pending.", "error")
    
    if request.referrer and request.referrer.endswith(url_for('main.home')):
        return redirect(url_for('main.home'))
    else:
        return redirect(url_for('main.completed'))
    
@main.route('/edit_assessment/<int:assessment_id>', methods=['GET', 'POST'])
def edit_assessment(assessment_id):
    # Retrieve the assessment by ID
    assessment = Assessment.query.get_or_404(assessment_id)
    
    if request.method == 'POST':
        # Get updated data from the form
        assessment.title = request.form['title']
        assessment.module_code = request.form['module_code']
        assessment.description = request.form['description']
        
        # Parse and update the deadline
        try:
            assessment.deadline = datetime.strptime(request.form['deadline'], '%Y-%m-%d')
        except ValueError:
            flash("Invalid date format. Please use YYYY-MM-DD.", "error")
            return render_template('edit_assessment.html', assessment=assessment)
        
        # Commit changes to the database
        db.session.commit()
        flash("Assessment updated successfully!", "success")
        return redirect(url_for('main.home'))  # Or wherever you want to redirect after edit

    # Render the edit form with current data
    return render_template('edit_assessment.html', assessment=assessment)