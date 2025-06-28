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
# app.py (add this code to the end of the file)

# --- MODULE 2: GDMT NAVIGATOR ---
st.header("Module 2: Guideline-Directed Medical Therapy (GDMT) Navigator")
st.markdown("This tool shows the level of evidence for HFrEF therapies based on the patient's CKD stage, as summarized in Figure 6 of the manuscript.")

# The data from Figure 6 is stored in a Python dictionary
gdmt_data = {
    "CKD 1 and 2": {
        "Beta Blocker": "Strong",
        "MRA": "Strong",
        "Non-steroidal MRA": "Strong",
        "ARNI": "Strong",
        "ACEi/ARB": "Strong",
        "Diuretics": "Absent",
        "SGLT2i": "Strong",
    },
    "CKD 3": {
        "Beta Blocker": "Strong",
        "MRA": "Strong",
        "Non-steroidal MRA": "Strong",
        "ARNI": "Strong",
        "ACEi/ARB": "Strong",
        "Diuretics": "Absent",
        "SGLT2i": "Strong",
    },
    "CKD 4": {
        "Beta Blocker": "Limited",
        "MRA": "Limited",
        "Non-steroidal MRA": "Strong (up to eGFR> 25 cc/min)",
        "ARNI": "Limited",
        "ACEi/ARB": "Limited",
        "Diuretics": "Absent",
        "SGLT2i": "Strong (eGFR> 20 cc/min)",
    },
    "CKD 5": {
        "Beta Blocker": "Absent",
        "MRA": "Absent",
        "Non-steroidal MRA": "Absent",
        "ARNI": "Absent",
        "ACEi/ARB": "Absent",
        "Diuretics": "Absent",
        "SGLT2i": "Limited",
    }
}

# Create a dropdown menu (selectbox) for the user to choose the CKD stage
ckd_stage = st.selectbox(
    "Select the patient's CKD Stage:",
    options=list(gdmt_data.keys()),
    index=None,
    placeholder="Choose a CKD Stage..."
)

# Display the recommendations if a stage is selected
if ckd_stage:
    st.subheader(f"Recommendations for {ckd_stage}")

    # Get the specific data for the selected stage
    recommendations = gdmt_data[ckd_stage]

    # Display each therapy and its evidence level
    for therapy, evidence in recommendations.items():
        if evidence == "Strong":
            st.markdown(
                f"- **{therapy}:** <span style='color:green;'>**{evidence}**</span>", unsafe_allow_html=True)
        elif evidence == "Limited":
            st.markdown(
                f"- **{therapy}:** <span style='color:orange;'>**{evidence}**</span>", unsafe_allow_html=True)
        elif "Strong (up to" in evidence or "Strong (eGFR>" in evidence:
            st.markdown(
                f"- **{therapy}:** <span style='color:green;'>**{evidence}**</span>", unsafe_allow_html=True)
        else:  # Absent
            st.markdown(
                f"- **{therapy}:** <span style='color:red;'>**{evidence}**</span>", unsafe_allow_html=True)

# --- Add another separator for the next module ---
st.divider()
