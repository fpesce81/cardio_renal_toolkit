# app.py

import streamlit as st

# --- Main Application ---
st.set_page_config(layout="wide")  # Use a wider layout for better readability
st.title("Cardio-Renal Clinical Toolkit")

st.markdown(
    'This is an interactive application based on the manuscript: [*Kidney Dysfunction in Heart Failure: Core Curriculum 2025*](https://www.ajkd.org/article/S0272-6386(25)00691-2/fulltext)')

st.divider()

# --- MODULE 1: INTERACTIVE DECONGESTION ALGORITHM ---
st.header("Module 1: Interactive Decongestion Algorithm")
st.markdown("This module is an interactive implementation of the diuretic escalation algorithm in Figure 4 of the manuscript.")

st.subheader("Step 1: Initial Diuretic Response")
st.write("Initial IV loop diuretic dose should be at least 2x the home dose or equivalent of furosemide 40 to 80mg IV if diuretic naive.")

response1 = st.radio(
    "After the initial dose, is the adequacy of diuresis/natriuresis met? (Criteria: spot urine sodium 2 hours after diuretic dose >50-70 mEq/L OR total urine output after 6 hours ≥100-150ml/hour)",
    ('Yes, response is adequate', 'No, response is inadequate'),
    index=None, key='step1'
)

if response1 == 'Yes, response is adequate':
    st.success("Recommendation: Adequate UO/sodium output (>50-70 meq/L).")
    st.info("Plan: Repeat diuretic doses with follow up on UO/Urine Na q 6-12 hours and continue until decongestion, then switch to oral diuretic regimen.")
elif response1 == 'No, response is inadequate':
    st.warning("Recommendation: Inadequate diuresis/natriuresis.")
    st.subheader("Step 2: Escalate Diuretic Dose")
    response2 = st.radio(
        "Action: Double current loop diuretic dose. After doubling the dose, is the diuretic response now adequate?",
        ('Yes, response is now adequate', 'No, response is still inadequate'),
        index=None, key='step2'
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
            index=None, key='step3'
        )
        if response3 == 'Yes, response is now adequate':
            st.success(
                "Recommendation: Response achieved with combination therapy.")
            st.info("Plan: Continue this regimen and monitor closely.")
        elif response3 == 'No, response remains inadequate':
            st.error(
                "Recommendation: Diuretic resistance likely. Inadequate diuresis/natriuresis persists.")
            st.subheader("Step 4: Advanced Options")
            st.markdown("- **Explore other possible causes of poor diuretic response**, such as low output states. Consider a right heart catheterization.\n- If congestion persists despite the above, **consider ultrafiltration**.")
st.divider()

# --- MODULE 2: GDMT NAVIGATOR ---
st.header("Module 2: Guideline-Directed Medical Therapy (GDMT) Navigator")
st.markdown("This tool shows the level of evidence for HFrEF therapies based on the patient's CKD stage, as summarized in Figure 6 of the manuscript.")
gdmt_data = {
    "CKD 1 and 2": {"Beta Blocker": "Strong", "MRA": "Strong", "Non-steroidal MRA": "Strong", "ARNI": "Strong", "ACEi/ARB": "Strong", "Diuretics": "Absent", "SGLT2i": "Strong"},
    "CKD 3": {"Beta Blocker": "Strong", "MRA": "Strong", "Non-steroidal MRA": "Strong", "ARNI": "Strong", "ACEi/ARB": "Strong", "Diuretics": "Absent", "SGLT2i": "Strong"},
    "CKD 4": {"Beta Blocker": "Limited", "MRA": "Limited", "Non-steroidal MRA": "Strong (up to eGFR> 25 cc/min)", "ARNI": "Limited", "ACEi/ARB": "Limited", "Diuretics": "Absent", "SGLT2i": "Strong (eGFR> 20 cc/min)"},
    "CKD 5": {"Beta Blocker": "Absent", "MRA": "Absent", "Non-steroidal MRA": "Absent", "ARNI": "Absent", "ACEi/ARB": "Absent", "Diuretics": "Absent", "SGLT2i": "Limited"}
}
ckd_stage = st.selectbox("Select the patient's CKD Stage:", options=list(
    gdmt_data.keys()), index=None, placeholder="Choose a CKD Stage...")
