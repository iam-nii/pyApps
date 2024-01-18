from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, EmailField

class Users(FlaskForm):
    email = EmailField('something@email.com')
    password = PasswordField('password')