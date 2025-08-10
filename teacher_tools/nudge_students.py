import streamlit as st
from db.users import get_all_students
from db.progress import get_student_scores
from db.messages import send_message
from datetime import datetime

def nudge_students():
    st.title("📬 Nudge Inactive Students")

    threshold_days = st.slider("Inactivity Threshold (days)", 3, 30, 7)
    students = get_all_students()

    inactive_students = []

    for student in students:
        scores = get_student_scores(student["username"])
        if not scores:
            inactive_students.append(student["username"])
        else:
            last_activity = max(datetime.strptime(s["date"], "%Y-%m-%d") for s in scores)
            if (datetime.today() - last_activity).days > threshold_days:
                inactive_students.append(student["username"])

    if not inactive_students:
        st.success("🎉 All students are active!")
        return

    st.subheader(f"Students inactive for more than {threshold_days} days:")
    selected_students = st.multiselect("Select students to nudge", inactive_students)

    if st.button("📨 Send Nudges"):
        for username in selected_students:
            send_message(username, "Hi! We noticed you haven’t taken a quiz recently. Jump back in and keep learning! 🚀")
            st.success(f"Nudge sent to {username}")
