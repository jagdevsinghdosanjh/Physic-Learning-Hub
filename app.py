import streamlit as st
from components.topic_selector import select_topic
from utils import topic_module
from utils.db import get_db_connection
from teacher_tools.content_browser import content_browser

# 🧪 App Title & Layout
st.set_page_config(page_title="Physics Learning Hub", layout="wide")
st.title("🧪 Physics Learning Hub")

# 🔐 Role Selection
role = st.sidebar.radio("Select Role", ["Student", "Teacher"])
st.sidebar.success(f"Logged in as: {role}")

# 🧼 Session Cleanup
if st.sidebar.button("🔄 Reset Session"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.sidebar.success("Session state cleared.")
    st.experimental_rerun()

# 🔗 Connect to MongoDB
db = get_db_connection()

# 📚 Topic Selection
topic_id, topic_title = select_topic(db, role)

# 🧠 Load Topic Module Dynamically
try:
    module_path = f"pages.{topic_id}"
    topic_mod = __import__(module_path, fromlist=["render"])
    topic_mod.render(role=role)
except ModuleNotFoundError:
    st.error(f"🚫 Module for topic '{topic_title}' not found.")
except Exception as e:
    st.error(f"⚠️ Error loading topic: {e}")

# ✅ Show Content Browser only for Teachers
if role == "Teacher":
    content_browser()
