import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def simulate_projectile(v0, angle_deg):
    angle_rad = np.radians(angle_deg)
    g = 9.8
    t_flight = 2 * v0 * np.sin(angle_rad) / g
    t = np.linspace(0, t_flight, num=100)
    x = v0 * np.cos(angle_rad) * t
    y = v0 * np.sin(angle_rad) * t - 0.5 * g * t**2

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel("Distance (m)")
    ax.set_ylabel("Height (m)")
    ax.set_title("Projectile Motion")
    st.pyplot(fig)

st.subheader("🎯 Projectile Motion Simulator")
v0 = st.slider("Initial Velocity (m/s)", 0, 100, 50)
angle = st.slider("Launch Angle (°)", 0, 90, 45)
simulate_projectile(v0, angle)
