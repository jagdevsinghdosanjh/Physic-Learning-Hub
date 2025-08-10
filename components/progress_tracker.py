from datetime import datetime
import streamlit as st

def save_progress(db, user_id, topic_id, score, total):
    if st.button("💾 Save Progress"):
        db.progress.update_one(
            {"user_id": user_id, "topic_id": topic_id},
            {"$set": {
                "quizzes_attempted": total,
                "correct_answers": score,
                "last_attempt": datetime.utcnow(),
                "score": int((score / total) * 100)
            }},
            upsert=True
        )
        st.success("Progress saved!")
