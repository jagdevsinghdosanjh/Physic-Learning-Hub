import streamlit as st

# def select_topic(db=None, role="Student"):
#     st.sidebar.header("📚 Topic Selection")

#     # Static fallback topics
#     static_topics = {
#         "Physical World": "physicalworld",
#         "Units & Measurements": "units_measurements",
#         "Kinematics": "kinematics",
#         "Laws of Motion": "laws_of_motion",
#         "Work, Energy & Power": "work_energy_power"
#     }

def select_topic(db=None, role="Student"):
    st.sidebar.header("📚 Topic Selection")

    static_topics = {
        "Physical World": "physicalworld",
        "Units & Measurements": "units_measurements",
        "Kinematics": "kinematics",
        "Laws of Motion": "laws_of_motion"
    }

    topic_map = {}
    if db is not None:
        try:
            collection = db["topics"]
            query = {} if role == "Teacher" else {"visible_to": {"$in": [role, "All"]}}
            topics = collection.find(query)
            for topic in topics:
                topic_map[topic["title"]] = topic["id"]
        except Exception as e:
            st.sidebar.error(f"⚠️ Error loading topics from DB: {e}")
            topic_map = static_topics
    else:
        topic_map = static_topics

    selected_title = st.sidebar.selectbox("Choose a topic", ["-- Select --"] + list(topic_map.keys()))

    if selected_title == "-- Select --":
        st.sidebar.warning("Please select a topic to continue.")
        st.stop()

    return topic_map[selected_title], selected_title


    # Load from MongoDB if available
    topic_map = {}
    if db is not None:
    # proceed with MongoDB logic
        try:
            collection = db["topics"]
            query = {} if role == "Teacher" else {"visible_to": "Student"}
            topics = collection.find(query)
            for topic in topics:
                topic_map[topic["title"]] = topic["id"]
        except Exception as e:
            st.sidebar.error(f"⚠️ Error loading topics from DB: {e}")
            topic_map = static_topics
    else:
        topic_map = static_topics

    # Topic selection
    selected_title = st.sidebar.selectbox("Choose a topic", ["-- Select --"] + list(topic_map.keys()))

    if selected_title == "-- Select --":
        st.sidebar.warning("Please select a topic to continue.")
        st.stop()

    return topic_map[selected_title], selected_title

# def select_topic(db):
#     topics = list(db.topics.find({}, {"_id": 0, "topic_id": 1, "title": 1}))
#     topic_map = {t["title"]: t["topic_id"] for t in topics}
#     selected_title = st.selectbox("📚 Choose a Topic", list(topic_map.keys()))
#     return topic_map[selected_title], selected_title
