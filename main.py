from bson import ObjectId
from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask("__name__")

client = MongoClient('localhost', 27017)

db = client.User
collections = db.User_data


# Get or Create Users data
@app.route("/users", methods=['GET','POST'])
def getUsers():
    if(request.method == 'GET'):
        users = list(collections.find())
        for user in users:
            user['_id'] = str(user['_id'])
        if(len(users) == 0):
            return jsonify(
                {
                    "message":"No users are available."
                }
            )
        return jsonify(users)
    
    elif(request.method == 'POST'):
        fields={'name':False, 'email':False, 'password':False}
        requreFields = ""
        data = request.get_json()
        for field in fields.keys():
            if(data.__contains__(field)):
                fields[field] = True
            else:
                requreFields += f"{field}, "
        if(requreFields != ""):
            return jsonify(
                {
                    "message": f"{requreFields} fields are required."
                }
            )
        collections.insert_one(data)
        return jsonify(
            {
                "message": "Successfully added."
            }
        )
    
# Get, Update, Delete Users data
@app.route("/users/<string:id>", methods=['GET', 'PUT', 'DELETE'])
def getUser(id):

    # Here we check the id is valid or not
    if(not ObjectId.is_valid(id)):
        return jsonify(
        {
            "message": "Invalid ID"
        }
    )

    # Here we check if the id is exist or not
    elif(not collections.find_one({'_id': ObjectId(id)})):
            return jsonify({'message': 'User not found'})
    
    elif(request.method == 'GET'):
        user = collections.find_one({'_id': ObjectId(id)})
        user['_id'] = str(user['_id'])
        return jsonify(user)
        
    elif(request.method == 'PUT'):
        data = request.get_json()
        collections.update_one({'_id': ObjectId(id)}, {'$set': data})
        return jsonify(
            {
                "message": "Sucessfully Updated"
            }
        )
    
    elif(request.method == 'DELETE'):
        user = collections.delete_one({'_id': ObjectId(id)})
        return jsonify(
            {
                "message": "Successfully deleted."
            }
        )
    

app.run(debug=True)