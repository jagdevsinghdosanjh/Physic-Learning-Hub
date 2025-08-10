import streamlit as st
from db.assignments import get_assigned_quizzes
from db.quizzes import get_all_topics

def show_notifications(username):
    st.title("🔔 Notifications")

    assigned = get_assigned_quizzes(username)
    available = get_all_topics()

    new_quizzes = [q for q in assigned if q in available]

    if new_quizzes:
        st.success("You have new quizzes assigned!")
        for q in new_quizzes:
            st.markdown(f"- ✅ **{q}** is ready to take.")
    else:
        st.info("No new quizzes at the moment.")
