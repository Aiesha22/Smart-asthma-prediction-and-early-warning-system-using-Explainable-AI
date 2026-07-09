def calculate_medical_risk(
    bmi,
    smoking,
    allergies,
    eczema,
    hay_fever,
    family_history,
    wheezing,
    chest_tightness,
    nighttime
):

    risk = 0

    risk += wheezing * 10
    risk += chest_tightness * 10
    risk += nighttime * 10

    risk += allergies * 8
    risk += eczema * 6
    risk += hay_fever * 6

    risk += family_history * 8
    risk += smoking * 8

    risk += bmi * 0.5

    return round(risk, 2)