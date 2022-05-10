from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class CommentsForm(FlaskForm):


    comments = TextAreaField('Movie review', validators=[Required()])
    submit = SubmitField('Submit')