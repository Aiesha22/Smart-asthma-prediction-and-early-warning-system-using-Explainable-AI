import pandas as pd

df = pd.read_csv("data/asthma_disease_data.csv")

print("\nDataset Shape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDiagnosis Value Counts:")
print(df["Diagnosis"].value_counts())