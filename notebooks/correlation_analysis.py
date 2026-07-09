import pandas as pd

df = pd.read_csv("data/asthma_disease_data.csv")

df.drop(
    columns=["PatientID", "DoctorInCharge"],
    inplace=True
)

corr = df.corr(numeric_only=True)

target_corr = corr["Diagnosis"].sort_values(
    ascending=False
)

print("\nCorrelation with Diagnosis:\n")
print(target_corr)