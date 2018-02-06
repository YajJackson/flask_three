from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegiser(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('username', type=str, required=True, help='Username field cannot be left blank')
  parser.add_argument('password', type=str, required=True, help='Password field cannot be left blank')

  def post(self):
    data = UserRegiser.parser.parse_args()

    if UserModel.find_by_username(data['username']):
      return {'message': 'A user with that username already exists'}, 400
      
    UserModel(**data).save_to_db()

    return {'message': 'User created successfully.'}, 201