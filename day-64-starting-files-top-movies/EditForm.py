# Create the WTForm
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


class EditForm(FlaskForm):
    Rating = StringField('Your rating out of 10 e.g. 3.2', validators=[DataRequired()])
    Review = StringField('Your review', validators=[DataRequired()])

    edit = SubmitField('Done')