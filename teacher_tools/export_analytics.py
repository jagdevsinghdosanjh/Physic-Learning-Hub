import streamlit as st
import pandas as pd
from db.progress import get_all_scores_all_students

def export_analytics():
    st.title("📤 Export Class Analytics")

    df = pd.DataFrame(get_all_scores_all_students())
    if df.empty:
        st.info("No data to export.")
        return

    st.download_button(
        label="📄 Download Excel",
        data=df.to_excel(index=False, engine='openpyxl'),
        file_name="class_analytics.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    st.download_button(
        label="🧾 Download PDF",
        data=df.to_string(index=False).encode("utf-8"),
        file_name="class_analytics.pdf",
        mime="application/pdf"
    )
