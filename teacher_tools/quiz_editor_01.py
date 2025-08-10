# teacher_tools/quiz_editor.py

import streamlit as st
from db.quizzes import get_quiz_by_topic, update_quiz, delete_quiz

def quiz_editor():
    st.header("✏️ Edit or Delete Quiz")

    topic = st.selectbox("Select Topic", ["Physical World", "Units and Measurements", "Electrostatics", "Current Electricity"])
    quiz = get_quiz_by_topic(topic)

    if not quiz:
        st.warning("No quiz found for this topic.")
        return

    st.subheader("Edit Questions")
    updated_questions = []
    for i, q in enumerate(quiz["questions"]):
        st.markdown(f"**Question {i+1}**")
        q_text = st.text_input("Question", value=q["question"], key=f"q{i}")
        options = [st.text_input(f"Option {j+1}", value=opt, key=f"opt{i}_{j}") for j, opt in enumerate(q["options"])]
        correct = st.selectbox("Correct Answer", options, index=options.index(q["answer"]), key=f"ans{i}")
        updated_questions.append({
            "question": q_text,
            "options": options,
            "answer": correct
        })

    if st.button("💾 Save Changes"):
        update_quiz(topic, updated_questions)
        st.success("Quiz updated successfully!")

    if st.button("🗑️ Delete Quiz"):
        delete_quiz(topic)
        st.warning("Quiz deleted.")
