from flask_wtf import FlaskForm
from wtforms import(StringField,BooleanField,DateTimeField,RadioField,SelectField,TextAreaField,SubmitField,HiddenField)
from wtforms.validators import DataRequired
from logger import logger

class PetAnimalRegistration(FlaskForm):
    name = StringField('Name: ', validators=[DataRequired()])
    age = StringField('Age: ' , validators=[DataRequired()])
    type = StringField('Type: ', validators=[DataRequired()])
    ownerName = StringField('Owner Name: ', validators=[DataRequired()])
    ownerAddress = StringField('Owner Address: ', validators=[DataRequired()])
    submit = SubmitField('Submit')
    logger.info("Registration Form Created")


class PetAnimalUpdate(FlaskForm):
    age = StringField('Age: ' , validators=[DataRequired()])
    type = StringField('Type: ', validators=[DataRequired()])
    ownerName = StringField('Owner Name: ', validators=[DataRequired()])
    ownerAddress = StringField('Owner Address: ', validators=[DataRequired()])
    submit = SubmitField('Submit')
    logger.info("Update Form Created")
