# Basic html template rendering in Flask

from flask import Flask, render_template
from flask_wtf import FlaskForm

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Basic1.html')

# wtforms and wtf in flask

if __name__ == '__main__':
    app.run(debug=True)