# messages.py

from db import send_message, get_messages_for_student

__all__ = ["send_message", "get_messages_for_student"]

# from datetime import datetime
# from db import messages_collection  # Assumes messages_collection is defined in db.py

# def send_message(username, message):
#     """
#     Stores a message from a student or teacher in the database.
#     """
#     if not username or not message:
#         raise ValueError("Username and message must be provided.")

#     try:
#         messages_collection.insert_one({
#             "username": username,
#             "message": message,
#             "timestamp": datetime.utcnow()
#         })
#     except Exception as e:
#         print(f"Error sending message: {e}")
#         raise


# def get_messages_for_student(username):
#     """
#     Retrieves all messages for a given student.
#     """
#     if not username:
#         raise ValueError("Username must be provided.")

#     try:
#         return list(messages_collection.find(
#             {"username": username},
#             {"_id": 0}
#         ))
#     except Exception as e:
#         print(f"Error retrieving messages: {e}")
#         return []

# # from datetime import datetime

# # def send_message(username, message):
# #     messages_collection.insert_one({
# #         "username": username,
# #         "message": message,
# #         "timestamp": datetime.utcnow().isoformat()
# #     })

# # def get_messages_for_student(username):
# #     return list(messages_collection.find({"username": username}, {"_id": 0}))
