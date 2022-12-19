import os

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField
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

class BudgetForm(FlaskForm):
    set_budget = FloatField(label='Budget', validators=[DataRequired()])    
    submit = SubmitField(label='Set Budget')

class ExpensesForm(FlaskForm):
    name = StringField(label='Name',validators=[DataRequired()])
    expense = FloatField(label='Expense', validators=[DataRequired()])
    submit = SubmitField(label='Submit')
    delete = SubmitField(label='Delete')    