if ckd_stage:
    st.subheader(f"Recommendations for {ckd_stage}")
    recommendations = gdmt_data[ckd_stage]
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
        else:
            st.markdown(
                f"- **{therapy}:** <span style='color:red;'>**{evidence}**</span>", unsafe_allow_html=True)
st.divider()

# --- MODULE 3: INTERACTIVE CASE STUDIES ---
st.header("Module 3: Interactive Case Studies")
st.markdown(
    "Test your knowledge with these interactive cases from the manuscript.")

# Create clean, consecutively numbered tabs
case1, case2, case3, case4, case5, case6, case7 = st.tabs(
    ["Case 1", "Case 2", "Case 3", "Case 4", "Case 5", "Case 6", "Case 7"])

with case1:
    st.subheader("Case 1 Presentation")
    st.markdown("A 48-year-old woman with a history of coronary artery disease, hypertension, and type 2 diabetes is hospitalized with progressive dyspnea and leg swelling... BP 160/90 mm Hg, HR 105 bpm... JVD, lung crackles... creatinine 1.7 mg/dL (baseline, 0.8 mg/dL). LVEF 55%.")
    st.subheader(
        "Question 1: What is the major mechanism behind this patient's worsening kidney function?")
    options_q1 = ["(a) Kidney venous congestion", "(b) Low cardiac output", "(c) Prerenal azotemia",
                  "(d) Acute tubular injury", "(e) Use of an angiotensin receptor blocker (ARB)"]
    answer_q1 = st.radio("Select your answer for Question 1:",
                         options_q1, index=None, key='q1')
    if answer_q1:
        st.subheader("Answer and Explanation")
        if answer_q1 == options_q1[0]:
            st.success("Correct!")
        else:
            st.error(
                f"Your answer: {answer_q1}. The correct answer is (a) Kidney venous congestion.")
        st.markdown("**Explanation:** In this patient with acute HF, the blood pressure is high with evidence of preserved perfusion... Increased right-sided venous filling pressure (and, by extension, kidney venous pressure) is a major determinant of worsening kidney function in HF across the ejection fraction spectrum.")

with case2:
    # This tab now contains BOTH questions related to Case 2
    st.subheader("Case 2 Presentation")
    st.markdown("A 56-year-old man with HFrEF (EF 30%), and hypertension is hospitalized with acute HF. Home furosemide is 40 mg/d orally... Exam shows JVD, lung crackles... creatinine 1.3 mg/dL (baseline, 0.9 mg/dL).")
    st.subheader(
        "Question 2: What is the most appropriate starting dose for diuretic agents in this patient on admission?")
    options_q2 = ["(a) Furosemide 40 mg intravenously", "(b) Furosemide 80 mg orally",
                  "(c) Bumetanide 1 mg intravenously", "(d) Torsemide 40 mg orally", "(e) Furosemide 100 mg intravenously"]
    answer_q2 = st.radio("Select your answer for Question 2:",
                         options_q2, index=None, key='q2')
    if answer_q2:
        st.subheader("Answer and Explanation")
        if answer_q2 == options_q2[4]:
            st.success("Correct!")
        else:
            st.error(
                f"Your answer: {answer_q2}. The correct answer is (e) Furosemide 100 mg intravenously.")
        st.markdown("**Explanation:** Most HF guidelines recommend starting IV loop diuretic therapy with at least twice the daily home dose. The DOSE trial supports a high-dose strategy (2.5x home oral dose). The intravenous route is preferred in acute HF due to unpredictable gut absorption.")

    st.divider()  # Separator between the two questions

    st.subheader("Case 2, Continued...")
    st.subheader(
        "Question 3: What is the best way to accurately assess diuretic response during decongestion for hospitalized HF?")
    options_q3 = ["(a) Daily measurement of patient weight", "(b) Urine sodium concentration measured 2 hours after diuretic administration",
                  "(c) Charted 24-hour urine output", "(d) Clinical signs and symptoms", "(e) Trend in serum urea nitrogen and creatinine levels"]
    answer_q3 = st.radio("Select your answer for Question 3:",
                         options_q3, index=None, key='q3')
    if answer_q3:
        st.subheader("Answer and Explanation")
        if answer_q3 == options_q3[1]:
            st.success("Correct!")
        else:
            st.error(
                f"Your answer: {answer_q3}. The correct answer is (b) Urine sodium concentration measured 2 hours after diuretic administration.")
        st.markdown("**Explanation:** Daily weights and 24-hour urine output are affected by many factors and are slow to reveal trends. A spot urine sodium measurement 2 hours after a diuretic dose is a reliable and rapid way of predicting the subsequent natriuresis. A spot urine sodium concentration <50-70 mEq/L at 2 hours denotes an insufficient response and allows for rapid uptitration of therapy.")

