import streamlit as st
import matplotlib.pyplot as plt #noqa

def render(role="Student"):
    st.header("📘Electrostatics")

    # Markdown
    with open("assets/electrostatics.md", "r") as f:
        st.markdown(f.read(), unsafe_allow_html=True)

    # Graphs, videos, etc.
    # You can also show teacher-only insights:
    if role == "Teacher":
        st.info("👩‍🏫 Teacher View: Add notes or review student analytics.")


# Load Markdown Content
# with open("assets/electrostatics.md", "r") as f:
#     st.markdown(f.read(), unsafe_allow_html=True)

# Video
st.subheader("Video: Coulomb's Law & Electric Fields")
st.video("https://www.youtube.com/watch?v=Yt2WqgGzQWk")
