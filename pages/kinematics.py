import streamlit as st
import matplotlib.pyplot as plt

def render(role="Student"):
    st.header("📘 Kinematics")

    # Markdown
    with open("assets/kinematics.md", "r") as f:
        st.markdown(f.read(), unsafe_allow_html=True)

    # Graphs, videos, etc.
    # You can also show teacher-only insights:
    if role == "Teacher":
        st.info("👩‍🏫 Teacher View: Add notes or review student analytics.")


# Load Markdown Content
# with open("assets/kinematics.md", "r") as f:
#     st.markdown(f.read(), unsafe_allow_html=True)

# Displacement-Time Graph
st.subheader("Displacement-Time Graph")
time = [0, 1, 2, 3, 4, 5]
displacement = [0, 2, 4, 6, 8, 10]

fig, ax = plt.subplots()
ax.plot(time, displacement, marker='o', color='blue')
ax.set_xlabel("Time (s)")
ax.set_ylabel("Displacement (m)")
ax.set_title("Displacement vs Time")
ax.grid(True)
st.pyplot(fig)

# Velocity-Time Graph
st.subheader("Velocity-Time Graph")
velocity = [0, 4, 8, 12, 16, 20]

fig2, ax2 = plt.subplots()
ax2.plot(time, velocity, marker='s', color='green')
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Velocity (m/s)")
ax2.set_title("Velocity vs Time")
ax2.grid(True)
st.pyplot(fig2)

# Video
st.subheader("Video: Introduction to Kinematics")
st.video("https://www.youtube.com/watch?v=ZihywtixUYo")
