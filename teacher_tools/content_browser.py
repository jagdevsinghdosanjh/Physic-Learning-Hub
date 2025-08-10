import streamlit as st
from db.quizzes import get_all_topics, get_quiz_by_topic
from db.assignments import get_all_assignments
from utils.display import preview_quiz, show_tabs, show_assignment, show_quiz_question

def content_browser():
    st.title("📚 Content Browser Dashboard")

    # 🔍 Select a quiz topic to preview
    topics = get_all_topics()
    if not topics:
        st.warning("No quiz topics available.")
        return

    selected_topic = st.selectbox("Choose a Quiz Topic to Preview", topics)
    quiz = get_quiz_by_topic(selected_topic)

    if quiz:
        st.subheader(f"🧪 Preview: {selected_topic}")
        preview_quiz(quiz)
    else:
        st.warning("Quiz not found.")

    # 🗂️ Tabbed view for assignments and quiz questions
    show_tabs({
        "Assignments": lambda: [
            show_assignment(a) for a in get_all_assignments()
        ],
        "Quiz Questions": lambda: [
            show_quiz_question(q, i) for i, q in enumerate(quiz["questions"])
        ] if quiz else st.info("No questions available.")
    })

# ✅ Run the dashboard
content_browser()
