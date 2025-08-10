# student_dashboard/history.py

import streamlit as st
import pandas as pd
from db.progress import get_all_scores

def student_history(username):
    st.header("📚 Your Quiz History")

    scores = get_all_scores(username)
    if not scores:
        st.info("You haven't taken any quizzes yet.")
        return

    df = pd.DataFrame(scores)
    df = df.sort_values(by="topic")

    st.dataframe(df)

    # Optional: Summary
    avg_score = df["score"].mean()
    st.metric("Average Score", f"{avg_score:.2f}")
