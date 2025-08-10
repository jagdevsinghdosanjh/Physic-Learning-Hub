import streamlit as st
from db.quizzes import get_all_topics, delete_topic
from db.assignments import get_all_assignments, delete_assignment

def manage_content():
    st.title("🗂️ Content Manager")

    st.subheader("📘 Manage Quiz Topics")
    topics = get_all_topics()
    if not topics:
        st.info("No quiz topics available.")
    else:
        selected_topic = st.selectbox("Select a topic to delete", topics)
        if st.button("🗑️ Delete Topic"):
            try:
                delete_topic(selected_topic)
                st.success(f"Topic '{selected_topic}' deleted successfully.")
            except Exception as e:
                st.error(f"Failed to delete topic: {e}")

    st.subheader("📄 Manage Assignments")
    assignments = get_all_assignments()
    if not assignments:
        st.info("No assignments uploaded.")
    else:
        assignment_titles = [a["title"] for a in assignments]
        selected_assignment = st.selectbox("Select an assignment to delete", assignment_titles)
        if st.button("🗑️ Delete Assignment"):
            try:
                delete_assignment(selected_assignment)
                st.success(f"Assignment '{selected_assignment}' deleted successfully.")
            except Exception as e:
                st.error(f"Failed to delete assignment: {e}")

# ✅ Ensure the function is called
manage_content()
