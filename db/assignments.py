from pymongo import MongoClient
from datetime import datetime
from db.progress import get_all_scores_all_students
from db.users import users_collection
import streamlit as st
import pandas as pd
import altair as alt

client = MongoClient("mongodb://localhost:27017/")
db = client["smartschool"]
assignments_collection = db["assignments"]

# 📊 Class Analytics
def class_analytics():
    st.title("🏫 Class-Wise Analytics")

    df = pd.DataFrame(get_all_scores_all_students())
    if df.empty:
        st.info("No quiz data available.")
        return

    class_selected = st.selectbox("Select Class", sorted(df["class"].unique()))
    filtered_df = df[df["class"] == class_selected]

    avg_scores = filtered_df.groupby("topic")["score"].mean().reset_index()

    chart = alt.Chart(avg_scores).mark_bar().encode(
        x="topic",
        y="score",
        tooltip=["topic", "score"]
    ).properties(title=f"Average Scores for {class_selected}")

    st.altair_chart(chart, use_container_width=True)

# 📥 Assign quiz to students
def assign_quiz_to_students(topic, student_usernames, deadline=None):
    for username in student_usernames:
        assignment = {
            "topic": topic,
            "assigned_on": datetime.utcnow(),
            "deadline": deadline
        }
        assignments_collection.update_one(
            {"username": username},
            {"$addToSet": {"assigned_quizzes": assignment}},
            upsert=True
        )

# 📅 Schedule quiz for a class
def schedule_quiz_for_class(topic, class_name, deadline):
    students = users_collection.find({"class": class_name})
    for student in students:
        assignments_collection.update_one(
            {"username": student["username"]},
            {"$push": {"assigned_quizzes": {"topic": topic, "deadline": deadline}}},
            upsert=True
        )

# 📤 Save uploaded assignment
def save_assignment(topic, file, description, deadline):
    assignment_doc = {
        "title": file.name,
        "topic": topic,
        "description": description,
        "deadline": deadline,
        "uploaded_on": datetime.utcnow(),
        "content": file.read()
    }
    assignments_collection.insert_one(assignment_doc)

# 📋 Get all assignments
def get_all_assignments():
    return list(assignments_collection.find({"title": {"$exists": True}}, {"_id": 0}))

# 🗑️ Delete assignment by title
def delete_assignment(title):
    result = assignments_collection.delete_one({"title": title})
    return result.deleted_count > 0

# 👤 Get assignments for a student
def get_assignments_for_student(username):
    return assignments_collection.find_one({"username": username}, {"_id": 0})

# 📚 Get assigned quizzes for a student
def get_assigned_quizzes(username):
    doc = assignments_collection.find_one({"username": username})
    return doc.get("assigned_quizzes", []) if doc else []
