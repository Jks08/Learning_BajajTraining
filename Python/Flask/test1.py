from flask import Flask, request
import pdb
from translate import Translator

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1> Hello User! Welcome to the landing page. </h1>' #Jinja2 will be used to render HTML. It understands HTML tags.

@app.route('/index')
def index():
    browser_info = request.headers.get('User-Agent')
    return '<h2> Your browser is %s </h2>' % browser_info

@app.route('/info')
def info():
    return ('<h2> This is the info page </h2>')

@app.route('/user/<name>')
def add(name):
    # pdb.set_trace()
    return f'<h1> This is the page of {name.upper()[-1]}. Our Lord and Saviour! </h1> <hr> <h1> Welcome to the page of {name.upper()} and forever be grateful for its existence!</h1>'  

@app.route('/userLatin/<name>')
def userLatin(name):
    if(name[-1]=='y'):
        username = name[:-1] + 'iful'
    else:
        username = name + 'y'

    return f"<h1> Hello {name}! Your latin name is {username} </h1>"



if __name__=='__main__':
    app.run(debug=True)   