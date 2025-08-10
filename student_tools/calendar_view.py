import streamlit as st
import pandas as pd
from db.assignments import get_assignments_for_student
from datetime import datetime

def calendar_view(username):
    st.title("🗓️ My Quiz Calendar")

    assignments = get_assignments_for_student(username)
    if not assignments or not assignments.get("assigned_quizzes"):
        st.info("No upcoming quizzes.")
        return

    events = []
    for quiz in assignments["assigned_quizzes"]:
        events.append({
            "Topic": quiz["topic"],
            "Deadline": datetime.strptime(quiz["deadline"], "%Y-%m-%d")
        })

    df = pd.DataFrame(events).sort_values("Deadline")
    st.dataframe(df.set_index("Deadline"))
