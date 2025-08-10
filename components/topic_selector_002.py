import streamlit as st

# 🎯 Topic Icons
TOPIC_ICONS = {
    "Physical World": "🌌",
    "Units And Measurements": "📏",
    "Kinematics": "🏃‍♂️",
    "Laws of Motion": "⚖️",
    "Work, Energy and Power": "🔋",
    "Electrostatics": "⚡",  # ✅ Fixed typo
    "Current Electricity": "🔌",
    "Magnetism": "🧲",
    "Optics and Optical Instruments": "🔍"
}

# 🧪 Static Topic Mapping
STATIC_TOPICS = {
    "Physical World": "physicalworld",
    "Units And Measurements": "unitsandmeasurements",
    "Kinematics": "kinematics",
    "Laws of Motion": "lawsofmotion",
    "Work, Energy and Power": "workenergyandpower",
    "Electrostatics": "electrostatics",  # ✅ Fixed typo
    "Current Electricity": "currentelectricity",
    "Magnetism": "magnetism",
    "Optics and Optical Instruments": "optics"
}

@st.cache_data(show_spinner=False)
def fetch_topics_from_db(_db, role):
    """Fetch topics from MongoDB with role-based filtering."""
    topic_map = {}
    try:
        collection = _db["topics"]
        query = {} if role == "Teacher" else {"visible_to": {"$in": [role, "All"]}}
        topics = collection.find(query)

        for topic in topics:
            title = topic.get("title", "Untitled")
            topic_id = topic.get("id", "unknown_id")
            icon = TOPIC_ICONS.get(title, "📘")
            topic_map[f"{icon} {title}"] = topic_id

    except Exception as e:
        st.sidebar.error(f"⚠️ DB error: {e}")

    # Fallback to static topics if DB fails or returns empty
    if not topic_map:
        topic_map = {
            f"{TOPIC_ICONS.get(title, '📘')} {title}": id
            for title, id in STATIC_TOPICS.items()
        }

    return topic_map

def extract_title(label):
    """Extract topic title from emoji-prefixed label."""
    return label[label.find(" ") + 1:] if " " in label else label

def select_topic(db=None, role="Student"):
    """Sidebar topic selector with emojis and fallback."""
    st.sidebar.header("📚 Topic Selection")
    st.sidebar.caption("🔍 Select a topic to explore its concepts, quizzes, and visualizations.")

    topic_map = fetch_topics_from_db(db, role) if db else {
        f"{TOPIC_ICONS.get(title, '📘')} {title}": id
        for title, id in STATIC_TOPICS.items()
    }

    sorted_keys = sorted(topic_map.keys(), key=lambda x: x.lower())
    selected_label = st.sidebar.selectbox("Choose a topic", ["-- Select --"] + sorted_keys)

    if selected_label == "-- Select --":
        st.sidebar.warning("Please select a topic to continue.")
        st.stop()

    topic_id = topic_map[selected_label]
    topic_title = extract_title(selected_label)

    return topic_id, topic_title
