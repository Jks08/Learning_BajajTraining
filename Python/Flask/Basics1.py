# Basic html template rendering in Flask

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
# wtforms and wtf in flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

class TestForm(FlaskForm):
    cat_breed = StringField('Enter your cat breed: ')
    submit = SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():
    cat_breed = False
    form = TestForm()

    if(form.validate_on_submit()):
        cat_breed = form.cat_breed.data
        form.cat_breed.data = ''

    return render_template('catBreed.html', cat_breed=cat_breed, form=form)

if __name__ == '__main__':
    app.run(debug=True)