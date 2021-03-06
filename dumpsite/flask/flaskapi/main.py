from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {
            'hello': 'world'
        }

class Book(Resource):
    def get(self):
        return {
            'books': ['Hello', 'Book'] 
        }

api.add_resource(HelloWorld, '/')
api.add_resource(Book, '/book')
