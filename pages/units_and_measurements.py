import streamlit as st

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

st.info("🧠 Tip for Students: Dimensional analysis is your secret weapon for checking equations — use it often!")
