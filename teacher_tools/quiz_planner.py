import streamlit as st
from db.assignments import schedule_quiz_for_class
from db.quizzes import get_all_topics

def quiz_planner():
    st.title("🗓️ Quiz Planner")

    topic = st.selectbox("Select Quiz Topic", get_all_topics())
    target_class = st.selectbox("Target Class", ["Class IX", "Class X", "Class XI", "Class XII"])
    deadline = st.date_input("Set Deadline")

    if st.button("📌 Schedule Quiz"):
        schedule_quiz_for_class(topic, target_class, deadline.strftime("%Y-%m-%d"))
        st.success(f"Quiz '{topic}' scheduled for {target_class} by {deadline}")
