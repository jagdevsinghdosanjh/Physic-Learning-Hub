from components import quiz_ui #noqa
from components.quiz import render_quiz  # Assumes reusable quiz component
import streamlit as st
import os # noqa

st.set_page_config(page_title="Units and Measurements", page_icon="📏", layout="wide")

st.title("📏 Units and Measurements")

with st.expander("🧠 Learning Objectives", expanded=True):
    st.markdown("""
    - Understand the need for measurement and standard units.
    - Learn SI units and their conventions.
    - Explore dimensional analysis and its applications.
    - Estimate errors and uncertainties in measurements.
    """)

with st.expander("📚 1. Introduction to Measurement"):
    st.markdown("""
    Measurement is the comparison of an unknown quantity with a known standard.  
    Physics relies on precise measurements to describe natural phenomena.
    """)

with st.expander("🧪 2. Fundamental and Derived Units"):
    st.subheader("🔹 Fundamental Quantities (SI Base Units)")
    st.markdown("""
    | Quantity             | Unit     | Symbol |
    |----------------------|----------|--------|
    | Length               | metre    | m      |
    | Mass                 | kilogram | kg     |
    | Time                 | second   | s      |
    | Temperature          | kelvin   | K      |
    | Electric Current     | ampere   | A      |
    | Luminous Intensity   | candela  | cd     |
    | Amount of Substance  | mole     | mol    |
    """)
    st.subheader("🔸 Derived Units")
    st.markdown("""
    Examples include:
    - Velocity: `m/s`
    - Acceleration: `m/s²`
    - Force: newton (N) = `kg·m/s²`
    """)

with st.expander("📐 3. Dimensional Analysis"):
    st.subheader("✅ Applications")
    st.markdown("""
    - Checking correctness of equations  
    - Converting units  
    - Deriving relationships  
    """)
    st.subheader("🧮 Example")
    st.markdown("Check if the equation is dimensionally correct:")
    st.latex(r"v = u + at")
    st.latex(r"[v] = [u] = LT^{-1}")
    st.latex(r"[a] = LT^{-2},\quad [t] = T")
    st.latex(r"[at] = LT^{-2} \cdot T = LT^{-1}")
    st.success("✅ Dimensions match → equation is valid.")

with st.expander("📊 4. Accuracy, Precision & Errors"):
    st.subheader("🔍 Types of Errors")
    st.markdown("""
    - **Systematic Error**: Consistent bias (e.g., faulty instrument)  
    - **Random Error**: Varies unpredictably  
    - **Gross Error**: Human mistakes  
    """)
    st.subheader("📈 Error Estimation")
    st.latex(r"\Delta x = |x_{\text{measured}} - x_{\text{true}}|")
    st.latex(r"\text{Relative Error} = \frac{\Delta x}{x_{\text{true}}}")
    st.latex(r"\text{Percentage Error} = \frac{\Delta x}{x_{\text{true}}} \times 100\%")

with st.expander("🧩 5. Significant Figures"):
    st.markdown("""
    - Reflect precision of measurement.  
    - Rules:
        - All non-zero digits are significant.  
        - Zeros between significant digits are significant.  
        - Trailing zeros in decimal are significant.  
    """)
    st.subheader("✏️ Examples")
    st.markdown("""
    - `0.00450` → 3 significant figures  
    - `1200` → 2 significant figures (unless specified)  
    """)

with st.expander("🔗 References"):
    st.markdown("""
    - NCERT Physics Class XI Chapter 2  
    - NIST SI Units Guide  
    - IAPT Physics Olympiad Resources  
    """)
    
def render(role="Student"):
    st.title("📏 Units and Measurements")

    # # Render markdown content
    # md_content = load_markdown("unitsandmeasurements")
    # st.markdown(md_content, unsafe_allow_html=True)

    # Role-specific view
    if role == "Teacher":
        st.info("👩‍🏫 Teacher View: Add notes, track student progress, or review analytics.")

    # Divider and quiz
    st.divider()
    st.subheader("🧠 Test Your Understanding")

    quiz_data = [
        {
            "question": "Which of the following is a fundamental quantity?",
            "options": ["Velocity", "Force", "Mass", "Acceleration"],
            "answer": "Mass"
        },
        {
            "question": "Dimensional formula of energy?",
            "options": ["ML^2T^-2", "MLT^-1", "M^2L^2T^-2", "ML^-1T^-2"],
            "answer": "ML^2T^-2"
        },
        {
        "question": "Which of the following is a fundamental quantity?",
        "options": ["Velocity", "Force", "Mass", "Acceleration"],
        "answer": "Mass"
    },
    {
        "question": "Dimensional formula of energy?",
        "options": ["ML^2T^-2", "MLT^-1", "M^2L^2T^-2", "ML^-1T^-2"],
        "answer": "ML^2T^-2"
    },
    {
        "question": "Which physical quantity has the dimensional formula ML^-1T^-2?",
        "options": ["Pressure", "Work", "Force", "Acceleration"],
        "answer": "Pressure"
    },
    {
        "question": "Which of the following is not a vector quantity?",
        "options": ["Displacement", "Velocity", "Speed", "Acceleration"],
        "answer": "Speed"
    },
    {
        "question": "What is the SI unit of power?",
        "options": ["Joule", "Watt", "Newton", "Pascal"],
        "answer": "Watt"
    },
    {
        "question": "Which law states that the rate of change of momentum is proportional to the applied force?",
        "options": ["Newton's First Law", "Newton's Second Law", "Newton's Third Law", "Law of Conservation of Energy"],
        "answer": "Newton's Second Law"
    },
    {
        "question": "Which quantity is conserved in an elastic collision?",
        "options": ["Momentum only", "Kinetic energy only", "Both momentum and kinetic energy", "Potential energy"],
        "answer": "Both momentum and kinetic energy"
    },
    {
        "question": "Which of the following has no dimensions?",
        "options": ["Strain", "Stress", "Force", "Velocity"],
        "answer": "Strain"
    },
    {
        "question": "What is the dimensional formula of impulse?",
        "options": ["MLT^-2", "MLT^-1", "ML^2T^-2", "ML^2T^-3"],
        "answer": "MLT^-1"
    },
    {
        "question": "Which instrument is used to measure atmospheric pressure?",
        "options": ["Thermometer", "Barometer", "Manometer", "Hygrometer"],
        "answer": "Barometer"
    },
    {
        "question": "Which of the following is a scalar quantity?",
        "options": ["Displacement", "Acceleration", "Work", "Velocity"],
        "answer": "Work"
    },
    {
        "question": "What is the unit of gravitational constant G?",
        "options": ["Nm^2/kg^2", "N/kg", "m/s^2", "kg/m^2"],
        "answer": "Nm^2/kg^2"
    },
    {
        "question": "Which of the following quantities is dimensionless?",
        "options": ["Refractive index", "Force", "Energy", "Momentum"],
        "answer": "Refractive index"
    },
    {
        "question": "Which of the following is the correct dimensional formula for pressure?",
        "options": ["ML^-1T^-2", "MLT^-2", "ML^2T^-2", "M^2L^-2T^-2"],
        "answer": "ML^-1T^-2"
    },
    {
        "question": "Which physical quantity has the unit 'Pascal'?",
        "options": ["Power", "Pressure", "Energy", "Force"],
        "answer": "Pressure"
    }
    ]
    render_quiz(quiz_data)

    # Tip
    st.info("💡 Dimensional analysis helps verify equations and derive relationships. Use it often!")
    st.info("🧠 Tip for Students: Dimensional analysis is your secret weapon for checking equations — use it often!")
