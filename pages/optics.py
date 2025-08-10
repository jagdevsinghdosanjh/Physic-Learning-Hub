import streamlit as st
import matplotlib.pyplot as plt #noqa

def render(role="Student"):
    st.header("📘Optics")

    # Markdown
    with open("assets/optics.md", "r") as f:
        st.markdown(f.read(), unsafe_allow_html=True)

    # Graphs, videos, etc.
    # You can also show teacher-only insights:
    if role == "Teacher":
        st.info("👩‍🏫 Teacher View: Add notes or review student analytics.")


# Video
st.subheader("Video: Reflection, Refraction & Lenses")
st.video("https://www.youtube.com/watch?v=1yGJvSx1fJQ")
