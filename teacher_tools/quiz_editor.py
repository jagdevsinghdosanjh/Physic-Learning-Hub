import streamlit as st
from db.quizzes import get_quiz_by_topic, update_quiz, delete_quiz

def quiz_editor():
    st.title("🧑‍🏫 Teacher Quiz Editor")

    st.markdown("Use this tool to **edit** or **delete** quizzes by topic.")

    # Select topic
    topic = st.selectbox("Select a topic to manage", [
        "Physical World", "Units and Measurements", "Electrostatics", "Current Electricity"
    ])

    quiz = get_quiz_by_topic(topic)

    if not quiz:
        st.warning("⚠️ No quiz found for this topic.")
        return

    st.subheader(f"Editing Quiz: {topic}")
    updated_questions = []

    for i, q in enumerate(quiz["questions"]):
        st.markdown(f"### Question {i+1}")
        q_text = st.text_area("Question", value=q["question"], key=f"q{i}")
        options = [
            st.text_input(f"Option {j+1}", value=opt, key=f"opt{i}_{j}")
            for j, opt in enumerate(q["options"])
        ]
        correct = st.selectbox(
            "Correct Answer", options,
            index=options.index(q["answer"]),
            key=f"ans{i}"
        )

        updated_questions.append({
            "question": q_text,
            "options": options,
            "answer": correct
        })

    col1, col2 = st.columns(2)

    with col1:
        if st.button("💾 Save Changes"):
            success = update_quiz(topic, updated_questions)
            if success:
                st.success("✅ Quiz updated successfully!")
            else:
                st.error("❌ Failed to update quiz.")

    with col2:
        if st.button("🗑️ Delete Quiz"):
            confirm = st.checkbox("Confirm deletion")
            if confirm:
                success = delete_quiz(topic)
                if success:
                    st.warning("⚠️ Quiz deleted.")
                else:
                    st.error("❌ Failed to delete quiz.")
