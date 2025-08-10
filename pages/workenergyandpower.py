import streamlit as st
import matplotlib.pyplot as plt

def render(role="Student"):
    st.header("📘 Work, Energy, and Power")

    # Markdown
    with open("assets/workenergyandpower.md", "r") as f:
        st.markdown(f.read(), unsafe_allow_html=True)

    # Graphs, videos, etc.
    # You can also show teacher-only insights:
    if role == "Teacher":
        st.info("👩‍🏫 Teacher View: Add notes or review student analytics.")

# Video
st.subheader("Video: Work, Energy & Power")
st.video("https://www.youtube.com/watch?v=4cGJZQYqR3g")
