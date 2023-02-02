from flask_restful import Resource, Api
from flask import Flask
from secure_check import authenticate, identity
from flask_jwt import JWT, jwt_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'
api = Api(app)
jwt = JWT(app, authenticate, identity)

cats = []

class HomePage(Resource):
    def get(self):
        return 'Homepage'

class CatNames(Resource):
    def get(self,name):
        print(cats)
        for cat in cats:
            if cat.get('name') == name:
                return cat
        return {name:'not found'},404
    
    @jwt_required()
    def post(self,name):
        cat = {'name':name}
        cats.append(cat)
        print(cats)
        return cat

    def delete(self,name):
        for index,cat in enumerate(cats):
            if cat.get('name') == name:
                deleted_cat = cats.pop(index)
                return {'note':'delete success', 'deleted_cat':deleted_cat}
        return {name:'not found, so cannot delete'}

class AllNames(Resource):
    @jwt_required()
    def get(self):
        return {'cats':cats}

api.add_resource(HomePage, '/')
api.add_resource(CatNames, '/cat/<string:name>')
api.add_resource(AllNames, '/cats')

if __name__ == '__main__':
    app.run(debug=True) # If we put host = 0.0.0.0 then we can access this from other machines on the network.