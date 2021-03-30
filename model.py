from wtforms import Form, BooleanField, StringField, PasswordField, validators
from flask_wtf import FlaskForm

class RegistrationForm(FlaskForm):
    fname = StringField('first_name', [validators.Length(min=4, max=25,message="First Name be between 4 and 25 characters")])
    lname = StringField('last_name', [validators.Length(min=4, max=25,message="Last Name be between 4 and 25 characters")])
    email = StringField('email', [validators.Length(min=6, max=35,message="Email be between 6 and 35 characters")])
    password = PasswordField('password', [validators.DataRequired(),validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('confirm')
class UserLoginForm(FlaskForm):
    username=StringField('Username')
    password= PasswordField('password')