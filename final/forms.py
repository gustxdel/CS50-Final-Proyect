import os

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField(label='Username',validators=[DataRequired(),Length(min=3,max=20)])
    password = PasswordField(label='Password',validators=[DataRequired(),Length(min=8,max=16)])
    confirm_password = PasswordField(label='Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField(label='Sign Up')
    
class LoginForm(FlaskForm):
    username = StringField(label='Username',validators=[DataRequired(),Length(min=3,max=20)])
    password = PasswordField(label='Password',validators=[DataRequired(),Length(min=8,max=16)])
    submit = SubmitField(label='Log In')