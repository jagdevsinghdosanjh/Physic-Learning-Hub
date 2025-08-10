import streamlit as st

def render_sidebar():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Dashboard", "Quiz", "Calendar"])
    st.session_state.page = page
    return page
