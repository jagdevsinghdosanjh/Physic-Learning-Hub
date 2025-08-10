from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["physics_learning_hub"]
progress_collection = db["progress"]

def save_student_score(username, topic, score):
    progress_collection.insert_one({
        "username": username,
        "topic": topic,
        "score": score
    })

def get_scores_by_user(username):
    return list(progress_collection.find({"username": username}))

def get_all_scores(username=None):
    if username:
        return list(progress_collection.find({"username": username}))
    return list(progress_collection.find({}))

def get_all_scores_all_students():
    return list(progress_collection.find({}, {"_id": 0}))

def get_recent_submissions(limit=10):
    return list(progress_collection.find({}, {"_id": 0}).sort("timestamp", -1).limit(limit))
