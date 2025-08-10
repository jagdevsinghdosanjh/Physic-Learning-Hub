import streamlit as st
import pandas as pd
from db.progress import get_all_scores_all_students

def leaderboard():
    st.title("🏆 Leaderboard")

    class_filter = st.selectbox("Filter by Class", ["All", "Class 9", "Class 10"])
    subject_filter = st.selectbox("Filter by Subject", ["All", "Physics", "Math", "Chemistry"])

    scores = get_all_scores_all_students()

    df = pd.DataFrame(scores)
    if class_filter != "All":
        df = df[df["class"] == class_filter]
    if subject_filter != "All":
        df = df[df["subject"] == subject_filter]

    leaderboard_df = df.groupby("username").agg({
        "score": ["mean", "count"]
    }).reset_index()

    leaderboard_df.columns = ["Username", "Average Score", "Quizzes Taken"]
    st.dataframe(leaderboard_df.sort_values(by="Average Score", ascending=False))


def leaderboard():
    st.title("🏆 Student Leaderboard")

    scores = get_all_scores_all_students()
    if not scores:
        st.info("No quiz data available.")
        return

    df = pd.DataFrame(scores)
    leaderboard_df = df.groupby("username").agg({
        "score": ["mean", "count"]
    }).reset_index()

    leaderboard_df.columns = ["Username", "Average Score", "Quizzes Taken"]
    leaderboard_df = leaderboard_df.sort_values(by="Average Score", ascending=False)

    st.dataframe(leaderboard_df)
