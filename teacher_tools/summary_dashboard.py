import streamlit as st
from db.quizzes import get_all_topics
from db.users import get_all_students
from db.assignments import get_all_assignments

def summary_dashboard():
    st.title("📊 Teacher Summary Dashboard")

    total_quizzes = len(get_all_topics())
    total_students = len(get_all_students())
    total_assignments = len(get_all_assignments())

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Quizzes", total_quizzes)
    col2.metric("Total Students", total_students)
    col3.metric("Total Assignments", total_assignments)

    st.markdown("---")
    st.subheader("📋 Assignment Overview")
    assignments = get_all_assignments()
    for a in assignments:
        st.markdown(f"- **{a['username']}** → {len(a.get('assigned_quizzes', []))} quizzes assigned")
