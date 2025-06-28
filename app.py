# app.py

import streamlit as st

# --- Main Application ---
st.title("Cardio-Renal Clinical Toolkit")
st.write("An interactive tool for clinicians based on the AJKD Core Curriculum 2025 on Kidney Dysfunction in Heart Failure.")

# --- MODULE 1: INTERACTIVE DECONGESTION ALGORITHM ---
st.header("Module 1: Interactive Decongestion Algorithm")
st.markdown("This module is an interactive implementation of the diuretic escalation algorithm in Figure 4 of the manuscript.")

st.subheader("Step 1: Initial Diuretic Response")
st.write("Initial IV loop diuretic dose should be at least 2x the home dose or equivalent of furosemide 40 to 80mg IV if diuretic naive.")

# First interactive question based on the flowchart's first decision point
response1 = st.radio(
    "After the initial dose, is the adequacy of diuresis/natriuresis met? (Criteria: spot urine sodium 2 hours after diuretic dose >50-70 mEq/L OR total urine output after 6 hours ≥100-150ml/hour)",
    ('Yes, response is adequate', 'No, response is inadequate'),
    key='step1'  # Using a key is good practice for widgets
)

# Logic to display recommendations based on the user's answer
if response1 == 'Yes, response is adequate':
    st.success("Recommendation: Adequate UO/sodium output (>50-70 meq/L).")
    st.info("Plan: Repeat diuretic doses with follow up on UO/Urine Na q 6-12 hours and continue until decongestion, then switch to oral diuretic regimen.")

elif response1 == 'No, response is inadequate':
    st.warning("Recommendation: Inadequate diuresis/natriuresis.")
    st.subheader("Step 2: Escalate Diuretic Dose")

    response2 = st.radio(
        "Action: Double current loop diuretic dose. After doubling the dose, is the diuretic response now adequate?",
        ('Yes, response is now adequate', 'No, response is still inadequate'),
        key='step2'
    )

    if response2 == 'Yes, response is now adequate':
        st.success("Recommendation: Response achieved with escalated dose.")
        st.info("Plan: Continue with this dose and monitor. Repeat diuretic doses with follow up on UO/Urine Na q 6-12 hours.")

    elif response2 == 'No, response is still inadequate':
        st.warning(
            "Recommendation: Inadequate diuresis/natriuresis despite dose escalation.")
        st.subheader("Step 3: Combination Therapy")

        response3 = st.radio(
            "Action: Initiate combination diuretic therapy (add acetazolamide OR thiazide diuretic). Is the diuretic response now adequate?",
            ('Yes, response is now adequate', 'No, response remains inadequate'),
            key='step3'
        )

        if response3 == 'Yes, response is now adequate':
            st.success(
                "Recommendation: Response achieved with combination therapy.")
            st.info("Plan: Continue this regimen and monitor closely.")

        elif response3 == 'No, response remains inadequate':
            st.error(
                "Recommendation: Diuretic resistance likely. Inadequate diuresis/natriuresis persists.")
            st.subheader("Step 4: Advanced Options")
            st.markdown("""
            - **Explore other possible causes of poor diuretic response**, such as low output states. Consider a right heart catheterization.
            - If congestion persists despite the above, **consider ultrafiltration**.
            """)

# --- Add a separator for the next module ---
st.divider()
