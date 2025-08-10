import streamlit as st
from db.users import get_all_students
from db.progress import get_student_scores
from datetime import datetime, timedelta

def inactivity_monitor():
    st.title("🕵️ Inactivity Monitor")

    students = get_all_students()
    threshold_days = st.slider("Inactivity Threshold (days)", 3, 30, 7)

    inactive = []
    for student in students:
        scores = get_student_scores(student["username"])
        if not scores:
            inactive.append((student["username"], "Never attempted"))
            continue
        latest = max(datetime.strptime(s["date"], "%Y-%m-%d") for s in scores)
        if (datetime.today() - latest).days > threshold_days:
            inactive.append((student["username"], f"{(datetime.today() - latest).days} days ago"))

    if inactive:
        st.subheader("🚫 Inactive Students")
        for name, status in inactive:
            st.markdown(f"- **{name}** → Last activity: {status}")
    else:
        st.success("🎉 All students are active!")
