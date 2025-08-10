import streamlit as st

def show_leaderboard(db, class_name="XI"):
    st.subheader("🏆 Leaderboard")
    board = db.leaderboard.find_one({"class": class_name}, {"_id": 0})
    if board:
        for rank, student in enumerate(board["top_students"], start=1):
            st.write(f"{rank}. {student['user_id']} — {student['score']} pts")
