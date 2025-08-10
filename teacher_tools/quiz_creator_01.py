# teacher_tools/quiz_creator.py

import streamlit as st
from db.quizzes import save_quiz  # You can mock this for now

def quiz_creator():
    st.header("🎓 Create a Quiz")

    class_selected = st.selectbox("Select Class", ["Class XI", "Class XII"])
    topic_selected = st.text_input("Topic Name (e.g., Kinematics)")

    st.subheader("📝 Add Questions")

    question = st.text_area("Question")
    options = []
    for i in range(4):
        options.append(st.text_input(f"Option {i+1}", key=f"opt_{i}"))

    correct_index = st.radio("Correct Option", [0, 1, 2, 3], format_func=lambda x: f"Option {x+1}")

    if st.button("➕ Add to Quiz"):
        if question and all(options):
            quiz_item = {
                "question": question,
                "options": options,
                "answer": options[correct_index]
            }

            # Save to database or session
            save_quiz(class_selected, topic_selected, quiz_item)
            st.success("Question added successfully!")
        else:
            st.error("Please fill in all fields.")
