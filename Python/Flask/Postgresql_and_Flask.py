import psycopg2

con = psycopg2.connect("dbname=Jks_Try1 user=postgres password=Finserv@2023")
cur = con.cursor()
# cur.execute("create table test (id serial primary key, num integer, data varchar);")
# con.commit()

# cur.execute("insert into test (num, data) values (%s, %s)", (100, "abcdef"))
# cur.execute("insert into test (num, data) values (%s, %s)", (110, "gfgdef"))
# con.commit()

# cur.execute("update test set data='chem' where data='abcdef';")
# con.commit()

cur.execute("select * from test;")
print(cur.fetchall())
con.commit()

''' This is how I did flask db init'''

# from flask import *
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Finserv@2023@localhost:5432/Jks_Try1'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

''' Terminal commands: 1)pip3 install flask_migrate
2)export FLASK_APP=Postgresql_and_Flask.py
3) flask --help (chekc for db in the commands in this
4) flask db init'''