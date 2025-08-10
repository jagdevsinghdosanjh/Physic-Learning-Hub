from pymongo import MongoClient
from urllib.parse import quote_plus
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

def get_db():
    user = quote_plus(os.getenv("MONGO_USER"))
    password = quote_plus(os.getenv("MONGO_PASS"))
    host = os.getenv("MONGO_HOST", "localhost:27017")
    db_name = os.getenv("MONGO_DB", "physics_learning_hub")

    mongo_uri = f"mongodb+srv://{user}:{password}@{host}/{db_name}?retryWrites=true&w=majority&authSource=admin"

    client = MongoClient(mongo_uri)
    return client[db_name]


# === User Operations ===
def get_user_by_username(username: str):
    db = get_db()
    return db.users.find_one({"username": username})

def create_user(username: str, hashed_password: str):
    db = get_db()
    db.users.insert_one({
        "username": username,
        "password": hashed_password,
        "created_at":datetime.now()
    })

# === Quiz Operations ===
def get_quiz_by_topic(topic: str):
    db = get_db()
    return db.quizzes.find_one({"topic": topic})

def save_quiz_response(user_id: str, topic: str, score: int):
    db = get_db()
    db.responses.insert_one({
        "user_id": user_id,
        "topic": topic,
        "score": score,
        "timestamp": datetime.now()
    })

# === Leaderboard & Analytics ===
def get_leaderboard():
    db = get_db()
    pipeline = [
        {"$group": {"_id": "$user_id", "total_score": {"$sum": "$score"}}},
        {"$sort": {"total_score": -1}},
        {"$limit": 10}
    ]
    return list(db.responses.aggregate(pipeline))

# === Public Connector ===
def get_db_connection():
    return get_db()

# === Messaging Operations ===
def send_message(username: str, message: str):
    db = get_db()
    if not username or not message:
        raise ValueError("Username and message must be provided.")

    db.messages.insert_one({
        "username": username,
        "message": message,
        "timestamp": datetime.utcnow()
    })


def get_messages_for_student(username: str):
    db = get_db()
    if not username:
        raise ValueError("Username must be provided.")

    return list(db.messages.find(
        {"username": username},
        {"_id": 0}
    ))
