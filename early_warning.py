def early_warning(final_risk, humidity, aqi):

    if final_risk >= 70 or aqi >= 150 or humidity >= 80:

        return """
🔴 HIGH RISK

High chance of an asthma attack within the next 24–72 hours.

Recommendations:
• Avoid outdoor activities.
• Carry your inhaler.
• Wear a mask outdoors.
• Consult your doctor if symptoms worsen.
"""

    elif final_risk >= 40:

        return """
🟡 MODERATE RISK

Possible asthma symptoms within the next 24–72 hours.

Recommendations:
• Monitor symptoms.
• Avoid dust and pollen.
• Stay hydrated.
"""

    else:

        return """
🟢 LOW RISK

Low chance of an asthma attack.

Recommendations:
• Continue healthy habits.
• Exercise regularly.
• Keep monitoring your environment.
"""