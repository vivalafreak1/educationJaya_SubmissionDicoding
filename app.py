import streamlit as st
import pandas as pd
import joblib
from data_preprocessing import data_preprocessing, encoder_Daytime_evening_attendance, encoder_Debtor, encoder_Gender, encoder_International, encoder_Marital_status, encoder_Scholarship_holder, encoder_target

# Load the trained Random Forest model
rdf_model = joblib.load("model/rdf_model.joblib")

# Streamlit layout
col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png", width=130)
with col2:
    st.header('Student Performance Prediction App (Prototype)')

# Initialize DataFrame to store user inputs
data = pd.DataFrame()

# Categorical Inputs (in 3 columns)
col1, col2, col3 = st.columns(3)

with col1:
    Daytime_evening_attendance = st.selectbox(label='Daytime/Evening Attendance', options=encoder_Daytime_evening_attendance.classes_, index=1)
    data["Daytime_evening_attendance"] = [Daytime_evening_attendance]

with col2:
    Debtor = st.selectbox(label='Debtor', options=encoder_Debtor.classes_, index=1)
    data["Debtor"] = [Debtor]

with col3:
    Gender = st.selectbox(label='Gender', options=encoder_Gender.classes_, index=1)
    data["Gender"] = [Gender]

col1, col2, col3 = st.columns(3)

with col1:
    International = st.selectbox(label='International', options=encoder_International.classes_, index=1)
    data["International"] = [International]

with col2:
    Marital_status = st.selectbox(label='Marital Status', options=encoder_Marital_status.classes_, index=0)
    data["Marital_status"] = [Marital_status]

with col3:
    Scholarship_holder = st.selectbox(label='Scholarship Holder', options=encoder_Scholarship_holder.classes_, index=1)
    data["Scholarship_holder"] = [Scholarship_holder]

# Numerical Inputs for pca_numerical_columns_1 (in 4 columns)
st.subheader("Academic Performance Metrics")
col1, col2, col3, col4 = st.columns(4)

with col1:
    Age_at_enrollment = int(st.number_input(label='Age at Enrollment', value=20))
    data["Age_at_enrollment"] = [Age_at_enrollment]

with col2:
    Curricular_units_1st_sem_credited = int(st.number_input(label='1st Sem Credited Units', value=5))
    data["Curricular_units_1st_sem_credited"] = [Curricular_units_1st_sem_credited]

with col3:
    Curricular_units_1st_sem_enrolled = int(st.number_input(label='1st Sem Enrolled Units', value=6))
    data["Curricular_units_1st_sem_enrolled"] = [Curricular_units_1st_sem_enrolled]

with col4:
    Curricular_units_1st_sem_evaluations = int(st.number_input(label='1st Sem Evaluations', value=5))
    data["Curricular_units_1st_sem_evaluations"] = [Curricular_units_1st_sem_evaluations]

col1, col2, col3, col4 = st.columns(4)

with col1:
    Curricular_units_1st_sem_approved = int(st.number_input(label='1st Sem Approved Units', value=5))
    data["Curricular_units_1st_sem_approved"] = [Curricular_units_1st_sem_approved]

with col2:
    Curricular_units_1st_sem_grade = float(st.number_input(label='1st Sem Grade', value=14.0))
    data["Curricular_units_1st_sem_grade"] = [Curricular_units_1st_sem_grade]

with col3:
    Curricular_units_1st_sem_without_evaluations = int(st.number_input(label='1st Sem Units w/o Evaluations', value=0))
    data["Curricular_units_1st_sem_without_evaluations"] = [Curricular_units_1st_sem_without_evaluations]

with col4:
    Curricular_units_2nd_sem_credited = int(st.number_input(label='2nd Sem Credited Units', value=5))
    data["Curricular_units_2nd_sem_credited"] = [Curricular_units_2nd_sem_credited]

col1, col2, col3, col4 = st.columns(4)

with col1:
    Curricular_units_2nd_sem_enrolled = int(st.number_input(label='2nd Sem Enrolled Units', value=6))
    data["Curricular_units_2nd_sem_enrolled"] = [Curricular_units_2nd_sem_enrolled]

with col2:
    Curricular_units_2nd_sem_evaluations = int(st.number_input(label='2nd Sem Evaluations', value=5))
    data["Curricular_units_2nd_sem_evaluations"] = [Curricular_units_2nd_sem_evaluations]

with col3:
    Curricular_units_2nd_sem_approved = int(st.number_input(label='2nd Sem Approved Units', value=5))
    data["Curricular_units_2nd_sem_approved"] = [Curricular_units_2nd_sem_approved]

with col4:
    Curricular_units_2nd_sem_grade = float(st.number_input(label='2nd Sem Grade', value=15.0))
    data["Curricular_units_2nd_sem_grade"] = [Curricular_units_2nd_sem_grade]

col1, col2, col3 = st.columns(3)

with col1:
    Curricular_units_2nd_sem_without_evaluations = int(st.number_input(label='2nd Sem Units w/o Evaluations', value=0))
    data["Curricular_units_2nd_sem_without_evaluations"] = [Curricular_units_2nd_sem_without_evaluations]

# Numerical Inputs for pca_numerical_columns_2 (in 3 columns)
st.subheader("Prior Academic and Economic Metrics")
col1, col2, col3 = st.columns(3)

with col1:
    Previous_qualification_grade = float(st.number_input(label='Previous Qualification Grade', value=150.0))
    data["Previous_qualification_grade"] = [Previous_qualification_grade]

with col2:
    Admission_grade = float(st.number_input(label='Admission Grade', value=140.0))
    data["Admission_grade"] = [Admission_grade]

with col3:
    Unemployment_rate = float(st.number_input(label='Unemployment Rate', value=10.0))
    data["Unemployment_rate"] = [Unemployment_rate]

col1, col2, col3 = st.columns(3)

with col1:
    Inflation_rate = float(st.number_input(label='Inflation Rate', value=2.0))
    data["Inflation_rate"] = [Inflation_rate]

with col2:
    GDP = float(st.number_input(label='GDP', value=1.5))
    data["GDP"] = [GDP]

# Display raw data
with st.expander("View the Raw Data"):
    st.dataframe(data=data, width=800, height=10)

# Prediction button
if st.button('Predict'):
    # Preprocess the data
    new_data = data_preprocessing(data=data)
    with st.expander("View the Preprocessed Data"):
        st.dataframe(data=new_data, width=800, height=10)
    
    # Make prediction
    prediction = rdf_model.predict(new_data)
    predicted_status = encoder_target.inverse_transform(prediction)[0]  # Inverse transform to get original label
    st.write(f"Predicted Student Status: **{predicted_status}**")