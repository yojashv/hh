import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# 1. Web App Title and Text
st.title("Gravitational Potential Calculator")
st.write("Formula: $V = -GM/R$")
st.write("Enter values below to see the graph:")

# 2. Input Boxes (Web Style)
col1, col2 = st.columns(2)

with col1:
    # Default value is Earth's Mass (5.97e24)
    M = st.number_input("Mass of Object (kg)", value=5.97e24, format="%e")

with col2:
    # Default value is Earth's Radius (6.37e6)
    R_target = st.number_input("Distance R (meters)", value=6.37e6, format="%e")

# 3. Logic to prevent Errors
if R_target <= 0:
    st.error("Distance (R) must be greater than 0")
else:
    # 4. Calculation
    G = 6.67e-11
    V_target = - (G * M) / R_target
    
    # Display Result nicely
    st.success(f"Calculated Potential (V): {V_target:.4e} J/kg")

    # 5. Graphing
    # Create the range for the curve
    r_values = np.linspace(R_target * 0.1, R_target * 5, 1000)
    v_values = - (G * M) / r_values

    # Make the plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(r_values, v_values, label='V = -GM/R', color='blue', linewidth=2)
    ax.scatter([R_target], [V_target], color='red', zorder=5, s=100, label='Your Point')
    
    # Lines and Formatting
    ax.axvline(x=R_target, color='gray', linestyle='--', alpha=0.5)
    ax.axhline(y=V_target, color='gray', linestyle='--', alpha=0.5)
    ax.axhline(y=0, color='black', linestyle='-', linewidth=1.5, label='V=0 (Max)')
    
    ax.set_title(f'Gravitational Potential vs Distance (M={M:.2e})')
    ax.set_xlabel('Distance R (m)')
    ax.set_ylabel('Potential V (J/kg)')
    ax.grid(True, which='both', linestyle='--', alpha=0.7)
    ax.legend()

    # 6. Show Graph on Website
    st.pyplot(fig)