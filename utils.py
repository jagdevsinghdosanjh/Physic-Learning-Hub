import matplotlib.pyplot as plt
import streamlit as st

def show_progress_chart(score, total):
    """Displays a bar chart of correct vs incorrect answers."""
    st.markdown("### 📊 Your Score")
    fig, ax = plt.subplots()
    ax.bar(["Correct", "Incorrect"], [score, total - score], color=["green", "red"])
    ax.set_ylim(0, total)
    st.pyplot(fig)

def format_topic_name(topic):
    """Converts topic name to filename-friendly format."""
    return topic.lower().replace(" ", "_").replace(",", "").replace("&", "and")

def display_success(message):
    """Displays a success message with a checkmark."""
    st.success(f"✅ {message}")

def display_error(message):
    """Displays an error message with a cross."""
    st.error(f"❌ {message}")
