from flask_wtf import FlaskForm 
from wtforms import SelectField, BooleanField, SubmitField, IntegerField, PasswordField, StringField #import input type for the form
from wtforms.validators import DataRequired, Email,EqualTo, ValidationError, Length # Importing data validators

class NoviceForm(FlaskForm): # Create a class inheriting from flask form object
    price = IntegerField('Budget', validators=[DataRequired()]) # Create form inputs
    submit = SubmitField('Find') # Submit button
    #In select field objects are defined as a tuple of what it is and what will be displayed and specified in choices
    category = SelectField(u'Category Of laptop', choices=[('all', 'All'),('gaming', 'Gaming'), ('office','Office'), ('internet', 'Internet')])

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()]) #Username 
    password = PasswordField('Password', validators=[DataRequired()]) #Password
    remember_me = BooleanField('Remember Me') #Remember me to maintain session
    submit = SubmitField('Sign In')

class RegisterationForm(FlaskForm): #Feel free to add more fields and expand like first name last name etc but then do edit the html,mongodb, registeration route and userprofile
    username = StringField("Username", validators=[DataRequired()])  
    email = StringField('Email',validators=[DataRequired(),Email()]) #Email to verify that it is a valid email
    password = PasswordField('Password',validators=[DataRequired()])
    passwordrep = PasswordField('Repeat Password',validators=[DataRequired(),EqualTo('password')]) #EqualTo makes sure content matches
    submit = SubmitField("Register")
    
class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Submit')
