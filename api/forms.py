from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class StudentForm(FlaskForm):
    id = IntegerField("Student ID", validators=[DataRequired()])
    name = StringField("Full Name", validators=[DataRequired()])
    address = StringField("Address", validators=[DataRequired()])
    classroom = StringField("ClassRoom", validators=[DataRequired()])

    submit_btn = SubmitField("Enter")
