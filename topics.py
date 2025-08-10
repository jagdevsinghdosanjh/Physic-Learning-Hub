# topics.py

import streamlit as st

# ------------------ Class XI ------------------
def render_physical_world():
    st.header("🌍 Physical World")
    st.write("The physical world refers to the study of natural phenomena...")
    st.subheader("Key Concepts")
    st.markdown("""
    - Observation and experimentation  
    - Scientific methods  
    - Scope of physics  
    """)

def render_units_and_measurements():
    st.header("📏 Units and Measurements")
    st.write("Understanding units is fundamental to physics...")
    st.subheader("Key Concepts")
    st.markdown("""
    - SI units  
    - Measurement errors  
    - Dimensional analysis  
    """)

# ------------------ Class XII ------------------
def render_electrostatics():
    st.header("⚡ Electrostatics")
    st.write("Electrostatics deals with electric charges at rest...")
    st.subheader("Key Concepts")
    st.markdown("""
    - Coulomb's law  
    - Electric field and potential  
    - Capacitance  
    """)

def render_current_electricity():
    st.header("🔋 Current Electricity")
    st.write("Current electricity involves the flow of electric charge...")
    st.subheader("Key Concepts")
    st.markdown("""
    - Ohm's law  
    - Resistance and circuits  
    - Kirchhoff's laws  
    """)
