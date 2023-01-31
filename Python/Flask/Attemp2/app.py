from flask import *
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, DateTimeField, RadioField, SelectField, TextAreaField
from wtforms.validators import DataRequired
import psycopg2
from petForm import PetAnimalRegistration, PetAnimalUpdate
from petConn import *


app = Flask(__name__)
app.config['SECRET_KEY']='someRandomSecretKey'

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/index',methods=['GET','POST'])
def index():
    DBConn.connect()
    DBConn.create_table()
    form = PetAnimalRegistration()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['age'] = form.age.data
        session['type'] = form.type.data
        session['ownerName'] = form.ownerName.data
        session['ownerAddress'] = form.ownerAddress.data
        # DBConn.insert_data(session['name'],session['age'],session['type'],session['ownerName'],session['ownerAddress'])
        DBConn.insert_data(form.name.data,form.age.data,form.type.data,form.ownerName.data,form.ownerAddress.data)
        DBConn.close()
        return redirect(url_for('view'))
    return render_template('index.html',form=form)

@app.route('/view',methods=['GET','POST'])
def view():
    DBConn.connect()
    data = DBConn.view_data()   
    DBConn.close()
    return render_template('view.html',data=data)

@app.route('/update/<name>',methods=['GET','POST'])
def update(name):
    DBConn.connect()
    form = PetAnimalUpdate()
    if form.validate_on_submit():
        session['age'] = form.age.data
        session['type'] = form.type.data
        session['ownerName'] = form.ownerName.data
        session['ownerAddress'] = form.ownerAddress.data
        DBConn.update_data(session['name'],form.age.data,form.type.data,form.ownerName.data,form.ownerAddress.data)
        DBConn.close()
        return redirect(url_for('view'))
    return render_template('update.html',form=form)

@app.route('/delete/<name>')
def delete(name):
    DBConn.connect()
    DBConn.delete_data(name)
    DBConn.close()
    return redirect(url_for('view'))

if __name__ == '__main__':
    app.run(debug=True)