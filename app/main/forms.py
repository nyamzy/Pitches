from tokenize import String
from unittest import TextTestRunner
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired

class CommentForm(FlaskForm):
    title = StringField('Comment title', validators=[InputRequired()])
    comment = TextAreaField('Your comment here', validators=[InputRequired()])
    submit = SubmitField('Post Comment')
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself', validators=[InputRequired()])
    submit = SubmitField('Submit')
