from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, StringField, validators
from wtforms.validators import DataRequired
import email_validator

class Users(FlaskForm):
    email = StringField('Email', validators=[validators.Length(min=8, max=120), validators.Email()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Login', validators=[DataRequired()])