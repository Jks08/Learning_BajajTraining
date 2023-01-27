from flask import Flask, request, render_template, url_for
import pdb
from translate import Translator
import string
import random

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

@app.route('/url_shortener', methods=['GET', 'POST'])
def url_shortener():
    l1 = []
    l2 = []
    if request.method == 'POST':
        req = request.form['url']
        url = "https://"+func_to_shorten_url(req)+".com"
        return f'<a href="{req}"> {url} </a>'
    #     l1.append(req)
    #     l2.append(url)
    #     d = dict(zip(l1, l2))
    #     print(d)

    # for i,j in d.items():
    #     if i == req:
    #         return f'<a href="{req}"> {d[i]} </a>'
    #     else:
    #         return f'<a href="{req}"> {url} </a>'


    return '''<form method="POST">
                URL: <input type="text" name="url">
                <input type="submit" value="Submit">
            </form>'''


def func_to_shorten_url(url):
    s = list(string.ascii_letters)
    s1 = list(string.digits)
    random.shuffle(s)
    random.shuffle(s1)
    s3 = s + s1
    short_url = ''.join(s[1])+ ''.join(s3[1:5])
    return short_url

if __name__=='__main__':
    app.run(debug=True)   