import streamlit as st
import joblib

st.set_page_config(
    page_title="Hospital Readmission Prediction",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Hospital Readmission Risk Prediction")

st.write(
    "An AI-based application for predicting the risk of "
    "30-day hospital readmission."
)

st.info(
    "This project is for educational purposes and is not intended "
    "for clinical decision-making."
)

model = joblib.load("models/random_forest.pkl")
preprocessor = joblib.load("models/preprocessor.pkl")

st.success("Model loaded successfully!")

st.header("👤 Patient Information")

col1, col2 = st.columns(2)

with col1:
    age = st.selectbox(
        "Age Group",
        [
            "[0-10)",
            "[10-20)",
            "[20-30)",
            "[30-40)",
            "[40-50)",
            "[50-60)",
            "[60-70)",
            "[70-80)",
            "[80-90)",
            "[90-100)"
        ]
    )

    gender = st.selectbox(
        "Gender",
        ["Female", "Male", "Unknown/Invalid"]
    )

    race = st.selectbox(
        "Race",
        [
            "Caucasian",
            "AfricanAmerican",
            "Hispanic",
            "Asian",
            "Other",
            "Unknown"
        ]
    )

with col2:
    time_in_hospital = st.number_input(
        "Time in Hospital (days)",
        min_value=1,
        max_value=14,
        value=4
    )

    num_lab_procedures = st.number_input(
        "Number of Lab Procedures",
        min_value=1,
        max_value=132,
        value=44
    )

    num_medications = st.number_input(
        "Number of Medications",
        min_value=1,
        max_value=81,
        value=15
    )


# ============================================================
# HOSPITALIZATION INFORMATION
# ============================================================

st.header("🏥 Hospitalization Information")

col1, col2, col3 = st.columns(3)

with col1:
    admission_type_id = st.selectbox(
        "Admission Type",
        ["1", "2", "3", "5", "6", "8", "Other"]
    )

with col2:
    discharge_disposition_id = st.selectbox(
        "Discharge Disposition",
        [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "11",
            "18",
            "22",
            "25",
            "Other"
        ]
    )

with col3:
    admission_source_id = st.selectbox(
        "Admission Source",
        [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "17",
            "Other"
        ]
    )


# ============================================================
# HEALTHCARE UTILIZATION
# ============================================================

st.header("📊 Healthcare Utilization")

col1, col2, col3 = st.columns(3)

with col1:
    num_procedures = st.number_input(
        "Number of Procedures",
        min_value=0,
        max_value=6,
        value=1
    )

with col2:
    number_diagnoses = st.number_input(
        "Number of Diagnoses",
        min_value=1,
        max_value=16,
        value=8
    )

with col3:
    number_outpatient = st.number_input(
        "Previous Outpatient Visits",
        min_value=0,
        max_value=42,
        value=0
    )

col1, col2 = st.columns(2)

with col1:
    number_emergency = st.number_input(
        "Previous Emergency Visits",
        min_value=0,
        max_value=76,
        value=0
    )

with col2:
    number_inpatient = st.number_input(
        "Previous Inpatient Visits",
        min_value=0,
        max_value=21,
        value=0
    )

# ============================================================
# LABORATORY & DIABETES INFORMATION
# ============================================================

st.header("🧪 Laboratory & Diabetes Information")

col1, col2 = st.columns(2)

with col1:
    max_glu_serum = st.selectbox(
        "Maximum Glucose Serum",
        [
            "Not measured",
            "Norm",
            ">200",
            ">300"
        ]
    )

with col2:
    A1Cresult = st.selectbox(
        "A1C Result",
        [
            "Not measured",
            "Norm",
            ">7",
            ">8"
        ]
    )

col1, col2 = st.columns(2)

with col1:
    diabetesMed = st.selectbox(
        "Diabetes Medication",
        ["Yes", "No"]
    )

with col2:
    change = st.selectbox(
        "Medication Change",
        ["Ch", "No"]
    )

# ============================================================
# MEDICATION INFORMATION
# ============================================================

st.header("💊 Medication Information")

medication_options = ["No", "Steady", "Up", "Down"]

col1, col2, col3 = st.columns(3)

with col1:
    metformin = st.selectbox(
        "Metformin",
        medication_options
    )

    repaglinide = st.selectbox(
        "Repaglinide",
        medication_options
    )

    nateglinide = st.selectbox(
        "Nateglinide",
        medication_options
    )

    chlorpropamide = st.selectbox(
        "Chlorpropamide",
        medication_options
    )

    glimepiride = st.selectbox(
        "Glimepiride",
        medication_options
    )

    acetohexamide = st.selectbox(
        "Acetohexamide",
        medication_options
    )

    glipizide = st.selectbox(
        "Glipizide",
        medication_options
    )

    glyburide = st.selectbox(
        "Glyburide",
        medication_options
    )

with col2:
    tolbutamide = st.selectbox(
        "Tolbutamide",
        medication_options
    )

    pioglitazone = st.selectbox(
        "Pioglitazone",
        medication_options
    )

    rosiglitazone = st.selectbox(
        "Rosiglitazone",
        medication_options
    )

    acarbose = st.selectbox(
        "Acarbose",
        medication_options
    )

    miglitol = st.selectbox(
        "Miglitol",
        medication_options
    )

    troglitazone = st.selectbox(
        "Troglitazone",
        medication_options
    )

    tolazamide = st.selectbox(
        "Tolazamide",
        medication_options
    )

    examide = st.selectbox(
        "Examide",
        medication_options
    )

with col3:
    citoglipton = st.selectbox(
        "Citoglipton",
        medication_options
    )

    insulin = st.selectbox(
        "Insulin",
        medication_options
    )

    glyburide_metformin = st.selectbox(
        "Glyburide-Metformin",
        medication_options
    )

    glipizide_metformin = st.selectbox(
        "Glipizide-Metformin",
        medication_options
    )

    glimepiride_pioglitazone = st.selectbox(
        "Glimepiride-Pioglitazone",
        medication_options
    )

    metformin_rosiglitazone = st.selectbox(
        "Metformin-Rosiglitazone",
        medication_options
    )

    metformin_pioglitazone = st.selectbox(
        "Metformin-Pioglitazone",
        medication_options
    )

# ============================================================
# DIAGNOSIS INFORMATION
# ============================================================

st.header("🩺 Diagnosis Information")

diagnosis_groups = [
    "Circulatory",
    "Respiratory",
    "Digestive",
    "Diabetes",
    "Symptoms",
    "Injury/Poisoning",
    "Genitourinary",
    "Musculoskeletal",
    "Neoplasms",
    "Infectious",
    "Metabolic",
    "Skin",
    "Mental",
    "Supplementary",
    "Nervous/Sensory",
    "Blood",
    "Pregnancy",
    "Endocrine",
    "Congenital",
    "Perinatal",
    "Unknown",
    "Other"
]

col1, col2, col3 = st.columns(3)

with col1:
    diag_1_group = st.selectbox(
        "Primary Diagnosis",
        diagnosis_groups
    )

with col2:
    diag_2_group = st.selectbox(
        "Secondary Diagnosis",
        diagnosis_groups
    )

with col3:
    diag_3_group = st.selectbox(
        "Tertiary Diagnosis",
        diagnosis_groups
    )

# ============================================================
# PREDICTION
# ============================================================

st.header("🔮 Readmission Risk Prediction")

if st.button("Predict Readmission Risk"):

    # Create input data
    input_data = {
        "race": race,
        "gender": gender,
        "age": age,
        "admission_type_id": admission_type_id,
        "discharge_disposition_id": discharge_disposition_id,
        "admission_source_id": admission_source_id,
        "time_in_hospital": time_in_hospital,
        "num_lab_procedures": num_lab_procedures,
        "num_procedures": num_procedures,
        "num_medications": num_medications,
        "number_outpatient": number_outpatient,
        "number_emergency": number_emergency,
        "number_inpatient": number_inpatient,
        "number_diagnoses": number_diagnoses,
        "max_glu_serum": max_glu_serum,
        "A1Cresult": A1Cresult,

        "metformin": metformin,
        "repaglinide": repaglinide,
        "nateglinide": nateglinide,
        "chlorpropamide": chlorpropamide,
        "glimepiride": glimepiride,
        "acetohexamide": acetohexamide,
        "glipizide": glipizide,
        "glyburide": glyburide,
        "tolbutamide": tolbutamide,
        "pioglitazone": pioglitazone,
        "rosiglitazone": rosiglitazone,
        "acarbose": acarbose,
        "miglitol": miglitol,
        "troglitazone": troglitazone,
        "tolazamide": tolazamide,
        "examide": examide,
        "citoglipton": citoglipton,
        "insulin": insulin,
        "glyburide-metformin": glyburide_metformin,
        "glipizide-metformin": glipizide_metformin,
        "glimepiride-pioglitazone": glimepiride_pioglitazone,
        "metformin-rosiglitazone": metformin_rosiglitazone,
        "metformin-pioglitazone": metformin_pioglitazone,

        "change": change,
        "diabetesMed": diabetesMed,

        "diag_1_group": diag_1_group,
        "diag_2_group": diag_2_group,
        "diag_3_group": diag_3_group
    }

    # Convert input into DataFrame
    import pandas as pd

    input_df = pd.DataFrame([input_data])

    # Preprocess the input
    input_processed = preprocessor.transform(input_df)

    # Predict probability
    probability = model.predict_proba(input_processed)[0][1]

    # Convert probability to percentage
    risk_percentage = probability * 100

    # Display result
    st.subheader("Prediction Result")

    st.metric(
        "30-Day Readmission Probability",
        f"{risk_percentage:.2f}%"
    )

    # Progress bar
    st.progress(float(probability))

    if probability >= 0.50:
        st.error("🔴 High Risk of 30-Day Readmission")
        st.write(
            "The model estimates a higher probability of "
            "readmission within 30 days."
        )
    else:
        st.success("🟢 Low Risk of 30-Day Readmission")
        st.write(
            "The model estimates a lower probability of "
            "readmission within 30 days."
        )

    st.caption(
        "This prediction is generated by a machine learning model "
        "for educational purposes and should not be used for "
        "clinical decision-making."
    )

    # ============================================================
# PROJECT INFORMATION
# ============================================================

st.divider()

st.subheader("📌 About This Project")

st.write(
    """
    This application uses a machine learning model to estimate the
    probability of a patient's readmission to the hospital within
    30 days of discharge.

    The model was trained using patient demographic, clinical,
    hospitalization, medication, diagnosis, and healthcare
    utilization features.
    """
)

st.info(
    "⚠️ This application is developed for educational and portfolio "
    "purposes only. It is not intended for clinical diagnosis or "
    "medical decision-making."
)

st.caption(
    "Hospital Readmission Risk Prediction | "
    "Python • Scikit-learn • Random Forest • Streamlit"
)