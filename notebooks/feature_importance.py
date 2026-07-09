import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load model
model = joblib.load("models/asthma_model.pkl")

# Load data
df = pd.read_csv("data/asthma_disease_data.csv")

# Remove unused columns
df.drop(
    columns=["PatientID", "DoctorInCharge"],
    inplace=True
)

X = df.drop("Diagnosis", axis=1)

# Feature importance
importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nTop Features:")
print(importance)

# Plot
plt.figure(figsize=(10,8))
plt.barh(
    importance["Feature"],
    importance["Importance"]
)

plt.gca().invert_yaxis()
plt.title("Asthma Feature Importance")
plt.tight_layout()
plt.show()