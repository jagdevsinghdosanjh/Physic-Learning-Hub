import streamlit as st
from db.progress import get_student_scores
from utils.gamification import calculate_xp, determine_level

def gamified_dashboard(username):
    st.title("🎮 My Gamified Dashboard")

    scores = get_student_scores(username)
    if not scores:
        st.info("No quiz data yet.")
        return

    xp = calculate_xp(scores)
    level = determine_level(xp)

    st.metric("⭐ XP Points", xp)
    st.metric("🎯 Level", level)

    st.progress(min(xp % 100 / 100, 1.0))
    st.caption(f"Next level at {((level + 1) * 100)} XP")
