import streamlit as st
from db.progress import get_student_scores
from utils.badges import calculate_badges, calculate_streak

def student_dashboard(username):
    st.title("🎓 My Learning Dashboard")

    scores = get_student_scores(username)
    if not scores:
        st.info("No quiz data yet.")
        return

    badges = calculate_badges(scores)
    streak = calculate_streak(scores)

    st.metric("🔥 Quiz Streak", f"{streak} days")
    st.subheader("🏅 Badges Earned")
    for b in badges:
        st.markdown(f"- {b}")
