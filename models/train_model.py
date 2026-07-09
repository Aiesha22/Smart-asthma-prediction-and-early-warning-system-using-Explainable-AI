import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

import seaborn as sns
import matplotlib.pyplot as plt

# -----------------------------
# LOAD DATA
# -----------------------------
DATA_PATH = "data/asthma_disease_data.csv"  # change if needed
df = pd.read_csv(DATA_PATH)

print("Dataset Loaded:", df.shape)

# -----------------------------
# TARGET COLUMN
# -----------------------------
target = "Diagnosis"

selected_features = [
    "Age",
    "BMI",
    "Smoking",
    "HistoryOfAllergies",
    "Eczema",
    "HayFever",
    "FamilyHistoryAsthma",
    "Wheezing",
    "ChestTightness",
    "NighttimeSymptoms"
]

X = df[selected_features]
y = df[target]



# -----------------------------
# TRAIN-TEST SPLIT
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# -----------------------------
# MODEL
# -----------------------------
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight="balanced"
)

# -----------------------------
# TRAIN MODEL  ✅ IMPORTANT FIX
# -----------------------------
model.fit(X_train, y_train)
feature_importance = pd.Series(model.feature_importances_, index=X.columns)
feature_importance = feature_importance.sort_values(ascending=False)

print("\nTop Important Features:")
print(feature_importance.head(10))
plt.figure(figsize=(8,5))
feature_importance.head(10).plot(kind="bar")
plt.title("Top Factors Affecting Asthma Risk")
plt.savefig("models/feature_importance.png")
plt.close()
# -----------------------------
# PREDICTION
# -----------------------------
y_pred = model.predict(X_test)

# -----------------------------
# EVALUATION
# -----------------------------
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# -----------------------------
# CONFUSION MATRIX
# -----------------------------
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

# -----------------------------
# VISUALIZATION
# -----------------------------
plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix Heatmap")
plt.savefig("models/confusion_matrix.png")
plt.close()
# -----------------------------
# SAVE MODEL
# -----------------------------
import joblib

joblib.dump(model, "models/asthma_model.pkl")

print("Model Saved Successfully!")

