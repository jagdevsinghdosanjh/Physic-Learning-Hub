import streamlit as st
import matplotlib.pyplot as plt

def render(role="Student"):
    st.header("📘 Magnetism")

    # Markdown
    with open("assets/magnetism.md", "r") as f:
        st.markdown(f.read(), unsafe_allow_html=True)

    # Graphs, videos, etc.
    # You can also show teacher-only insights:
    if role == "Teacher":
        st.info("👩‍🏫 Teacher View: Add notes or review student analytics.")


# Load Markdown Content
# with open("assets/magnetism.md", "r") as f:
#     st.markdown(f.read(), unsafe_allow_html=True)

# Video
st.subheader("Video: Magnetic Fields & Lorentz Force")
st.video("https://www.youtube.com/watch?v=5Zg-C8AAIGg")
