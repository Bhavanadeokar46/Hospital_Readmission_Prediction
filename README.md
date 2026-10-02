# 🏥 Hospital Readmission Risk Prediction & Analytics

## 📌 Project Overview

Hospital readmission is an important healthcare challenge. This project develops a machine learning system to estimate whether a diabetic patient is likely to be readmitted to the hospital within 30 days of discharge.

The project combines data understanding, data cleaning, exploratory data analysis, feature engineering, SQL analytics, machine learning, model evaluation, and Streamlit to create an end-to-end healthcare analytics application.

> ⚠️ **Disclaimer:** This project is developed for educational and portfolio purposes only. It is not intended for clinical diagnosis, medical advice, or real-world medical decision-making.

---

## 🎯 Problem Statement

Develop a machine learning system that predicts whether a diabetic patient is likely to be readmitted to a hospital within 30 days of discharge using demographic, clinical, hospitalization, medication, diagnosis, and healthcare utilization information.

### Prediction Question

**Can we identify patients with a higher estimated probability of 30-day readmission using information available from their hospital encounter?**

---

## 📊 Dataset

The project uses the **Diabetes 130-US Hospitals for Years 1999–2008** dataset.

### Dataset Size

- **101,766** hospital encounters
- **71,518** unique patients
- **50** original features

The dataset contains information related to:

- Patient demographics
- Hospital admission and discharge
- Laboratory procedures
- Medications
- Diagnoses
- Healthcare utilization
- Diabetes treatment
- Readmission status

### Target Variable

The original `readmitted` variable contains three categories:

- `<30` — readmitted within 30 days
- `>30` — readmitted after 30 days
- `NO` — not readmitted

For binary classification, these were converted into:

- `1` → Readmitted within 30 days
- `0` → Not readmitted within 30 days

### Target Distribution

- Not readmitted within 30 days: **90,409**
- Readmitted within 30 days: **11,357**
- Overall 30-day readmission rate: **11.16%**

The target variable is imbalanced, so precision, recall, F1-score, and ROC-AUC were considered along with accuracy.

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
Patient-Aware Train/Test Split
   ↓
Data Preprocessing
   ↓
Machine Learning
   ↓
Model Evaluation
   ↓
Hyperparameter Tuning
   ↓
Feature Importance Analysis
   ↓
Streamlit Application