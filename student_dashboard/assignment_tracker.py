import streamlit as st
from db.assignments import get_assigned_quizzes
from db.progress import get_all_scores

def assignment_tracker(username):
    st.title("📌 Your Assignments")

    assigned = get_assigned_quizzes(username)
    completed = get_all_scores(username)
    completed_topics = [entry["topic"] for entry in completed]

    for a in assigned:
        topic = a["topic"]
        deadline = a.get("deadline", "No deadline")
        status = "✅ Completed" if topic in completed_topics else "🕒 Pending"
        st.markdown(f"- **{topic}** — {status} (Deadline: {deadline})")
