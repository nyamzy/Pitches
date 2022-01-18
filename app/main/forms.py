from tokenize import String
from unittest import TextTestRunner
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class CommentForm(FlaskForm):
    title = StringField('Comment title', validators=[Required()])
    comment = TextAreaField('Your comment here', validators=[Required()])
    submit = SubmitField('Post Comment')
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself', validators=[Required()])
    submit = SubmitField('Submit')
    