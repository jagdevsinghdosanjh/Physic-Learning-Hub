import streamlit as st

# 📘 Display a single quiz question
def show_quiz_question(question_data, index):
    st.markdown(f"**Q{index + 1}: {question_data['question']}**")
    for i, option in enumerate(question_data["options"]):
        st.markdown(f"- {chr(65 + i)}. {option}")
    st.markdown(f"✅ **Answer:** {question_data['answer']}")
    st.markdown("---")

# 📚 Display assignment details
def show_assignment(assignment):
    st.markdown(f"### 📄 {assignment['title']}")
    st.markdown(f"**Topic:** {assignment['topic']}")
    if assignment.get("description"):
        st.markdown(f"**Description:** {assignment['description']}")
    if assignment.get("deadline"):
        st.markdown(f"**Deadline:** {assignment['deadline']}")
    st.markdown(f"**Uploaded On:** {assignment.get('uploaded_on', 'N/A')}")
    st.markdown("---")

# 🏅 Display leaderboard entry
def show_leaderboard_entry(username, avg_score, quiz_count, rank=None):
    medal = {0: "🥇", 1: "🥈", 2: "🥉"}.get(rank, "")
    st.markdown(f"{medal} **{username}** — Avg Score: `{avg_score:.2f}` | Quizzes Taken: `{quiz_count}`")

# 📊 Display a summary box
def show_summary(title, value, icon="ℹ️"):
    st.markdown(f"{icon} **{title}:** `{value}`")
