import pandas as pd

# -----------------------------
# LOAD DATASET
# -----------------------------
# Change filename if your dataset name is different
DATA_PATH = "data/asthma_disease_data.csv"

try:
    df = pd.read_csv("data/asthma_disease_data.csv")
    print("\n✅ Dataset loaded successfully!\n")

except FileNotFoundError:
    print(f"\n❌ File not found at: {DATA_PATH}")
    print("👉 Please check your file path and try again.\n")
    exit()

# -----------------------------
# BASIC INFORMATION
# -----------------------------
print("\n📊 FIRST 5 ROWS:")
print(df.head())

print("\n📌 DATASET INFO:")
print(df.info())

print("\n📏 DATASET SHAPE:")
print(df.shape)

# -----------------------------
# MISSING VALUES CHECK
# -----------------------------
print("\n⚠️ MISSING VALUES:")
print(df.isnull().sum())

# -----------------------------
# DUPLICATES CHECK
# -----------------------------
print("\n🔁 DUPLICATE ROWS:")
print(df.duplicated().sum())

# -----------------------------
# STATISTICS SUMMARY
# -----------------------------
print("\n📈 STATISTICAL SUMMARY:")
print(df.describe())

# -----------------------------
# TARGET COLUMN CHECK
# -----------------------------
# Change "Diagnosis" if your target column has a different name
target_column = "Diagnosis"

if target_column in df.columns:
    print("\n🎯 TARGET DISTRIBUTION:")
    print(df[target_column].value_counts())
else:
    print(f"\n⚠️ Target column '{target_column}' not found in dataset!")