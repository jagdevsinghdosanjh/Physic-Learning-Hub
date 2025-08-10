import streamlit as st
from pymongo import MongoClient

# Build MongoDB URI
mongo_uri = f"mongodb+srv://{st.secrets['mongo']['user']}:{st.secrets['mongo']['password']}@{st.secrets['mongo']['host']}/{st.secrets['mongo']['database']}?retryWrites=true&w=majority"

# Connect to MongoDB
client = MongoClient(mongo_uri)
db = client[st.secrets["mongo"]["database"]]

# Example: Access a collection
collection = db["students"]
students = collection.find()

# Display data
for student in students:
    st.write(student)
