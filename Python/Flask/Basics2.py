from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, DateTimeField, RadioField, SelectField, TextAreaField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'

class InfoForm(FlaskForm):
    breed = StringField('What kind of meow meow are you?', validators=[DataRequired()]) 
    #Field is required, can't be empty, so validator DataRequired() is used.
    
    neutered = BooleanField('Have you been neutered?')
    mood = RadioField('Please choose your mood:', choices=[('Happy','Happy'),('Excited','Excited')])
    food_choice = SelectField(u'Pick your favorite food:', choices=[('chicken','Chicken'),('beef','Beef'),('Fish','Fish')])
    feedback = TextAreaField()
    submit = SubmitField('Submit')

@app.route('/', methods=['GET','POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food_choice'] = form.food_choice.data
        session['feedback'] = form.feedback.data

        return redirect(url_for('thankyou'))
    return render_template('Basics2.html', form=form)

@app.route('/thankyou', methods=['GET','POST'])
def thankyou():
    return render_template('thankyou_Basics2.html')
    # Another way to send a variables value to the thank you page is :->
    # return render_template('thankyou_Basics2.html', breed=session['breed'])

if __name__ == '__main__':
    app.run(debug=True)

