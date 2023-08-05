from bson import ObjectId
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
from marshmallow import Schema, fields, ValidationError

app = Flask("__name__")
api = Api(app)

client = MongoClient('localhost', 27017)
db = client.User
collections = db.User_data

# This class is help to ensure required fields are given by the user
class requreFields(Schema):
    name = fields.String(required=True)
    email = fields.String(required=True)
    password = fields.String(required=True)

# Here we make an instance of class requreFields
fields = requreFields()


class UsersResource(Resource):
    # Get all users
    def get(self):
        users = list(collections.find())
        for user in users:
            user['_id'] = str(user['_id'])

        if not users:
            return {"message": "No users are available."}, 404

        return users, 200

    # Add new user
    def post(self):
        try:
            data = fields.load(request.get_json())
        except ValidationError as e:
            error = e.normalized_messages()
            return {"errors": error}, 400
        
        collections.insert_one(data)
        return {"message": "Successfully added"}, 201


class UserResource(Resource):

    # Get Specific single user
    def get(self, id):
        if not ObjectId.is_valid(id):
            return {"message": "Invalid ID"}, 400

        user = collections.find_one({'_id': ObjectId(id)})
        if not user:
            return {"message": "User not found"}, 404

        user['_id'] = str(user['_id'])
        return user, 200

    # Update the specific user
    def put(self, id):
        if not ObjectId.is_valid(id):
            return {"message": "Invalid ID"}, 400

        data = request.get_json()
        collections.update_one({'_id': ObjectId(id)}, {'$set': data})
        return {"message": "Successfully updated"}, 200

    # Delete Specific user
    def delete(self, id):
        if not ObjectId.is_valid(id):
            return {"message": "Invalid ID"}, 400
        collections.delete_one({'_id': ObjectId(id)})
        return {"message": "Successfully deleted"}, 200

# Endpoints
api.add_resource(UsersResource, '/users')
api.add_resource(UserResource, '/users/<string:id>')


if __name__ == "__main__":
    app.run(debug=True)
