from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegiser
from item import Item, ItemList

app = Flask(__name__)
app.secret_key = 'yaj' # should be secure
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(Item, '/item/<name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegiser, '/register')

if __name__ == '__main__': # prevents app.run from running when importing app.py
  app.run(port=5000, debug=True)