from flask import Flask, request
from flask_restful import Resource, Api
from user import *

db.create_all()

users = [User(1, 'bob', 'pass'), User(2,'Abhay','pass')]
user_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = user_table.get(username, None)
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)