from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["physics_app"]

users = db["users"]
quizzes = db["quizzes"]
doubts = db["doubts"]
content = db["content"]
