from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.fields.html5 import DateField #Special, will allow user to pick date from calender
from wtforms.validators import DataRequired, EqualTo, ValidationError

from .models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username): #This method is automatically called on_validate()
        user = User.query.filter_by(username=username.data).first()
        if user is not None: #so if it exists
            raise ValidationError("That username already exists, try a different one.")
        

class EventForm(FlaskForm):
    event_name = StringField("Event Name", validators=[DataRequired()])
    event_description = TextAreaField("Event description")
    event_date = DateField("Event Date", validators=[DataRequired()])
    submit = SubmitField('Create!')
