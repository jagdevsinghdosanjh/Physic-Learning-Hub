import streamlit as st
import pandas as pd
from db.progress import get_all_scores_all_students

def leaderboard():
    st.title("🏆 Student Leaderboard")

    # Fetch scores
    scores = get_all_scores_all_students()
    if not scores:
        st.info("No quiz data available.")
        return

    df = pd.DataFrame(scores)

    # Dynamic filters based on available data
    class_options = ["All"] + sorted(df["class"].dropna().unique())
    subject_options = ["All"] + sorted(df["subject"].dropna().unique())

    class_filter = st.selectbox("Filter by Class", class_options)
    subject_filter = st.selectbox("Filter by Subject", subject_options)

    # Apply filters
    if class_filter != "All":
        df = df[df["class"] == class_filter]
    if subject_filter != "All":
        df = df[df["subject"] == subject_filter]

    if df.empty:
        st.warning("No data matches the selected filters.")
        return

    # Aggregate leaderboard
    leaderboard_df = df.groupby("username").agg(
        Average_Score=("score", "mean"),
        Quizzes_Taken=("score", "count")
    ).reset_index()

    leaderboard_df = leaderboard_df.sort_values(by="Average_Score", ascending=False)

    st.dataframe(leaderboard_df)

# ✅ Ensure the function is called
leaderboard()
