from flask_wtf import FlaskForm
# import input type for the form
from wtforms import SelectField, BooleanField, SubmitField, IntegerField, PasswordField, RadioField, StringField
# Importing data validators
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length


class NoviceForm(FlaskForm):  # Create a class inheriting from flask form object
    price = IntegerField('Budget', validators=[
                         DataRequired()])  # Create form inputs
    submit = SubmitField('Find')  # Submit button
    # In select field objects are defined as a tuple of what it is and what will be displayed and specified in choices
    category = SelectField('Category Of laptop')
    
    def __init__(self, category):
        super(NoviceForm, self).__init__()
        self.category.choices = category
        
class ProForm(FlaskForm):  # Create a class inheriting from flask form object
    ram = SelectField('Ram')
    submit = SubmitField('Find')  # Submit button
    # In select field objects are defined as a tuple of what it is and what will be displayed and specified in choices
    cpu = SelectField('CPU')
    hdd = SelectField('Hard Disk')
    gpu = SelectField('Graphics Card')
    motherboard = SelectField('Motherboard')
    powersupply = SelectField('Power Supplies cables')

    def __init__(self, ramchoices, cpuchoices, gpuchoices, powersupplychoices, hddchoices, motherboardchoices):
        super(ProForm, self).__init__()
        self.ram.choices = ramchoices
        self.cpu.choices = cpuchoices
        self.gpu.choices = gpuchoices
        self.hdd.choices = hddchoices
        self.motherboard.choices = motherboardchoices
        self.powersupply.choices = powersupplychoices

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])  # Username
    password = PasswordField('Password', validators=[
                             DataRequired()])  # Password
    # Remember me to maintain session
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


# Feel free to add more fields and expand like first name last name etc but then do edit the html,mongodb, registeration route and userprofile
class RegisterationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    # Email to verify that it is a valid email
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    passwordrep = PasswordField('Repeat Password', validators=[
                                DataRequired(), EqualTo('password')])  # EqualTo makes sure content matches
    submit = SubmitField("Register")


class IndexForm(FlaskForm):
    usertype = RadioField('What Type of user are you?', choices=[
                          ('n', 'Novice'), ('p', 'Pro')])
    submit = SubmitField("Submit")


class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Submit')
