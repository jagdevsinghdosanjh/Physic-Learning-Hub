# main.py

import streamlit as st
from topics import (
    render_physical_world,
    render_units_and_measurements,
    render_electrostatics,
    render_current_electricity
)
from teacher_tools.quiz_creator import quiz_creator

# ✅ Must be the first Streamlit command
st.set_page_config(page_title="Physics Learning Hub", layout="wide")

# ------------------ SESSION INITIALIZATION ------------------
if "user" not in st.session_state:
    st.session_state["user"] = None
if "role" not in st.session_state:
    st.session_state["role"] = None

# ------------------ LOGIN / SIGNUP INTERFACE ------------------
if st.session_state["user"] is None:
    st.title("🔐 Login / Sign Up")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Login")
        username = st.text_input("Username", key="login_user")
        password = st.text_input("Password", type="password", key="login_pass")
        role = st.selectbox("Role", ["student", "teacher"], key="login_role")
        if st.button("Login"):
            # ✅ Replace with real authentication logic
            if username and password:
                st.session_state["user"] = username
                st.session_state["role"] = role
                st.success(f"Welcome back, {username} ({role})!")
                st.experimental_rerun()
            else:
                st.error("Invalid credentials.")

    with col2:
        st.subheader("Sign Up")
        new_username = st.text_input("New Username", key="signup_user")
        new_password = st.text_input("New Password", type="password", key="signup_pass")
        new_role = st.selectbox("Role", ["student", "teacher"], key="signup_role")
        if st.button("Create Account"):
            # ✅ Replace with real account creation logic
            if new_username and new_password:
                st.success(f"Account created for {new_username} as {new_role}. Please log in.")
            else:
                st.error("Please enter a username and password.")
else:
    # ------------------ DASHBOARD ------------------
    st.title("📘 Senior School Physics Learning Hub")

    # 🔓 Logout button
    logout_col, _ = st.columns([1, 5])
    with logout_col:
        if st.button("🚪 Logout"):
            st.session_state["user"] = None
            st.session_state["role"] = None
            st.experimental_rerun()

    st.success(f"Welcome back, {st.session_state['user']} ({st.session_state['role']})!")

    # ------------------ STUDENT DASHBOARD ------------------
    if st.session_state["role"] == "student":
        class_selected = st.selectbox("Select Class", ["Class XI", "Class XII"])
        st.subheader("Choose a Topic")

        if class_selected == "Class XI":
            col1, col2 = st.columns(2)
            with col1:
                if st.button("🌍 Physical World"):
                    render_physical_world()
            with col2:
                if st.button("📏 Units and Measurements"):
                    render_units_and_measurements()

        elif class_selected == "Class XII":
            col1, col2 = st.columns(2)
            with col1:
                if st.button("⚡ Electrostatics"):
                    render_electrostatics()
            with col2:
                if st.button("🔋 Current Electricity"):
                    render_current_electricity()

    # ------------------ TEACHER DASHBOARD ------------------
    elif st.session_state["role"] == "teacher":
        st.subheader("👩‍🏫 Teacher Dashboard")
        st.markdown("""
        - 📊 View student progress  
        - 📝 Upload assignments  
        - 🎓 Create quizzes  
        - 📁 Manage content  
        """)

        with st.expander("🎓 Create Quizzes"):
            quiz_creator()

        st.info("Teacher tools coming soon! Let me know what you'd like to add.")
