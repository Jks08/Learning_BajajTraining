import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
app.app_context().push()
Migrate(app, db)

#Above code is same for all ORM use cases (subject to changes in requirements). Django has built in ORM, but not Flask. Thus we have to build our own ORM.

class Pet(db.Model):
    __tablename__ = 'pets'
    pet_id = db.Column(db.Integer, primary_key=True)
    pet_breed = db.Column(db.Text)
    pet_name = db.Column(db.Text)
    pet_owner = db.Column(db.Text)
    pet_age = db.Column(db.Integer)

    def __init__(self, breed, name, owner, age):
        self.pet_breed = breed
        self.pet_name = name
        self.pet_owner = owner
        self.pet_age = age

    def __repr__(self):
        return f"{self.pet_name} is a {self.pet_breed} and is {self.pet_age} years old. The owner is {self.pet_owner}."


# db.create_all()

my_pet = Pet('TRex', 'Barbie', 'Adam', 2)
db.session.add(my_pet)
db.session.commit()

all_pets = Pet.query.all()
print(all_pets)
