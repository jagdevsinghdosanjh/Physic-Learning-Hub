import streamlit as st
from components import quiz_ui #noqa
import os
from components.quiz import render_quiz  # Assumes reusable quiz component


def load_markdown(topic_id):
    """Load markdown content from assets folder."""
    filepath = os.path.join("assets", f"{topic_id}.md")
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    else:
        return "🚫 Topic content not found."

def render(role="Student"):
    st.title("📏 Units and Measurements")

    # Render markdown content
    md_content = load_markdown("unitsandmeasurements")
    st.markdown(md_content, unsafe_allow_html=True)

    # Role-specific view
    if role == "Teacher":
        st.info("👩‍🏫 Teacher View: Add notes, track student progress, or review analytics.")

    # Divider and quiz
    st.divider()
    st.subheader("🧠 Test Your Understanding")

    quiz_data = [
        {
            "question": "Which of the following is a fundamental quantity?",
            "options": ["Velocity", "Force", "Mass", "Acceleration"],
            "answer": "Mass"
        },
        {
            "question": "Dimensional formula of energy?",
            "options": ["ML^2T^-2", "MLT^-1", "M^2L^2T^-2", "ML^-1T^-2"],
            "answer": "ML^2T^-2"
        }
    ]
    render_quiz(quiz_data)

    # Tip
    st.info("💡 Dimensional analysis helps verify equations and derive relationships. Use it often!")
    