with case3:
    st.subheader("Case 3 Presentation (from manuscript's Case 4)")
    st.markdown("A 53-year-old woman with HFpEF (EF 55%), diabetes, HTN, and CKD stage G4 is hospitalized. She receives IV furosemide 200 mg twice daily, but her net intake/output is +300 mL and weight is unchanged.")
    st.subheader("Question 4: What is the next best step for this patient?")
    options_q4 = ["(a) Increase furosemide to 400 mg intravenously twice daily", "(b) Change diuretic agent to bumetanide 4 mg intravenously twice daily",
                  "(c) Add metolazone 5 mg/d", "(d) Discontinue lisinopril treatment", "(e) Initiate ultrafiltration"]
    answer_q4 = st.radio("Select your answer for this question:",
                         options_q4, index=None, key='q4')
    if answer_q4:
        st.subheader("Answer and Explanation")
        if answer_q4 == options_q4[2]:
            st.success("Correct!")
        else:
            st.error(
                f"Your answer: {answer_q4}. The correct answer is (c) Add metolazone 5 mg/d.")
        st.markdown("**Explanation:** This patient has diuretic resistance. The best approach is sequential nephron blockade, using diuretic agents acting on different nephron segments. Adding a thiazide-type diuretic like metolazone to a loop diuretic is a classic and effective strategy to augment the overall diuretic response, as demonstrated in trials like CLOROTIC.")

with case4:
    st.subheader("Case 4 Presentation (from manuscript's Case 5)")
    st.markdown("A 60-year-old man with HFrEF (EF, 25%), CKD, is hospitalized. He is on high dose diuretics plus chlorothiazide. Urine output is poor, creatinine is rising (2.4 to 3.2 mg/dL), BP is 90/60 mm Hg, and lactate is 4 mmol/L.")
    st.subheader("Question 5: What is the next best step for this patient?")
    options_q5 = ["(a) Change to furosemide continuous infusion and add acetazolamide", "(b) Change furosemide to bumetanide infusion",
                  "(c) Add metolazone 30 minutes before furosemide", "(d) Arrange for right heart catheterization", "(e) Initiate ultrafiltration"]
    answer_q5 = st.radio("Select your answer for this question:",
                         options_q5, index=None, key='q5')
    if answer_q5:
        st.subheader("Answer and Explanation")
        if answer_q5 == options_q5[3]:
            st.success("Correct!")
        else:
            st.error(
                f"Your answer: {answer_q5}. The correct answer is (d) Arrange for right heart catheterization.")
        st.markdown("**Explanation:** Worsening kidney function despite appropriate decongestion efforts, inadequate diuretic response, and especially concern for low cardiac output (signaled by hypotension and elevated lactate) should prompt early consideration for right heart catheterization to obtain invasive hemodynamic measurements and guide therapy, such as inotropes.")

