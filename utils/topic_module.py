from utils.db import get_db

def get_topics_by_role(role: str):
    db = get_db()
    query = {} if role == "Teacher" else {"visible_to": {"$in": [role, "All"]}}
    return list(db.topics.find(query, {"_id": 0, "title": 1, "id": 1}))
