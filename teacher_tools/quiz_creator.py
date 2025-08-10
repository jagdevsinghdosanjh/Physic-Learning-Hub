import streamlit as st
from db.quizzes import add_quiz

def quiz_creator():
    st.title("📝 Create a New Quiz")

    topic = st.text_input("Enter Quiz Topic")
    num_questions = st.number_input("Number of Questions", min_value=1, max_value=20, step=1)

    questions = []

    for i in range(int(num_questions)):
        st.markdown(f"### Question {i + 1}")
        q_text = st.text_input(f"Question Text", key=f"q{i}")
        option_a = st.text_input(f"Option A", key=f"opt{i}_a")
        option_b = st.text_input(f"Option B", key=f"opt{i}_b")
        option_c = st.text_input(f"Option C", key=f"opt{i}_c")
        option_d = st.text_input(f"Option D", key=f"opt{i}_d")

        options = [option_a, option_b, option_c, option_d]
        correct = st.selectbox("Correct Answer", options, key=f"ans{i}")

        questions.append({
            "question": q_text,
            "options": options,
            "answer": correct
        })

    if st.button("💾 Save Quiz"):
        if not topic.strip():
            st.error("Please enter a topic name.")
            return
        if any(not q["question"].strip() or not all(q["options"]) for q in questions):
            st.error("Please complete all questions and options.")
            return

        add_quiz(topic, questions)
        st.success(f"✅ Quiz for '{topic}' saved successfully!")

# ✅ Ensure the function is called
quiz_creator()
