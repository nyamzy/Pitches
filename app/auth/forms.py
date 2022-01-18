from ast import Pass, Str
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Email, EqualTo
from ..models import User

class RegistrationForm(FlaskForm):
    email = StringField('Your email address', validators=[InputRequired(), Email()])
    username = StringField('Enter username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired(), EqualTo('password_confirm', message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm password', validators=[InputRequired()])
    submit = SubmitField('Sign up')


class LoginForm(FlaskForm):
    email = StringField('Your email address', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')

