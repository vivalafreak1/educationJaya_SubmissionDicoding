import joblib
import numpy as np
import pandas as pd

encoder_Daytime_evening_attendance = joblib.load("model/encoder_Daytime_evening_attendance.joblib")
encoder_Debtor = joblib.load("model/encoder_Debtor.joblib")
encoder_Gender = joblib.load("model/encoder_Gender.joblib")
encoder_International = joblib.load("model/encoder_International.joblib")
encoder_Marital_status = joblib.load("model/encoder_Marital_status.joblib")
encoder_Scholarship_holder = joblib.load("model/encoder_Scholarship_holder.joblib")

encoder_target = joblib.load("model/encoder_target.joblib")

pca_1 = joblib.load("model/pca_1.joblib")
pca_2 = joblib.load("model/pca_2.joblib")

scaler_Admission_grade = joblib.load("model/scaler_Admission_grade.joblib")
scaler_Age_at_enrollment = joblib.load("model/scaler_Age_at_enrollment.joblib")
scaler_Curricular_units_1st_sem_approved = joblib.load("model/scaler_Curricular_units_1st_sem_approved.joblib")
scaler_Curricular_units_1st_sem_credited = joblib.load("model/scaler_Curricular_units_1st_sem_credited.joblib")
scaler_Curricular_units_1st_sem_enrolled = joblib.load("model/scaler_Curricular_units_1st_sem_enrolled.joblib")
scaler_Curricular_units_1st_sem_evaluations = joblib.load("model/scaler_Curricular_units_1st_sem_evaluations.joblib")
scaler_Curricular_units_1st_sem_grade = joblib.load("model/scaler_Curricular_units_1st_sem_grade.joblib")
scaler_Curricular_units_1st_sem_without_evaluations = joblib.load("model/scaler_Curricular_units_1st_sem_without_evaluations.joblib")
scaler_Curricular_units_2nd_sem_approved = joblib.load("model/scaler_Curricular_units_2nd_sem_approved.joblib")
scaler_Curricular_units_2nd_sem_credited = joblib.load("model/scaler_Curricular_units_2nd_sem_credited.joblib")
scaler_Curricular_units_2nd_sem_enrolled = joblib.load("model/scaler_Curricular_units_2nd_sem_enrolled.joblib")
scaler_Curricular_units_2nd_sem_evaluations = joblib.load("model/scaler_Curricular_units_2nd_sem_evaluations.joblib")
scaler_Curricular_units_2nd_sem_grade = joblib.load("model/scaler_Curricular_units_2nd_sem_grade.joblib")
scaler_Curricular_units_2nd_sem_without_evaluations = joblib.load("model/scaler_Curricular_units_2nd_sem_without_evaluations.joblib")
scaler_GDP = joblib.load("model/scaler_GDP.joblib")
scaler_Inflation_rate = joblib.load("model/scaler_Inflation_rate.joblib")
scaler_Previous_qualification_grade = joblib.load("model/scaler_Previous_qualification_grade.joblib")
scaler_Unemployment_rate = joblib.load("model/scaler_Unemployment_rate.joblib")

pca_numerical_columns_1 = [
    'Age_at_enrollment',
    'Curricular_units_1st_sem_credited',
    'Curricular_units_1st_sem_enrolled',
    'Curricular_units_1st_sem_evaluations',	
    'Curricular_units_1st_sem_approved',
    'Curricular_units_1st_sem_grade',
    'Curricular_units_1st_sem_without_evaluations',
    'Curricular_units_2nd_sem_credited',
    'Curricular_units_2nd_sem_enrolled',
    'Curricular_units_2nd_sem_evaluations',	
    'Curricular_units_2nd_sem_approved',
    'Curricular_units_2nd_sem_grade',
    'Curricular_units_2nd_sem_without_evaluations',
]

pca_numerical_columns_2 = [
    'Previous_qualification_grade',
    'Admission_grade',
    'Unemployment_rate',
    'Inflation_rate',
    'GDP'
]

