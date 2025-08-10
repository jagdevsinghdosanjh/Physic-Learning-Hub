from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["smartschool"]
quizzes_collection = db["quizzes"]

# 📥 Add a new quiz
def add_quiz(topic, questions):
    quiz = {
        "topic": topic,
        "questions": questions
    }
    result = quizzes_collection.insert_one(quiz)
    return result.inserted_id

# 🔍 Get quiz by topic
def get_quiz_by_topic(topic):
    quiz = quizzes_collection.find_one({"topic": topic})
    if quiz:
        return {
            "topic": quiz["topic"],
            "questions": quiz["questions"]
        }
    return None

# 📋 Get all quiz topics
def get_all_topics():
    topics = quizzes_collection.distinct("topic")
    return sorted(topics)

# ✏️ Update quiz questions
def update_quiz(topic, questions):
    result = quizzes_collection.update_one(
        {"topic": topic},
        {"$set": {"questions": questions}}
    )
    return result.modified_count > 0

# 🗑️ Delete quiz by topic
def delete_topic(topic):
    result = quizzes_collection.delete_one({"topic": topic})
    return result.deleted_count > 0

# 📦 Get full quiz document
def get_full_quiz(topic):
    return quizzes_collection.find_one({"topic": topic})
