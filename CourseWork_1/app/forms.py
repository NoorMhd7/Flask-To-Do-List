from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

class AssessmentForm(FlaskForm):
    title = StringField('Assessment Title', validators=[DataRequired()])
    module_code = StringField('Module Code', validators=[DataRequired()])
    deadline = DateField('Deadline Date', format='%Y-%m-%d', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    status = SelectField('Status', choices=[('pending', 'Pending'), ('completed', 'Completed')], validators=[DataRequired()])
    submit = SubmitField('Create Assessment')
