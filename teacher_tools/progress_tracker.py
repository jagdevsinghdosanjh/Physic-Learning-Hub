# teacher_tools/progress_tracker.py

import streamlit as st
import pandas as pd
import altair as alt
from db.progress import get_all_scores
from db.users import users_collection

def progress_tracker():
    st.header("📊 Student Progress Tracker")

    students = users_collection.find({"role": "student"})
    student_names = sorted([s["username"] for s in students])
    selected_student = st.selectbox("Select Student", student_names)

    scores = get_all_scores(selected_student)
    if not scores:
        st.info("No quiz data available for this student.")
        return

    df = pd.DataFrame(scores)
    df = df.sort_values(by="topic")

    # 🔍 Topic filter
    topics = df["topic"].unique().tolist()
    selected_topics = st.multiselect("Filter by Topic", topics, default=topics)
    filtered_df = df[df["topic"].isin(selected_topics)]

    # 📄 Pagination
    page_size = 5
    total_pages = (len(filtered_df) - 1) // page_size + 1
    page = st.number_input("Page", min_value=1, max_value=total_pages, step=1)
    start = (page - 1) * page_size
    end = start + page_size
    paginated_df = filtered_df.iloc[start:end]

    chart = alt.Chart(paginated_df).mark_bar().encode(
        x="topic",
        y="score",
        tooltip=["topic", "score"]
    ).properties(title=f"{selected_student}'s Quiz Performance")

    st.altair_chart(chart, use_container_width=True)
