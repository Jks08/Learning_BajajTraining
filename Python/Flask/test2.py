from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def landing_page():
    return '<h1> Welcome to the landing page! </h1>'

# Add a user input box and after submitting the name, it should go to the user_latin page.

@app.route('/user_latin/<name>')
def userLatin(name):
    if(name[-1]=='y'):
        username = name[:-1] + 'iful'
    else:
        username = name + 'y'

    return f"<h1> Hello {name}! Your latin name is {username} </h1>"

if __name__=='__main__':
    app.run(debug=True)