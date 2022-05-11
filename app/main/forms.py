from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError
from flask_login import current_user

class PitchForm(FlaskForm):
  
    content = TextAreaField('Content',validators=[DataRequired()])

    category = SelectField('Category', choices=[('General', 'General'),('Business','Business'),('Career','Career')],validators=[DataRequired()])

    submit = SubmitField('SubmitPitch')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    
    comment = TextAreaField('Comments...',validators=[DataRequired()])
    submit = SubmitField('comment')