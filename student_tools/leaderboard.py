import streamlit as st
import pandas as pd
from db.progress import get_all_scores_all_students
from utils.badges import rank_badge

def leaderboard():
    st.title("🏆 Leaderboard with Badges")

    df = pd.DataFrame(get_all_scores_all_students())
    if df.empty:
        st.info("No quiz data available.")
        return

    leaderboard_df = df.groupby("username")["score"].mean().reset_index()
    leaderboard_df["badge"] = leaderboard_df["score"].apply(rank_badge)
    leaderboard_df = leaderboard_df.sort_values(by="score", ascending=False).head(10)

    st.subheader("Top Performers")
    st.table(leaderboard_df.rename(columns={"username": "Student", "score": "Avg Score (%)", "badge": "🏅 Badge"}))


# import streamlit as st
# import pandas as pd
# from db.progress import get_all_scores_all_students

# def leaderboard():
#     st.title("🏆 Leaderboard")

#     df = pd.DataFrame(get_all_scores_all_students())
#     if df.empty:
#         st.info("No quiz data available.")
#         return

#     leaderboard_df = df.groupby("username")["score"].mean().reset_index()
#     leaderboard_df = leaderboard_df.sort_values(by="score", ascending=False).head(10)

#     st.subheader("Top Performers")
#     st.table(leaderboard_df.rename(columns={"username": "Student", "score": "Avg Score (%)"}))
