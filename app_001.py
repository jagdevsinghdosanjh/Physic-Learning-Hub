import streamlit as st
from components.topic_selector import select_topic
from utils import topic_module #noqa
from utils.db import get_db_connection  # MongoDB connector
from teacher_tools.content_browser import content_browser

content_browser()


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
db = get_db_connection()  # ✅ No truth value testing

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

# import streamlit as st
# from components.topic_selector import select_topic
# from utils import topic_module
# from utils.db import get_db_connection # Your MongoDB connector



# # App Title
# st.set_page_config(page_title="Physics Learning Hub", layout="wide")
# st.title("🧪 Physics Learning Hub")

# # 🔐 Role Selection
# role = st.sidebar.radio("Select Role", ["Student", "Teacher"])
# st.sidebar.success(f"Logged in as: {role}")
# topics = topic_module.get_topics_by_role(role)

# # 🧼 Session Cleanup
# if st.sidebar.button("🔄 Reset Session"):
#     for key in st.session_state.keys():
#         del st.session_state[key]
#     st.sidebar.success("Session state cleared.")
#     st.experimental_rerun()

# # 🔗 Connect to MongoDB
# db = get_db_connection()

# # 📚 Topic Selection
# topic_id, topic_title = select_topic(db, role)

# # 🧠 Load Topic Module Dynamically
# try:
#     exec(f"import pages.{topic_id} as topic_module")
#     topic_module.render(role=role)  # Optional: pass role to module
# except ModuleNotFoundError:
#     st.error(f"🚫 Module for topic '{topic_title}' not found.")
# except Exception as e:
#     st.error(f"⚠️ Error loading topic: {e}")

# # import streamlit as st
# # from utils.db import get_db
# # from components.topic_selector import select_topic
# # from components.quiz_component import run_quiz
# # from components.progress_tracker import save_progress
# # from components.leaderboard import show_leaderboard

# # db = get_db()
# # st.set_page_config(page_title="Physics Learning Hub", layout="wide")
# # st.title("📘 Physics Learning Hub")

# # user_id = "stu_001"  # Replace with session-based logic later
# # topic_id, topic_title = select_topic(db)
# # score, total = run_quiz(db, topic_id)
# # save_progress(db, user_id, topic_id, score, total)
# # show_leaderboard(db)
