from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(
    filename,
    age,
    bmi,
    prediction,
    probability,
    medical_risk,
    environment_risk,
    final_risk
):

    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("<b>Smart Asthma Prediction Report</b>", styles["Title"]))

    story.append(Paragraph(f"<b>Age:</b> {age}", styles["BodyText"]))
    story.append(Paragraph(f"<b>BMI:</b> {bmi}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Prediction:</b> {prediction}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Prediction Probability:</b> {probability:.2%}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Medical Risk:</b> {medical_risk:.2f}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Environmental Risk:</b> {environment_risk:.2f}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Final Risk Score:</b> {final_risk:.2f}", styles["BodyText"]))

    story.append(Paragraph("<b>Recommendations</b>", styles["Heading2"]))

    if final_risk < 25:
        recommendation = "Low Risk: Maintain a healthy lifestyle and regular checkups."
    elif final_risk < 50:
        recommendation = "Moderate Risk: Avoid pollution and monitor symptoms."
    else:
        recommendation = "High Risk: Consult a doctor immediately and avoid asthma triggers."

    story.append(Paragraph(recommendation, styles["BodyText"]))

    doc.build(story)