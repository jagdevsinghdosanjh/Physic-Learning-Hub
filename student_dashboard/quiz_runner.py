# student_dashboard/quiz_runner.py

import streamlit as st
from db.quizzes import get_quiz_by_topic
from db.progress import save_student_score

def quiz_runner(username):
    st.header("🧠 Take a Quiz")

    topic = st.selectbox("Choose Topic", ["Physical World", "Units and Measurements", "Electrostatics", "Current Electricity"])
    quiz = get_quiz_by_topic(topic)

    if not quiz:
        st.warning("No quiz available for this topic yet.")
        return

    score = 0
    responses = {}

    for i, q in enumerate(quiz["questions"]):
        st.subheader(f"Q{i+1}: {q['question']}")
        answer = st.radio("Choose your answer", q["options"], key=f"q{i}")
        responses[q["question"]] = answer
        if answer == q["answer"]:
            score += 1

    if st.button("Submit Quiz"):
        st.success(f"You scored {score} out of {len(quiz['questions'])}")
        save_student_score(username, topic, score)

        st.markdown("---")
        st.subheader("📖 Review Answers")
        for i, q in enumerate(quiz["questions"]):
            st.markdown(f"**Q{i+1}: {q['question']}**")
            st.markdown(f"- Your answer: `{responses[q['question']]}`")
            st.markdown(f"- Correct answer: ✅ `{q['answer']}`")
            if responses[q["question"]] == q["answer"]:
                st.success("Correct ✅")
            else:
                st.error("Incorrect ❌")
