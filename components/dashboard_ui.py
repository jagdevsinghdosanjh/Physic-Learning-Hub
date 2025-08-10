import streamlit as st
from utils.charts import render_leaderboard_chart

def show_dashboard():
    st.header("📊 Dashboard")
    render_leaderboard_chart()
