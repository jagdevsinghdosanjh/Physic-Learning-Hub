import streamlit as st
import matplotlib.pyplot as plt

def render(role="Student"):
    st.header("📘 Physical World and Measurement")

    # Markdown
    with open("assets/physicalworld.md", "r") as f:
        st.markdown(f.read(), unsafe_allow_html=True)

    # Graphs, videos, etc.
    # You can also show teacher-only insights:
    if role == "Teacher":
        st.info("👩‍🏫 Teacher View: Add notes or review student analytics.")


# Load Markdown Content
# with open("assets/physicalworld.md", "r") as f:
#     st.markdown(f.read(), unsafe_allow_html=True)

# Scientific Disciplines Pie Chart
st.subheader("Scientific Disciplines in Physical World")
labels = ['Physics', 'Chemistry', 'Biology', 'Astronomy', 'Geology']
sizes = [30, 25, 20, 15, 10]
colors = ['#4CAF50', '#2196F3', '#FFC107', '#FF5722', '#9C27B0']

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
ax1.set_title("Distribution of Scientific Disciplines")
st.pyplot(fig1)

# Timeline of Scientific Discoveries
st.subheader("Timeline of Major Scientific Discoveries")
years = [1600, 1700, 1800, 1900, 2000]
discoveries = [1, 3, 7, 15, 25]

fig2, ax2 = plt.subplots()
ax2.plot(years, discoveries, marker='o', linestyle='-', color='purple')
ax2.set_xlabel("Year")
ax2.set_ylabel("Number of Discoveries")
ax2.set_title("Scientific Discoveries Over Time")
ax2.grid(True)
st.pyplot(fig2)

# Video
st.subheader("Video: What is Physical World?")
st.video("https://www.youtube.com/watch?v=ZK0s2iKQk7A")
