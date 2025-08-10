from utils.notifications import send_email_notification
from db.assignments import assign_quiz_to_students
from db.quizzes import get_all_topics
from db.users import get_all_students
import streamlit as st
import datetime

def assign_quiz():
    st.title("📤 Assign Quiz to Students")

    # Step 1: Select topic
    topics = get_all_topics()
    if not topics:
        st.warning("No quiz topics available.")
        return

    topic = st.selectbox("Select Quiz Topic", topics)

    # Step 2: Select students
    students = get_all_students()
    if not students:
        st.warning("No students found.")
        return

    selected_students = st.multiselect("Select Students", students)

    # Step 3: Set deadline
    deadline = st.date_input("Set Deadline (optional)", value=datetime.date.today())

    # Step 4: Assign quiz and send notifications
    if st.button("✅ Assign Quiz"):
        if not selected_students:
            st.error("Please select at least one student.")
            return

        try:
            assign_quiz_to_students(topic, selected_students, deadline)
            st.success(f"Quiz '{topic}' assigned to selected students with deadline {deadline}.")

            # Send email notifications
            for student in selected_students:
                try:
                    to_email = f"{student}@school.edu"  # Replace with actual email if available
                    send_email_notification(
                        to_email=to_email,
                        subject="New Quiz Assigned",
                        message=f"You've been assigned the quiz: {topic}. Deadline: {deadline}"
                    )
                    st.info(f"📧 Notification sent to {student}")
                except Exception as e:
                    st.warning(f"Failed to send email to {student}: {e}")

        except Exception as e:
            st.error(f"Failed to assign quiz: {e}")

# ✅ Ensure the function is called
assign_quiz()
