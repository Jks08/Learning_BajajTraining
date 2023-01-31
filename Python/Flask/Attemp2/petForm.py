from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, DateTimeField, RadioField, SelectField, TextAreaField
from wtforms.validators import DataRequired

class PetAnimalRegistration(FlaskForm):
    name = StringField('Name: ', validators=[DataRequired()])
    age = StringField('Age: ' , validators=[DataRequired()])
    type = StringField('Type: ', validators=[DataRequired()])
    ownerName = StringField('Owner Name: ', validators=[DataRequired()])
    ownerAddress = StringField('Owner Address: ', validators=[DataRequired()])
    submit = SubmitField('Submit')

class PetAnimalUpdate(FlaskForm):
    age = StringField('Age: ' , validators=[DataRequired()])
    type = StringField('Type: ', validators=[DataRequired()])
    ownerName = StringField('Owner Name: ', validators=[DataRequired()])
    ownerAddress = StringField('Owner Address: ', validators=[DataRequired()])
    submit = SubmitField('Submit')