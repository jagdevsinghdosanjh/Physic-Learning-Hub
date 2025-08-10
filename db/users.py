# db/users.py

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["physics_learning"]
users_collection = db["users"]

def create_user(username, password, role):
    users_collection.insert_one({
        "username": username,
        "password": password,
        "role": role
    })

def authenticate_user(username, password):
    return users_collection.find_one({"username": username, "password": password})
