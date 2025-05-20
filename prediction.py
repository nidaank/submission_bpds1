import pandas as pd
import joblib

# === Load Model, Scaler, dan OneHotEncoder ===
model = joblib.load("model/rf_model.pkl")
encoder = joblib.load("model/onehot_encoder.pkl")

# === Siapkan Data Baru ===
# Fitur numerik dan kategorikal HARUS sesuai dengan saat training
data_baru = pd.DataFrame({
    'OverTime': ['Yes'],
    'BusinessTravel': ['Travel_Rarely'],
    'JobRole': ['Laboratory Technician'],
    'Age': [23],
    'MonthlyIncome': [1200],
    'JobLevel': [1],
    'TotalWorkingYears': [0],
    'YearsAtCompany': [0],
    'YearsWithCurrManager': [0],
    'YearsInCurrentRole': [0],
    'JobInvolvement': [2]
})

# === Pisahkan fitur numerik & kategorikal ===
important_categorical = ['OverTime', 'BusinessTravel', 'JobRole']
important_numerical = ['Age', 'JobLevel', 'TotalWorkingYears', 'YearsAtCompany','YearsWithCurrManager', 
                      'YearsInCurrentRole', 'JobInvolvement', 'MonthlyIncome']

# === Transformasi fitur ===
# One-hot encode fitur kategorikal
X_cat = encoder.transform(data_baru[important_categorical])
cat_cols = encoder.get_feature_names_out(important_categorical)

# Scale fitur numerik
X_num = data_baru[important_numerical].reset_index(drop=True)
X_ready = pd.concat([X_num, pd.DataFrame(X_cat, columns=cat_cols)], axis=1)

# === Prediksi ===
prediction = model.predict(X_ready)
proba = model.predict_proba(X_ready)

# === Output ===
print("Hasil Prediksi:")
if prediction == 1:
    print(f"Karyawan diprediksi AKAN keluar (Attrition = 1), kemungkinan: {proba[0][1]:.2%}")
else:
    print(f"Karyawan diprediksi TIDAK AKAN keluar (Attrition = 0), kemungkinan keluar: {proba[0][0]:.2%}")