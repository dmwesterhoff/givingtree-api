from flask import Flask
from flask_restful import Resource, Api
from models import *

app = Flask(__name__)
api = Api(app)

@api.resource('/status/')
class Status(Resource):
    def get(self):
        return {'status':'true'}

    def delete(self):
        return {'status':'success'}

@api.resource('/user/<int:id>/')
class UserItemViewSet(Resource):
    def get(self, id):
        return {'status':'true',
                'id':id}

@api.resource('/user/')
class UserViewSet(Resource):
    def get(self):
        return {'status':'true'}

    def post(self):
        return

    def delete(self):
        return {'status':'success'}

@api.resource('/address/<int:id>/')
class AddressItemViewSet(Resource):
    def get(self, id):
        return {'status':'true',
                'id':id}

@api.resource('/address/')
class AddressViewSet(Resource):
    def get(self):
        return {'status':'true'}

    def post(self):
        return

    def delete(self):
        return {'status':'success'}

@api.resource('/account/<int:id>/')
class AccountItemViewSet(Resource):
    def get(self, id):
        return {'status':'true',
                'id':id}

@api.resource('/account/')
class AccountViewSet(Resource):
    def get(self):
        return {'status':'true'}

    def post(self):
        return

    def delete(self):
        return {'status':'success'}

@api.resource('/event/<int:id>/')
class EventItemViewSet(Resource):
    def get(self, id):
        return {'status':'true',
                'id':id}

@api.resource('/event/')
class EventViewSet(Resource):
    def get(self):
        return {'status':'true'}

    def post(self):
        return

    def delete(self):
        return {'status':'success'}

@api.resource('/transaction/<int:id>/')
class TransactionItemViewSet(Resource):
    def get(self, id):
        return {'status':'true',
                'id':id}

@api.resource('/transaction/')
class TransactionViewSet(Resource):
    def get(self):
        return {'status':'true'}

    def post(self):
        return

    def delete(self):
        return {'status':'success'}

if __name__ == '__main__':
    app.run(debug=True, host='10.0.0.2')
