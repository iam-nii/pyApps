# Create the WTForm
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, FloatField
from wtforms.validators import DataRequired

class AddForm(FlaskForm):
    title = StringField("Title:", validators=[DataRequired()])
    year = StringField("Year:", validators=[DataRequired()])
    description = StringField("Description:", validators=[DataRequired()])
    rating = FloatField("Rating:", validators=[DataRequired()])
    ranking = IntegerField("Ranking:", validators=[DataRequired()])
    review = StringField("Review:", validators=[DataRequired()])
    img_url = StringField("Image link", validators=[DataRequired()])