def data_preprocessing(data):
    """Preprocessing data
    
    Args:
        data (Pandas DataFrame): Dataframe that contains all the data to make predictions
        
    return:
        Pandas DataFrame: Dataframe that contains all the preprocessed data
    """
    data = data.copy()
    df = pd.DataFrame()
    
    data['Age_at_enrollment'] = scaler_Age_at_enrollment.transform(np.asarray(data['Age_at_enrollment']).reshape(-1, 1)).ravel()
    data['Curricular_units_1st_sem_credited'] = scaler_Curricular_units_1st_sem_credited.transform(np.asarray(data['Curricular_units_1st_sem_credited']).reshape(-1, 1)).ravel()
    data['Curricular_units_1st_sem_enrolled'] = scaler_Curricular_units_1st_sem_enrolled.transform(np.asarray(data['Curricular_units_1st_sem_enrolled']).reshape(-1, 1)).ravel()
    data['Curricular_units_1st_sem_evaluations'] = scaler_Curricular_units_1st_sem_evaluations.transform(np.asarray(data['Curricular_units_1st_sem_evaluations']).reshape(-1, 1)).ravel()
    data['Curricular_units_1st_sem_approved'] = scaler_Curricular_units_1st_sem_approved.transform(np.asarray(data['Curricular_units_1st_sem_approved']).reshape(-1, 1)).ravel()
    data['Curricular_units_1st_sem_grade'] = scaler_Curricular_units_1st_sem_grade.transform(np.asarray(data['Curricular_units_1st_sem_grade']).reshape(-1, 1)).ravel()
    data['Curricular_units_1st_sem_without_evaluations'] = scaler_Curricular_units_1st_sem_without_evaluations.transform(np.asarray(data['Curricular_units_1st_sem_without_evaluations']).reshape(-1, 1)).ravel()
    data['Curricular_units_2nd_sem_credited'] = scaler_Curricular_units_2nd_sem_credited.transform(np.asarray(data['Curricular_units_2nd_sem_credited']).reshape(-1, 1)).ravel()
    data['Curricular_units_2nd_sem_enrolled'] = scaler_Curricular_units_2nd_sem_enrolled.transform(np.asarray(data['Curricular_units_2nd_sem_enrolled']).reshape(-1, 1)).ravel()
    data['Curricular_units_2nd_sem_evaluations'] = scaler_Curricular_units_2nd_sem_evaluations.transform(np.asarray(data['Curricular_units_2nd_sem_evaluations']).reshape(-1, 1)).ravel()
    data['Curricular_units_2nd_sem_approved'] = scaler_Curricular_units_2nd_sem_approved.transform(np.asarray(data['Curricular_units_2nd_sem_approved']).reshape(-1, 1)).ravel()
    data['Curricular_units_2nd_sem_grade'] = scaler_Curricular_units_2nd_sem_grade.transform(np.asarray(data['Curricular_units_2nd_sem_grade']).reshape(-1, 1)).ravel()
    data['Curricular_units_2nd_sem_without_evaluations'] = scaler_Curricular_units_2nd_sem_without_evaluations.transform(np.asarray(data['Curricular_units_2nd_sem_without_evaluations']).reshape(-1, 1)).ravel()
    
    # PCA 1
    pca_1_result = pca_1.transform(data[pca_numerical_columns_1])
    df[['pc1_1', 'pc1_2', 'pc1_3']] = pca_1_result[:, :3] 

    # PCA 2
    data['Previous_qualification_grade'] = scaler_Previous_qualification_grade.transform(np.asarray(data['Previous_qualification_grade']).reshape(-1, 1)).ravel()
    data['Admission_grade'] = scaler_Admission_grade.transform(np.asarray(data['Admission_grade']).reshape(-1, 1)).ravel()
    data['Unemployment_rate'] = scaler_Unemployment_rate.transform(np.asarray(data['Unemployment_rate']).reshape(-1, 1)).ravel()
    data['Inflation_rate'] = scaler_Inflation_rate.transform(np.asarray(data['Inflation_rate']).reshape(-1, 1)).ravel()
    data['GDP'] = scaler_GDP.transform(np.asarray(data['GDP']).reshape(-1, 1)).ravel()
    
    # PCA 2 
    pca_2_result = pca_2.transform(data[pca_numerical_columns_2])
    df[['pc2_1', 'pc2_2', 'pc2_3']] = pca_2_result[:, :3]  

    # Encode categorical variables
    df['Daytime_evening_attendance'] = encoder_Daytime_evening_attendance.transform(data['Daytime_evening_attendance'])
    df['Debtor'] = encoder_Debtor.transform(data['Debtor'])
    df['Gender'] = encoder_Gender.transform(data['Gender'])
    df['International'] = encoder_International.transform(data['International'])
    df['Marital_status'] = encoder_Marital_status.transform(data['Marital_status'])
    df['Scholarship_holder'] = encoder_Scholarship_holder.transform(data['Scholarship_holder'])

    return df