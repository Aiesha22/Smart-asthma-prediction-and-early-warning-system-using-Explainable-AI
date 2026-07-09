medical_risk = 54.94
environment_risk = 55

# Weighted Formula
final_risk = (
    medical_risk * 0.60 +
    environment_risk * 0.40
)

print(f"Medical Risk Score: {medical_risk:.2f}")
print(f"Environmental Risk Score: {environment_risk:.2f}")
print(f"\nFinal Asthma Risk Score: {final_risk:.2f}")

if final_risk < 25:
    print("Risk Level: Low")
elif final_risk < 50:
    print("Risk Level: Moderate")
elif final_risk < 75:
    print("Risk Level: High")
else:
    print("Risk Level: Very High")

print("\nRecommendations:")

if final_risk >= 50:
    print("- Avoid outdoor activities during peak pollution.")
    print("- Carry inhaler if prescribed.")
    print("- Monitor symptoms regularly.")
    print("- Reduce exposure to dust and pollen.")