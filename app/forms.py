from flask_wtf import FlaskForm
from wtforms import SelectField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class NoviceForm(FlaskForm):
    price = IntegerField('Budget', validators=[DataRequired()])
    submit = SubmitField('Find')
    category = SelectField(u'Category Of laptop', choices=[('all', 'All'),('gaming', 'Gaming'), ('office','Office'), ('internet', 'Internet')])
