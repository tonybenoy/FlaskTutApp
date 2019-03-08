from flask_wtf import FlaskForm 
from wtforms import SelectField, BooleanField, SubmitField, IntegerField #import input type for the form
from wtforms.validators import DataRequired # Makes the input compulsory

class NoviceForm(FlaskForm): # Create a class inheriting from flask form object
    price = IntegerField('Budget', validators=[DataRequired()]) # Create form inputs
    submit = SubmitField('Find') # Submit button
    #In select field objects are defined as a tuple of what it is and what will be displayed and specified in choices
    category = SelectField(u'Category Of laptop', choices=[('all', 'All'),('gaming', 'Gaming'), ('office','Office'), ('internet', 'Internet')])
