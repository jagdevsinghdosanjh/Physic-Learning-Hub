import streamlit as st
from utils.db import get_user_by_username
from bcrypt import checkpw

def authenticate_user():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user = get_user_by_username(username)
        if user and checkpw(password.encode(), user["password"].encode()):
            st.session_state.authenticated = True
            st.success("Login successful!")
        else:
            st.error("Invalid credentials")
