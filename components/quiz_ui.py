import streamlit as st

def render_question_block(question, options, key):
    st.write(f"**{question}**")
    return st.radio("Choose one:", options, key=key)

def show_feedback(is_correct):
    if is_correct:
        st.success("✅ Correct!")
    else:
        st.error("❌ Incorrect.")
