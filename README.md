# Flask MongoDB CRUD API - User Management System
This project provides a RESTful API for user management using Flask and MongoDB. The API allows you to perform CRUD (Create, Read, Update, Delete) operations on user data. Each user resource contains the following fields:
  * id (a unique identifier for the user)
  * name (the name of the user)
  * email (the email address of the user)
  * password (the password of the user)
# Getting Started
Follow the instructions below to set up and run the application on your local machine.
# Prerequisites
Make sure you have the following software installed on your system:
  * Python (version 3.6 or higher)
  * MongoDB (version 4.0 or higher)
# Installation
1. Clone the repository to your local machine:
```
  git clone https://github.com/sibashis9692/Flask_API.git
  cd Flask_API
```
2. Create a virtual environment (optional):
```
python -m venv venv
venv\Scripts\activate
```
3. Install the required dependencies:
```
pip install -r requirements.txt
```
# Configuration
By default, the application connects to a local MongoDB server at localhost:27017. If your MongoDB server is running on a different host or port, you can modify the connection settings in the app.py file.
```
# main.py
client = MongoClient('localhost', 27017)
```
# Running the Application
```
python main.py
```
The server should now be running at http://localhost:5000

# API Endpoints
# GET /users
Returns a list of all users.
# Response:
```
[
    {
        "id": "6146d6b16384d43df6f1b3f7",
        "name": "John Doe",
        "email": "john@example.com",
        "password": "hashed_password"
    },
    {
        "id": "6146d6b16384d43df6f1b3f8",
        "name": "Jane Smith",
        "email": "jane@example.com",
        "password": "hashed_password"
    }
]
```
# GET /users/id
Returns the user with the specified ID.
# Response:
```
{
    "id": "6146d6b16384d43df6f1b3f7",
    "name": "John Doe",
    "email": "john@example.com",
    "password": "hashed_password"
}
```
# POST /users
Creates a new user with the specified data.
# Request Body:
```
{
    "name": "New User",
    "email": "newuser@example.com",
    "password": "new_password"
}
```
# Response:
```
{
    "message": "Successfully added."
}
```
# PUT /users/id
Updates the user with the specified ID with the new data.
# Request Body:
```
{
    "name": "Updated User",
    "email": "updateduser@example.com",
    "password": "updated_password"
}
```
# Response:
```
{
    "message": "Successfully updated."
}
```
# DELETE /users/id
Deletes the user with the specified ID.
# Response:
```
{
    "message": "Successfully deleted."
}
```
# Conclusion
Congratulations! You have successfully set up and run the Flask MongoDB CRUD API for user management. You can now use the provided API endpoints to perform CRUD operations on user data.
