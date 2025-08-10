import streamlit as st
import pandas as pd
import altair as alt
from db.progress import get_all_scores_all_students

def class_analytics():
    st.title("🏫 Class-Wise Analytics")

    df = pd.DataFrame(get_all_scores_all_students())
    if df.empty:
        st.info("No quiz data available.")
        return

    class_selected = st.selectbox("Select Class", sorted(df["class"].unique()))
    filtered_df = df[df["class"] == class_selected]

    avg_scores = filtered_df.groupby("topic")["score"].mean().reset_index()

    chart = alt.Chart(avg_scores).mark_bar().encode(
        x="topic",
        y="score",
        tooltip=["topic", "score"]
    ).properties(title=f"Average Scores for {class_selected}")

    st.altair_chart(chart, use_container_width=True)
