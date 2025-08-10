import streamlit as st
from db.users import get_all_students
from db.progress import get_student_scores
from db.messages import send_message
from datetime import datetime, timedelta

def nudge_students():
    st.title("📬 Nudge Inactive Students")

    threshold_days = st.slider("Inactivity Threshold", 3, 30, 7)
    students = get_all_students()

    for student in students:
        scores = get_student_scores(student["username"])
        if not scores or (datetime.today() - max(datetime.strptime(s["date"], "%Y-%m-%d") for s in scores)).days > threshold_days:
            if st.button(f"Send Nudge to {student['username']}"):
                send_message(student["username"], "Hi! We noticed you haven’t taken a quiz recently. Jump back in and keep learning! 🚀")
                st.success(f"Nudge sent to {student['username']}")
