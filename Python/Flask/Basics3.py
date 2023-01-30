from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, DateTimeField, RadioField, SelectField, TextAreaField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

class SimpleForm(FlaskForm):
    submit = SubmitField('Click Me!')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SimpleForm()
    if form.validate_on_submit():
        flash(f"Thank you for your submission!")
        return redirect(url_for('index'))
    return render_template('home3.html', form=form)

# @app.route('/Basics3', methods=['GET', 'POST'])
# def Basics3():
#     return "This Works fine. Just lie your life."

if __name__ == '__main__':
    app.run(debug=True)