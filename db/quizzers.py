# db/quizzes.py

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["physics_learning"]
quizzes_collection = db["quizzes"]

def get_quiz_by_topic(topic):
    return quizzes_collection.find_one({"topic": topic})

def save_quiz(topic, questions):
    quizzes_collection.update_one(
        {"topic": topic},
        {"$set": {"questions": questions}},
        upsert=True
    )

# # db/quizzes.py

# # Temporary in-memory store
# quiz_store = {}

# def save_quiz(class_name, topic, question_data):
#     key = f"{class_name}_{topic}".lower().replace(" ", "_")
#     if key not in quiz_store:
#         quiz_store[key] = []
#     quiz_store[key].append(question_data)
