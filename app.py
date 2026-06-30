import streamlit as st

st.set_page_config(layout="wide")

# --- DATA DICTIONARIES ---
xerop = {"No": 0, "Sometimes": 1, "Always": 2}
medop = {"No": 0, "Yes": 1}
diabop = {"No": 0, "Yes": 1}

halop = {"0": 1, "1": 1, "2": 2, "3": 2, "4": 3, "5": 3}
candop = {"No": 0, "Yes": 2}
lendop = {"No": 0, "Yes": 1}
perdop = {"None": 0, "Moderate": 1, "Severe": 2}

ckdop = {"0": 0, "1": 0, "2": 0, "3": 1, "4": 2, "5": 2, "Dialysis": 3}

# Initialize calculation state
if 'calculated' not in st.session_state:
    st.session_state.calculated = False
    st.session_state.total_points = 0 

# --- TITLE ---
st.title('Oral Health Index & CKD Risk Calculator')

# --- PATIENT SECTION ---
st.header("Patient")
xer = st.selectbox("Xerostomia:", list(xerop.keys()))
med = st.selectbox("Medications causing dry mouth:", list(medop.keys()))
diab = st.selectbox("Diabetes:", list(diabop.keys()))

# --- DENTAL EXAM SECTION ---
st.header("Dental Exam")
hal = st.selectbox("Halitosis:", list(halop.keys()))
cand = st.selectbox("Candidiasis:", list(candop.keys()))
tongue = st.selectbox("Tongue Fissuring / Scrotal Tongue:", list(lendop.keys()))
per = st.selectbox("Periodontal Disease:", list(perdop.keys()))

# --- CKD SECTION ---
st.header("CKD")
ckd = st.selectbox("CKD Stage:", list(ckdop.keys()))

# --- CALCULATION LOGIC ---
def calculate_risk():
    total = (xerop[xer] + medop[med] + diabop[diab] +
             halop[hal] + candop[cand] + lendop[tongue] +
             perdop[per] + ckdop[ckd])
    st.session_state.total_points = total
    st.session_state.calculated = True

# --- RESULTS SECTION AT THE END ---
st.divider()
st.header("Calculator Results")

if st.button("Calculate Risk Score", use_container_width=True):
    calculate_risk()

if st.session_state.calculated:
    points = st.session_state.total_points

    # Plain text results (no colors)
    if points <= 3:
        st.write(f"### Low Risk\nScore: {points}")
    elif 4 <= points <= 6:
        st.write(f"### Moderate Risk\nScore: {points}")
    else:
        st.write(f"### High Risk\nScore: {points}")

    if points >= 4:
        st.write("---")
        st.button("📤 Share Results", use_container_width=True)

else:
    st.write("*Waiting for calculation...*")
