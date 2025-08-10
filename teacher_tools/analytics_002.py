from db.progress import get_all_scores 
from utils.file_ops import export_csv, export_pdf 
import streamlit as st
import pandas as pd
import altair as alt

def teacher_analytics():
    st.header("📈 Class-Wide Quiz Analytics")

    # Fetch all scores
    all_scores = get_all_scores()
    if not all_scores:
        st.info("No quiz data available.")
        return

    # Create DataFrame
    df = pd.DataFrame(all_scores)

    # Calculate average scores by topic
    avg_scores = df.groupby("topic")["score"].mean().reset_index()

    # Display chart
    chart = alt.Chart(avg_scores).mark_bar().encode(
        x="topic",
        y="score",
        tooltip=["topic", "score"]
    ).properties(title="📊 Average Scores by Topic")

    st.altair_chart(chart, use_container_width=True)

    # Show raw data
    st.subheader("📋 Raw Data")
    st.dataframe(df)

    # Export section
    st.subheader("📤 Export Reports")

    csv_data = export_csv(df)
    st.download_button("Download CSV", csv_data, file_name="quiz_scores.csv", mime="text/csv")

    pdf_data = export_pdf(df)
    st.download_button("Download PDF", pdf_data, file_name="quiz_scores.pdf", mime="application/pdf")
