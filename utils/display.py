import streamlit as st

# 📘 Display a single quiz question
def show_quiz_question(question_data, index):
    with st.expander(f"Q{index + 1}: {question_data['question']}"):
        for i, option in enumerate(question_data["options"]):
            st.markdown(f"- {chr(65 + i)}. {option}")
        st.markdown(f"✅ **Answer:** {question_data['answer']}")

# 📚 Display assignment details
def show_assignment(assignment):
    with st.expander(f"📄 {assignment['title']}"):
        st.markdown(f"**Topic:** {assignment['topic']}")
        if assignment.get("description"):
            st.markdown(f"**Description:** {assignment['description']}")
        if assignment.get("deadline"):
            st.markdown(f"**Deadline:** {assignment['deadline']}")
        st.markdown(f"**Uploaded On:** {assignment.get('uploaded_on', 'N/A')}")

# 🏅 Display leaderboard entry
def show_leaderboard_entry(username, avg_score, quiz_count, rank=None):
    medal = {0: "🥇", 1: "🥈", 2: "🥉"}.get(rank, "")
    st.markdown(f"{medal} **{username}** — Avg Score: `{avg_score:.2f}` | Quizzes Taken: `{quiz_count}`")

# 📊 Display a summary box
def show_summary(title, value, icon="ℹ️"):
    st.markdown(f"{icon} **{title}:** `{value}`")

# 🧪 Interactive quiz preview (no scoring)
def preview_quiz(quiz_data):
    st.subheader(f"🧪 Preview: {quiz_data['topic']}")
    for i, q in enumerate(quiz_data["questions"]):
        with st.expander(f"Question {i + 1}"):
            st.markdown(q["question"])
            st.radio("Choose an option", q["options"], key=f"preview_{i}")

# 🗂️ Tabbed display for multiple views
def show_tabs(tab_data):
    tab_titles = list(tab_data.keys())
    tabs = st.tabs(tab_titles)
    for i, tab in enumerate(tabs):
        with tab:
            tab_data[tab_titles[i]]()
