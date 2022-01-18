from tokenize import String
from unittest import TextTestRunner
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import InputRequired

class CommentForm(FlaskForm):
    title = StringField('Comment title', validators=[InputRequired()])
    comment = TextAreaField('Your comment here', validators=[InputRequired()])
    submit = SubmitField('Post Comment')
    
class PitchForm(FlaskForm):
    category = SelectField(label = 'Select category', choices = [("products","products"),("vows","vows"), ("jokes","jokes")])
    text = TextAreaField("Your pitch here", validators=[InputRequired()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself', validators=[InputRequired()])
    submit = SubmitField('Submit')
