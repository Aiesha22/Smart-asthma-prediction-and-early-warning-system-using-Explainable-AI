import pandas as pd

# Load datasets
air = pd.read_csv("data/Air Quality.csv")
weather = pd.read_csv("data/weather_dataset_2025.csv")

# Latest records
air_row = air.iloc[0]
weather_row = weather.iloc[0]

env_score = 0

# Air Quality Risk
if air_row["CO(GT)"] > 5:
    env_score += 20

if air_row["NO2(GT)"] > 100:
    env_score += 20

if air_row["NOx(GT)"] > 100:
    env_score += 20

# Weather Risk
if weather_row["Humidity_%"] > 70:
    env_score += 15

if weather_row["Temperature_C"] > 35:
    env_score += 15

print("Environmental Risk Score:", env_score)

if env_score < 20:
    print("Low Environmental Risk")
elif env_score < 50:
    print("Moderate Environmental Risk")
else:
    print("High Environmental Risk")