from flask import *
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, DateTimeField, RadioField, SelectField, TextAreaField
from wtforms.validators import DataRequired
import psycopg2

app = Flask(__name__)
app.config['SECRET_KEY']='secretKey2'

class DBconn:
    con = psycopg2.connect("dbname=Jks_Try1 user=postgres password=Finserv@2023")
    cur = con.cursor()
    
    @classmethod
    def disp(cls):
        cls.cur.execute("SELECT * FROM pet_regs")
        rows = cls.cur.fetchall()
        return rows

# class DBConnection:
#     conn = psycopg2.connect("dbname=Jks_try1 user=postgres password=Finserv@2023")
#     cur = conn.cursor

#     def __init__(cls):
#         pass

#     @classmethod
#     def insert_data(cls,name,age,type,ownerName,ownerAddress):
#         cls.cur.execute("INSERT INTO pet_regs (name,age,type,ownerName,ownerAddress) VALUES (%s,%s,%s,%s,%s)",(name,age,type,ownerName,ownerAddress))
#         cls.conn.commit()

#     @classmethod
#     def view_data(cls):
#         cls.cur.execute("SELECT * FROM pet_regs")
#         rows = cls.cur.fetchall()
#         return rows

#     @classmethod
#     def delete_data(cls,name):
#         cls.cur.execute("DELETE FROM pet_regs WHERE name=%s",(name,))
#         cls.conn.commit()

#     @classmethod
#     def update_data(cls,name,age,type,ownerName,ownerAddress):
#         cls.cur.execute("UPDATE pet_regs SET age=%s,type=%s,ownerName=%s,ownerAddress=%s WHERE name=%s",(age,type,ownerName,ownerAddress,name))
#         cls.conn.commit()

# class PetAnimalRegistration(FlaskForm):
#     name = StringField('Name: ', validators=[DataRequired()])
#     age = StringField('Age: ' , validators=[DataRequired()])
#     type = StringField('Type: ', validators=[DataRequired()])
#     ownerName = StringField('Owner Name: ', validators=[DataRequired()])
#     ownerAddress = StringField('Owner Address: ', validators=[DataRequired()])
#     submit = SubmitField('Submit')

# class PetAnimalUpdate(FlaskForm):
#     age = StringField('Age: ' , validators=[DataRequired()])
#     type = StringField('Type: ', validators=[DataRequired()])
#     ownerName = StringField('Owner Name: ', validators=[DataRequired()])
#     ownerAddress = StringField('Owner Address: ', validators=[DataRequired()])
#     submit = SubmitField('Submit')

# @app.route('/',methods=['GET','POST'])
# def home():
#     return render_template('homepage.html')

# @app.route('/index',methods=['GET','POST'])
# def index():
#     form = PetAnimalRegistration()
#     if form.validate_on_submit():
#         session['name'] = form.name.data
#         session['age'] = form.age.data
#         session['type'] = form.type.data
#         session['ownerName'] = form.ownerName.data
#         session['ownerAddress'] = form.ownerAddress.data
#         val = (session['name'],session['age'],session['type'],session['ownerName'],session['ownerAddress'])
#         DBConnection.insert_data(val)
        
#         return redirect(url_for('view'))
#     return render_template('index.html',form=form)

# @app.route('/view',methods=['GET','POST'])
# def view():
#     data = DBConnection.view_data()
#     return render_template('view.html',data=data)

# def delete_data(name):
#     DBConnection.delete_data(session['name'])

# def update_data(name,age,type,ownerName,ownerAddress):
#     DBConnection.update_data(name,age,type,ownerName,ownerAddress)

# @app.route('/delete/<name>')
# def delete(name):
#     delete_data(name)
#     return redirect(url_for('view'))

# @app.route('/update/<name>',methods=['GET','POST'])
# def update(name):
#     form = PetAnimalUpdate()
#     if form.validate_on_submit():
#         age = form.age.data
#         type = form.type.data
#         ownerName = form.ownerName.data
#         ownerAddress = form.ownerAddress.data
#         update_data(name,age,type,ownerName,ownerAddress)
#         return redirect(url_for('view'))
#     return render_template('update.html',form=form)

# if __name__=='__main__':
#     DBConnection.get_connection()
#     app.run(debug=True)