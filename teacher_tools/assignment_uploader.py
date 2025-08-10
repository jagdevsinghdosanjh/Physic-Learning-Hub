import streamlit as st
import datetime
from db.assignments import save_assignment
from db.quizzes import get_all_topics

def upload_assignment():
    st.title("📚 Upload New Assignment")

    # Step 1: Select topic
    topics = get_all_topics()
    if not topics:
        st.warning("No topics available. Please create a topic first.")
        return

    topic = st.selectbox("Select Topic", topics)

    # Step 2: Upload file
    uploaded_file = st.file_uploader("Upload Assignment File (PDF, DOCX, etc.)", type=["pdf", "docx", "txt"])
    if not uploaded_file:
        st.info("Please upload a file to continue.")
        return

    # Step 3: Add optional metadata
    description = st.text_area("Assignment Description (optional)")
    deadline = st.date_input("Set Deadline (optional)", value=datetime.date.today())

    # Step 4: Submit
    if st.button("📤 Submit Assignment"):
        try:
            # Save assignment to database or file system
            save_assignment(
                topic=topic,
                file=uploaded_file,
                description=description,
                deadline=deadline
            )
            st.success(f"Assignment for topic '{topic}' uploaded successfully.")
        except Exception as e:
            st.error(f"Failed to upload assignment: {e}")

# ✅ Ensure the function is called
upload_assignment()
