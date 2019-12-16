from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class StringScoreForm(FlaskForm):
    applicant_name = StringField('Applicant Name', validators=[DataRequired()])
    pan_name = StringField('PAN Name', validators=[DataRequired()])
    submit = SubmitField('Get Score')
