from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class CommentForm(FlaskForm):
    title = StringField('Comment title', validators=[Required()])
    comment = TextAreaField('Your comment here', validators=[Required()])
    submit = SubmitField('Post Comment')
    