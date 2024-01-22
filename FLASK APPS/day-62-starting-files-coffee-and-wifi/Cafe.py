from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

COFFEE = ['☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕']
WIFI = ['💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪']
POWER = ['🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌']


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    Open = StringField('Opening time e.g. 8AM', validators=[DataRequired()])
    Close = StringField('Closing time e.g. 8PM', validators=[DataRequired()])
    Coffee = SelectField('Coffee rating', choices=COFFEE, validators=[DataRequired()])
    Wifi = SelectField('Wifi strength rating', choices=WIFI, validators=[DataRequired()])
    Power = SelectField('Power socket availability', choices=POWER, validators=[DataRequired()])

    submit = SubmitField('Submit', validators=[DataRequired()])
