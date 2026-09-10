# 🏥 Hospital Readmission Risk Prediction & Analytics

## 📌 Project Overview

Hospital readmission is an important healthcare challenge. This project develops a machine learning system that predicts whether a diabetic patient is likely to be readmitted to the hospital within 30 days of discharge.

The project combines data analysis, feature engineering, SQL analytics, machine learning, and Streamlit to create an end-to-end healthcare analytics application.

> ⚠️ **Disclaimer:** This project is developed for educational and portfolio purposes only. It is not intended for clinical diagnosis or medical decision-making.

---

## 🎯 Problem Statement

Develop a machine learning system that predicts whether a diabetic patient is likely to be readmitted to a hospital within 30 days of discharge using demographic, clinical, hospitalization, medication, diagnosis, and healthcare utilization information.

### Prediction Question

**Can we identify patients at higher risk of being readmitted within 30 days using information available from their hospital encounter?**

---

## 📊 Dataset

The project uses the **Diabetes 130-US Hospitals for Years 1999–2008** dataset.

The dataset contains:

- 101,766 hospital encounters
- 71,518 unique patients
- 50 original features

The data contains information related to:

- Patient demographics
- Hospital admission and discharge
- Laboratory procedures
- Medications
- Diagnoses
- Previous healthcare utilization
- Readmission status

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- SQL / SQLite
- Streamlit
- Jupyter Notebook
- Joblib
- Git & GitHub

---

## 🔄 Project Workflow

```text
Dataset
   ↓
Data Understanding
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Feature Engineering
   ↓
SQL Analysis
   ↓
Train/Test Split
   ↓
Data Preprocessing
   ↓
Machine Learning
   ↓
Model Evaluation
   ↓
Streamlit Application

---

## 🚀 Streamlit Application

The trained Random Forest model is integrated into an interactive Streamlit application.

Users can enter:

- Patient information
- Hospitalization information
- Healthcare utilization
- Laboratory information
- Diabetes medication information
- Medication details
- Diagnosis groups

The application then generates a predicted **30-day hospital readmission risk**.

### 🧑 Patient Information

![Patient Information](screenshots/patient_information.png)

### 🏥 Hospitalization & Healthcare Utilization

![Hospitalization](screenshots/hospitalization.png)

### 💊 Medication Information

![Medication Information](screenshots/medication_information.png)

### 🩺 Diagnosis & Prediction Result

![Prediction Result](screenshots/prediction_result.png)