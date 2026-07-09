import pandas as pd
import shap
import joblib
import numpy as np
import matplotlib.pyplot as plt

print("Loading model...")

# Load model
model = joblib.load("models/asthma_model.pkl")

print("Loading dataset...")

# Load data
df = pd.read_csv("data/asthma_disease_data.csv")

# Drop unnecessary columns
df.drop(
    columns=["PatientID", "DoctorInCharge"],
    inplace=True
)

# Features
X = df.drop("Diagnosis", axis=1)

# Sample for faster execution
X_sample = X.sample(200, random_state=42)

print("Creating SHAP explainer...")

explainer = shap.TreeExplainer(model)

print("Calculating SHAP values...")

shap_values = explainer.shap_values(X_sample)

# Your SHAP shape = (samples, features, classes)
shap_values_class1 = shap_values[:, :, 1]

print("Generating graph...")

# Calculate average importance
shap_importance = np.abs(shap_values_class1).mean(axis=0)

# Create dataframe
importance_df = pd.DataFrame({
    "Feature": X_sample.columns,
    "SHAP Importance": shap_importance
})

importance_df = importance_df.sort_values(
    by="SHAP Importance",
    ascending=False
)

print("\nTop 10 Explainable AI Features:\n")
print(importance_df.head(10))

# Plot
plt.figure(figsize=(10, 6))

plt.barh(
    importance_df["Feature"],
    importance_df["SHAP Importance"]
)

plt.gca().invert_yaxis()

plt.title("SHAP Explainable AI Feature Importance")

plt.xlabel("Average Impact on Asthma Prediction")

plt.tight_layout()

plt.show()

print("\nSHAP Analysis Completed Successfully!")