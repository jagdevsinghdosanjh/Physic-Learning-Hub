import matplotlib.pyplot as plt
import streamlit as st

def render_leaderboard_chart(data):
    names = [entry['name'] for entry in data]
    scores = [entry['score'] for entry in data]

    fig, ax = plt.subplots()
    ax.barh(names, scores, color='skyblue')
    ax.set_xlabel('Score')
    ax.set_title('Leaderboard')

    st.pyplot(fig)
