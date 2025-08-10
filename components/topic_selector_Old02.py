import streamlit as st

# Optional: Add emojis for visual flair
TOPIC_ICONS = {
    "Physical World": "🌌",
    "Units & Measurements": "📏",
    "Kinematics": "🏃‍♂️",
    "Laws of Motion": "⚖️"
}

STATIC_TOPICS = {
    "Physical World": "physicalworld",
    "Units & Measurements": "units_measurements",
    "Kinematics": "kinematics",
    "Laws of Motion": "laws_of_motion"
}

@st.cache_data(show_spinner=False)
def fetch_topics_from_db(db, role):
    """Fetch topics from MongoDB with role-based filtering."""
    topic_map = {}
    try:
        collection = db["topics"]
        query = {} if role == "Teacher" else {"visible_to": {"$in": [role, "All"]}}
        topics = collection.find(query)

        for topic in topics:
            title = topic.get("title", "Untitled")
            topic_id = topic.get("id", "unknown_id")
            icon = TOPIC_ICONS.get(title, "📘")
            topic_map[f"{icon} {title}"] = topic_id

    except Exception as e:
        st.sidebar.error(f"⚠️ DB error: {e}")

    return topic_map if topic_map else {
        f"{TOPIC_ICONS.get(title, '📘')} {title}": id
        for title, id in STATIC_TOPICS.items()
    }

def select_topic(db=None, role="Student"):
    """Sidebar topic selector with caching and emojis."""
    st.sidebar.header("📚 Topic Selection")

    topic_map = fetch_topics_from_db(db, role) if db is not None else {
        f"{TOPIC_ICONS.get(title, '📘')} {title}": id
        for title, id in STATIC_TOPICS.items()
    }

    selected_title = st.sidebar.selectbox("Choose a topic", ["-- Select --"] + list(topic_map.keys()))

    if selected_title == "-- Select --":
        st.sidebar.warning("Please select a topic to continue.")
        st.stop()

    return topic_map[selected_title], selected_title.split(" ", 1)[-1]  # Return clean title
