import streamlit as st # noqa

st.set_page_config(page_title="Current Electricity", layout="wide")

st.title("🔌 Current Electricity – Class 12 Physics")
st.markdown("Explore key concepts, derivations, and problem-solving techniques through curated video resources.")

# Role-based access (example)
role = st.sidebar.selectbox("Select Role", ["Student", "Teacher"])

# Video Embeds
videos = {
    "Complete Derivations & Concepts": "https://www.youtube.com/embed/59259QKLJ2c",
    "Fast-Paced Summary": "https://www.youtube.com/embed/S9hU_GjfNFQ",
    "Deep Dive with Time-Stamps": "https://www.youtube.com/embed/zPFiGJPRAhI",
    "NEET/JEE Crash Course Style": "https://www.youtube.com/embed/OPlHTsn7lsg",
    "Visual + Conceptual Clarity": "https://www.youtube.com/embed/OHoL5Sf5pII"
}

for title, url in videos.items():
    st.subheader(f"🎥 {title}")
    st.video(url)

# Optional: Quiz Launcher
if role == "Student":
    st.markdown("### 🧠 Ready to test your understanding?")
    if st.button("Launch Quiz"):
        st.success("Quiz module coming soon!")

# Teacher-only section
if role == "Teacher":
    st.markdown("### 📊 Teacher Dashboard")
    st.info("Analytics and student progress tracking will be available here.")

# import streamlit as st
# import matplotlib.pyplot as plt #noqa

# def render(role="Student"):
#     st.header("📘 Current Electricity")

#     # Markdown
#     with open("assets/currentelectricity.md", "r") as f:
#         st.markdown(f.read(), unsafe_allow_html=True)

#     # Graphs, videos, etc.
#     # You can also show teacher-only insights:
#     if role == "Teacher":
#         st.info("👩‍🏫 Teacher View: Add notes or review student analytics.")


# # Load Markdown Content
# with open("assets/currentelectricity.md", "r") as f:
#     st.markdown(f.read(), unsafe_allow_html=True)

# # Video
# st.subheader("Video: Ohm's Law & Circuits")
# st.video("https://www.youtube.com/watch?v=Zz4ZzjJ4KzI")
