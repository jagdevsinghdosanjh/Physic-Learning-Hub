
# from pymongo import MongoClient

# client = MongoClient("mongodb+srv://jagdevsinghdosanjh: Jsdasr@1973 cluster0.3xnlzlw.mongodb.net/")
# db = client.get_database("physics_learning_hub")
# print(db.list_collection_names())
from utils.db import get_db

db = get_db()
print("Connected to:", db.name)
print("Collections:", db.list_collection_names())
