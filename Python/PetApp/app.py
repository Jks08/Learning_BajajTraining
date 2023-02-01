from flask import *
from wtforms import StringField, SubmitField, BooleanField, DateTimeField, RadioField, SelectField, TextAreaField
from wtforms.validators import DataRequired
from petConn import *
from petForm import PetAnimalRegistration, PetAnimalUpdate
from config import Config
from logger import logger

app = Flask(__name__)
app.config['SECRET_KEY']=Config().secret()

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/view',methods=['GET','POST'])
def view():
    DBconnect.connect()
    data = DBconnect.disp()
    DBconnect.close()
    return render_template('view.html',data=data)

@app.route('/delete/<name>',methods=['GET','POST'])
def delete(name):
    DBconnect.connect()
    DBconnect.delete(name)
    DBconnect.close()
    return redirect(url_for('view'))

@app.route('/update/<name>',methods=['GET','POST'])
def update(name):
    form = PetAnimalUpdate()
    if form.validate_on_submit():
        DBconnect.connect()
        DBconnect.update(name,form.age.data,form.type.data,form.ownerName.data,form.ownerAddress.data)
        DBconnect.close()
        return redirect(url_for('view'))
    return render_template('update.html',form=form)

@app.route('/index',methods=['GET','POST'])
def index1():
    form = PetAnimalRegistration()
    if form.validate_on_submit():
        DBconnect.connect()
        DBconnect.insert(form.name.data,form.age.data,form.type.data,form.ownerName.data,form.ownerAddress.data)
        DBconnect.close()
        return redirect(url_for('view'))
    return render_template('index.html',form=form)
    

if __name__ == '__main__':
    logger.info("App started")
    app.run(debug=True)
    # Get logger info from the app.py file and store them in a log file
    logger.info("App ended")