with case5:
    st.subheader("Case 5 Presentation (from manuscript's Case 6)")
    st.markdown("A 63-year-old woman with HFrEF (EF, 30%) and CKD (stage G3a A1) is stable after hospitalization. Her only GDMT is carvedilol.")
    st.subheader(
        "Question 7: What additional classes of agents constitute GDMT for this individual?")
    options_q7 = ["(a) Angiotensin receptor/neprilysin (ARN) inhibitors, sodium/glucose cotransporter 2 (SGLT2) inhibitors",
                  "(b) ARN inhibitors, SGLT2 inhibitors, mineralocorticoid receptor antagonists (MRAS)", "(c) ARN inhibitors, MRAS"]
    answer_q7 = st.radio("Select your answer for this question:",
                         options_q7, index=None, key='q7')
    if answer_q7:
        st.subheader("Answer and Explanation")
        if answer_q7 == options_q7[1]:
            st.success("Correct!")
        else:
            st.error(
                f"Your answer: {answer_q7}. The correct answer is (b) ARN inhibitors, SGLT2 inhibitors, mineralocorticoid receptor antagonists (MRAS).")
        st.markdown("**Explanation:** GDMT for HFrEF involves the four 'pillars' of therapy. This patient is on a beta-blocker, so she should also be started on an ARNI (or ACEi/ARB), an MRA, and an SGLT2 inhibitor to achieve maximal mortality and morbidity benefit.")

with case6:
    st.subheader("Case 6 Presentation (from manuscript's Case 7)")
    st.markdown("A 65-year-old man with HFrEF (EF, 35%), and CKD (stage G3a) is seen in clinic. He is euvolemic. His K+ is 5.3 mEq/L, and his lisinopril was recently stopped.")
    st.subheader("Question 8: What is the next best step for this patient?")
    options_q8 = ["(a) Start spironolactone", "(b) Increase the furosemide dose", "(c) Add an SGLT2 inhibitor together with lisinopril",
                  "(d) Maintain deescalation of lisinopril", "(e) Add metolazone 3 times per week"]
    answer_q8 = st.radio("Select your answer for this question:",
                         options_q8, index=None, key='q8')
    if answer_q8:
        st.subheader("Answer and Explanation")
        if answer_q8 == options_q8[2]:
            st.success("Correct!")
        else:
            st.error(
                f"Your answer: {answer_q8}. The correct answer is (c) Add an SGLT2 inhibitor together with lisinopril.")
        st.markdown("**Explanation:** Hyperkalemia is a common barrier to GDMT. SGLT2 inhibitors have been shown to reduce the risk of serious hyperkalemia, even in patients taking RAAS inhibitors and MRAs. Adding an SGLT2 inhibitor creates an opportunity to safely reintroduce or maintain the lisinopril, thus optimizing GDMT.")

with case7:
    st.subheader("Case 7 Presentation (from manuscript's Case 8)")
    st.markdown("A 45-year-old woman with a new diagnosis of HFrEF (EF, 35%) was started on lisinopril and empagliflozin two weeks ago. Her creatinine has increased from 1.2 mg/dL to 1.5 mg/dL.")
    st.subheader("Question 9: What is the next best step for this patient?")
    options_q9 = ["(a) Continue lisinopril and empagliflozin", "(b) Stop lisinopril",
                  "(c) Switch lisinopril to valsartan", "(d) Stop empagliflozin"]
    answer_q9 = st.radio("Select your answer for this question:",
                         options_q9, index=None, key='q9')
    if answer_q9:
        st.subheader("Answer and Explanation")
        if answer_q9 == options_q9[0]:
            st.success("Correct!")
        else:
            st.error(
                f"Your answer: {answer_q9}. The correct answer is (a) Continue lisinopril and empagliflozin.")
        st.markdown("**Explanation:** An initial, modest decrease in eGFR (a 'dip' of <30% from baseline, as seen here) is an expected hemodynamic effect upon starting RAAS inhibitors or SGLT2 inhibitors. It does not reflect true tubular injury. Guidelines recommend continuing these therapies, as their long-term use is associated with improved cardiac and kidney outcomes.")
