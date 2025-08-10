import streamlit as st
from components.sidebar import render_sidebar
from components.dashboard_ui import show_dashboard
from components.quiz_ui import show_quiz
from components.calendar_ui import show_calendar
from utils.auth import authenticate_user
from utils.session import init_session
from teacher_tools.content_browser import content_browser

content_browser()


# Initialize session state
init_session()

# Sidebar navigation
page = render_sidebar()

# Authentication gate (optional)
if not st.session_state.get("authenticated", False):
    authenticate_user()
else:
    if page == "Dashboard":
        show_dashboard()
    elif page == "Quiz":
        show_quiz()
    elif page == "Calendar":
        show_calendar()
