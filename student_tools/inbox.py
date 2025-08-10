import streamlit as st
from db.messages import get_messages_for_student

def inbox(username):
    st.title("📥 My Inbox")

    messages = get_messages_for_student(username)
    if not messages:
        st.info("No messages yet.")
        return

    for msg in sorted(messages, key=lambda m: m["timestamp"], reverse=True):
        st.markdown(f"**{msg['timestamp'][:10]}** — {msg['message']}")
