import streamlit as st
import time
from db.progress import get_recent_submissions

def live_submissions():
    st.title("📡 Live Quiz Submissions")

    st.info("Auto-refreshing every 10 seconds...")
    placeholder = st.empty()

    while True:
        with placeholder.container():
            submissions = get_recent_submissions()
            if not submissions:
                st.write("No recent submissions.")
            else:
                for sub in submissions:
                    st.markdown(f"- **{sub['username']}** submitted **{sub['topic']}** → {sub['score']}%")
        time.sleep(10)
