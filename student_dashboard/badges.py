import streamlit as st
from db.progress import get_all_scores

def badge_system(username):
    st.title("🏅 Your Achievements")

    scores = get_all_scores(username)
    total = len(scores)
    avg = sum([s["score"] for s in scores]) / total if total else 0

    if total >= 10:
        st.success("🎖️ Quiz Master: Completed 10+ quizzes")
    if avg >= 90:
        st.success("🌟 High Achiever: Avg score ≥ 90")
    if any(s["score"] == 100 for s in scores):
        st.success("💯 Perfect Score: Scored 100 in a quiz")
