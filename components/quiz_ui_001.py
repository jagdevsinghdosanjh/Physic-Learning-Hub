import streamlit as st

def show_quiz():
    st.header("🧪 Quiz Section")
    st.write("Render quiz questions here...")

  q1 = render_question_block(
         "What is the SI unit of electric current?",
         ["Volt", "Ampere", "Ohm", "Coulomb"],
         correct_index=1
     )
     if q1: score += 1

     q2 = render_question_block(
         "Which law states that the current is directly proportional to voltage?",
         ["Faraday's Law", "Ohm's Law", "Kirchhoff's Law", "Lenz's Law"],
         correct_index=1
     )
     if q2: score += 1

     q3 = render_question_block(
         "What is the drift velocity of electrons?",
         ["Speed of light", "Average velocity due to electric field", "Thermal velocity", "Zero"],
         correct_index=1
     )