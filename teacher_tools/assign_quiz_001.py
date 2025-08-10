from utils.notifications import send_email_notification
from db.assignments import assign_quiz_to_students
from db.quizzes import get_all_topics
from db.users import get_all_students
import streamlit as st
import datetime


deadline = st.date_input("Set Deadline (optional)", value=datetime.date.today())
assign_quiz_to_students(topic, selected_students, deadline)

for student in selected_students:
    send_email_notification(
        to_email=f"{student}@school.edu",
        subject="New Quiz Assigned",
        message=f"You've been assigned the quiz: {topic}. Deadline: {deadline}"
    )

def assign_quiz():
    st.title("📤 Assign Quiz to Students")

    topic = st.selectbox("Select Quiz Topic", get_all_topics())
    students = get_all_students()

    selected_students = st.multiselect("Select Students", students)

    if st.button("✅ Assign Quiz"):
        assign_quiz_to_students(topic, selected_students)
        st.success(f"Quiz '{topic}' assigned to selected students.")
