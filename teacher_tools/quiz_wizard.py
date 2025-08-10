import streamlit as st
from db.quizzes import add_quiz

def quiz_wizard():
    st.title("🧙 Quiz Creation Wizard")

    topic = st.text_input("Quiz Topic")
    template = st.selectbox("Choose Template", ["Blank", "Physics Basics", "Units & Measurements"])

    questions = []

    if template == "Physics Basics":
        questions = [
            {
                "question": "What is the scope of physics?",
                "options": ["Matter", "Energy", "Space", "All of the above"],
                "answer": "All of the above"
            }
        ]
    elif template == "Units & Measurements":
        questions = [
            {
                "question": "What is the SI unit of length?",
                "options": ["Meter", "Kilogram", "Second", "Ampere"],
                "answer": "Meter"
            }
        ]

    st.subheader("Customize Questions")
    for i, q in enumerate(questions):
        st.text_input(f"Q{i+1}", value=q["question"], key=f"q{i}")
        for j, opt in enumerate(q["options"]):
            st.text_input(f"Option {j+1}", value=opt, key=f"opt{i}_{j}")
        st.selectbox("Correct Answer", q["options"], index=q["options"].index(q["answer"]), key=f"ans{i}")

    if st.button("🧾 Create Quiz"):
        add_quiz(topic, questions)
        st.success(f"Quiz '{topic}' created successfully!")
