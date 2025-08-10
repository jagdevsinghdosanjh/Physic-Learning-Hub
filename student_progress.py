import streamlit as st
import pandas as pd
from db.progress import get_all_scores_all_students

def student_progress():
    st.title("📊 Student Progress by Quiz")

    scores = get_all_scores_all_students()
    df = pd.DataFrame(scores)

    topic = st.selectbox("Select Quiz Topic", sorted(df["topic"].unique()))
    filtered = df[df["topic"] == topic]

    st.dataframe(filtered.sort_values(by="score", ascending=False))
