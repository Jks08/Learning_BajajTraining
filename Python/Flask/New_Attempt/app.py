from flask import *
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, DateTimeField, RadioField, SelectField, TextAreaField
from wtforms.validators import DataRequired
import psycopg2

app = Flask(__name__)
app.config['SECRET_KEY']='secretKey1'

con = psycopg2.connect("dbname=Jks_Try1 user=postgres password=Finserv@2023")
cur = con.cursor()

class PetAnimalRegistration(FlaskForm):
    name = StringField('Name: ', validators=[DataRequired()])
    age = StringField('Age: ' , validators=[DataRequired()])
    type = StringField('Type: ', validators=[DataRequired()])
    ownerName = StringField('Owner Name: ', validators=[DataRequired()])
    ownerAddress = StringField('Owner Address: ', validators=[DataRequired()])
    submit = SubmitField('Submit')

class PetAnimalUpdate(FlaskForm):
    age = StringField('Age: ' , validators=[DataRequired()])
    type = StringField('Type: ', validators=[DataRequired()])
    ownerName = StringField('Owner Name: ', validators=[DataRequired()])
    ownerAddress = StringField('Owner Address: ', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('homepage.html')

@app.route('/index',methods=['GET','POST'])
def index():
    form = PetAnimalRegistration()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['age'] = form.age.data
        session['type'] = form.type.data
        session['ownerName'] = form.ownerName.data
        session['ownerAddress'] = form.ownerAddress.data
        cur.execute("INSERT INTO pet_regs (name,age,type,ownerName,ownerAddress) VALUES (%s,%s,%s,%s,%s)",(session['name'],session['age'],session['type'],session['ownerName'],session['ownerAddress']))
        con.commit()
        return redirect(url_for('view'))
    return render_template('index.html',form=form)

@app.route('/view',methods=['GET','POST'])
def view():
    cur.execute("SELECT * FROM pet_regs")
    data = cur.fetchall()
    return render_template('view.html',data=data)

def delete_data(name):
    cur.execute("DELETE FROM pet_regs WHERE name=%s",(name,))
    con.commit()


def update_data(name,age,type,ownerName,ownerAddress):
    cur.execute("UPDATE pet_regs SET age=%s,type=%s,ownerName=%s,ownerAddress=%s WHERE name=%s",(age,type,ownerName,ownerAddress,name))
    con.commit()

@app.route('/delete/<name>')
def delete(name):
    delete_data(name)
    return redirect(url_for('view'))

@app.route('/update/<name>',methods=['GET','POST'])
def update(name):
    form = PetAnimalUpdate()
    if form.validate_on_submit():
        age = form.age.data
        type = form.type.data
        ownerName = form.ownerName.data
        ownerAddress = form.ownerAddress.data
        update_data(name,age,type,ownerName,ownerAddress)
        return redirect(url_for('view'))
    return render_template('update.html',form=form)

if __name__=='__main__':
    app.run(debug=True)