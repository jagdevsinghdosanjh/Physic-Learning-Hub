import streamlit as st

def run_quiz(db, topic_id):
    quizzes = list(db.quizzes.find({"topic_id": topic_id}, {"_id": 0}))
    score = 0
    st.subheader("🧪 Quiz Time")

    for q in quizzes:
        st.markdown(f"**{q['question']}**")
        selected = st.radio(f"Choose answer for {q['quiz_id']}", q["options"], key=q["quiz_id"])
        if st.button(f"Submit {q['quiz_id']}"):
            if selected == q["answer"]:
                st.success("✅ Correct!")
                score += 1
            else:
                st.error(f"❌ Incorrect. {q['explanation']}")
    return score, len(quizzes)

def get_score(responses, answers):
    return sum([r == a for r, a in zip(responses, answers)])

def reset_quiz_state(n, key_prefix):
    for i in range(n):
        st.session_state.pop(f"{key_prefix}_{i}", None)