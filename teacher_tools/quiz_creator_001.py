# teacher_tools/quiz_creator.py

import streamlit as st
from db.quizzes import save_quiz

def quiz_creator():
    st.subheader("📝 Create a Quiz")

    topic = st.text_input("Topic Name")
    num_questions = st.number_input("Number of Questions", min_value=1, max_value=20, step=1)

    questions = []
    for i in range(num_questions):
        st.markdown(f"**Question {i+1}**")
        q_text = st.text_input(f"Question Text {i+1}", key=f"q{i}")
        options = [
            st.text_input(f"Option A", key=f"opt{i}_a"),
            st.text_input(f"Option B", key=f"opt{i}_b"),
            st.text_input(f"Option C", key=f"opt{i}_c"),
            st.text_input(f"Option D", key=f"opt{i}_d")
        ]
        correct = st.selectbox("Correct Answer", options, key=f"ans{i}")
        questions.append({
            "question": q_text,
            "options": options,
            "answer": correct
        })

    if st.button("Save Quiz"):
        save_quiz(topic, questions)
        st.success(f"Quiz for '{topic}' saved successfully!")
