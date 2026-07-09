import pandas as pd

# Load asthma dataset
df = pd.read_csv("data/asthma_disease_data.csv")

# Example patient
patient = df.iloc[0]

risk_score = 0

# Symptoms
risk_score += patient["Wheezing"] * 10
risk_score += patient["ShortnessOfBreath"] * 10
risk_score += patient["ChestTightness"] * 10
risk_score += patient["NighttimeSymptoms"] * 10

# Allergies
risk_score += patient["HistoryOfAllergies"] * 8
risk_score += patient["Eczema"] * 6
risk_score += patient["HayFever"] * 6

# Family history
risk_score += patient["FamilyHistoryAsthma"] * 8

# Smoking
risk_score += patient["Smoking"] * 8

# Exposure
risk_score += patient["PollutionExposure"] * 5

print("Asthma Risk Score:", risk_score)

if risk_score < 25:
    print("Low Risk")
elif risk_score < 50:
    print("Moderate Risk")
elif risk_score < 75:
    print("High Risk")
else:
    print("Very High Risk")