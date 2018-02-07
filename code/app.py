from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegiser
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' # Can be any db, postgres TSQL MSSQL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'yaj' # should be secure
api = Api(app)

@app.before_first_request
def create_tables():
  db.create_all() 

jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(Store, '/store/<name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegiser, '/register')

if __name__ == '__main__': # prevents app.run from running when importing app.py
  from db import db
  db.init_app(app)
  app.run(port=5000, debug=True)