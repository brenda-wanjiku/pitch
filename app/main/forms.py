from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField,SubmitField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class AddPitch(FlaskForm):
    title = StringField('Title', validators=[Required()])
    content = TextAreaField('Pitch:', validators=[Required()])
    category = SelectField('Category', choices = [('Technology','Technology pitch'),('Philosophy','Philosophy pitch'),('Sports','Sports pitch'),('Alchemy', 'Alchemy pitch')], validators=[Required()])
    submit = SubmitField('Submit')

class AddComment(FlaskForm):
    text = TextAreaField('Leave a comment',validators=[Required()])
    submit = SubmitField('Submit')