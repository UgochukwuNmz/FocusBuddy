from flask_wtf import FlaskForm
from wtforms import Form, StringField, IntegerField, PasswordField, BooleanField, validators

class LoginForm(FlaskForm):
    email = StringField('Email Address', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired(), validators.EqualTo('confirm', message = 'Passwords must match')])
    remember = BooleanField('Remember me')
    
class RegisterForm(FlaskForm):
    name = StringField('Name', [validators.DataRequired()])
    email = StringField('Email Address', [validators.DataRequired()])
    password = PasswordField('New Password', [validators.DataRequired(), validators.EqualTo('confirm', message = 'Passwords must match')])
    confirm = PasswordField('Repeat Password')
    major = StringField('Major', [validators.DataRequired()])
    year = IntegerField('Graduating Year', [validators.DataRequired()])
    class1 = StringField('Class')
    class2 = StringField('Class')
    class3 = StringField('Class')
    class4 = StringField('Class')
    class5 = StringField('Class')
    class6 = StringField('Class')
