import streamlit as st
from db.assignments import get_assignments_for_student
from datetime import datetime

def notifications(username):
    st.title("🔔 Notifications")

    assignments = get_assignments_for_student(username)
    if not assignments:
        st.info("No active assignments.")
        return

    today = datetime.today().date()
    for quiz in assignments.get("assigned_quizzes", []):
        deadline = datetime.strptime(quiz["deadline"], "%Y-%m-%d").date()
        days_left = (deadline - today).days
        if days_left < 0:
            st.error(f"❌ Missed deadline for **{quiz['topic']}**")
        elif days_left == 0:
            st.warning(f"⚠️ Today is the deadline for **{quiz['topic']}**")
        else:
            st.info(f"📅 **{quiz['topic']}** due in {days_left} days")
