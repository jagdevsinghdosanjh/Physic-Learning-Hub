from pymongo import MongoClient
from datetime import datetime
from progress import get_all_scores_all_students
from users import users_collection
import streamlit as st
import pandas as pd
import altair as alt

client = MongoClient("mongodb://localhost:27017/")
db = client["smartschool"]
assignments_collection = db["assignments"]

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

def get_assigned_quizzes(username):
    doc = assignments_collection.find_one({"username": username})
    return doc.get("assigned_quizzes", []) if doc else []

# def assign_quiz_to_students(topic, student_usernames):
#     for username in student_usernames:
#         assignments_collection.update_one(
#             {"username": username},
#             {"$addToSet": {"assigned_quizzes": topic}},
#             upsert=True
#         )

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

def get_assignments_for_student(username):
    return assignments_collection.find_one({"username": username}, {"_id": 0})

def schedule_quiz_for_class(topic, class_name, deadline):
    students = users_collection.find({"class": class_name})
    for student in students:
        assignments_collection.update_one(
            {"username": student["username"]},
            {"$push": {"assigned_quizzes": {"topic": topic, "deadline": deadline}}},
            upsert=True
        )
