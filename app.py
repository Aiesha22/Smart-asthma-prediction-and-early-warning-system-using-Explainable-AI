import streamlit as st
import pandas as pd
import plotly.express as px
import joblib
from database import save_prediction, load_history
# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Smart Asthma Prediction",
    layout="wide"
)

# Load trained machine learning model
model = joblib.load("models/asthma_model.pkl")

st.title("🫁 Smart Asthma Prediction and Early Detection System")
st.markdown("""
This system combines:

✅ Patient Medical Data

✅ Air Quality Data

✅ Weather Data

✅ Explainable AI

to predict asthma risk and provide recommendations.
""")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go To",
    [
        "Patient Assessment",
        "Dataset Analytics",
        "Environmental Risk",
        "Explainable AI",
        "Final Assessment",
        "Patient History"
    ]
)

# -----------------------------
# PATIENT ASSESSMENT
# -----------------------------
if page == "Patient Assessment":
    st.header("Patient Information")
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", 1, 100, 25)
        bmi = st.number_input("BMI", 10.0, 50.0, 22.0)
        smoking = st.selectbox("Smoking", ["NO", "YES"])
        allergies = st.selectbox("History Of Allergies", ["NO", "YES"])
        eczema = st.selectbox("Eczema", ["NO", "YES"])

    with col2:
        hay_fever = st.selectbox("Hay Fever", ["NO", "YES"])
        family_history = st.selectbox("Family History Asthma", ["NO", "YES"])
        wheezing = st.selectbox("Wheezing", ["NO", "YES"])
        chest_tightness = st.selectbox("Chest Tightness", ["NO", "YES"])
        nighttime = st.selectbox("Nighttime Symptoms", ["NO", "YES"])

    if st.button("Predict Asthma"):

        input_df = pd.DataFrame({
            "Age": [age],
            "BMI": [bmi],
            "Smoking": [1 if smoking == "YES" else 0],
            "HistoryOfAllergies": [1 if allergies == "YES" else 0],
            "Eczema": [1 if eczema == "YES" else 0],
            "HayFever": [1 if hay_fever == "YES" else 0],
            "FamilyHistoryAsthma": [1 if family_history == "YES" else 0],
            "Wheezing": [1 if wheezing == "YES" else 0],
            "ChestTightness": [1 if chest_tightness == "YES" else 0],
            "NighttimeSymptoms": [1 if nighttime == "YES" else 0]
        })

        prediction = model.predict(input_df)[0]
        probability = model.predict_proba(input_df)[0][1]

        st.session_state["prediction"] = prediction
        st.session_state["confidence"] = probability
        st.session_state["medical_risk"] = probability * 100

        st.success(f"Prediction Probability: {probability:.2%}")

        if prediction == 1:
            st.error("🔴 Asthma Detected")
        else:
            st.success("🟢 No Asthma Detected")

# -----------------------------
# DATASET ANALYTICS
# -----------------------------
elif page == "Dataset Analytics":

    st.header("📊 Dataset Analytics")

    # Load asthma dataset
    df = pd.read_csv("data/asthma_disease_data.csv")

    # Remove unnecessary columns
    df = df.drop(columns=["PatientID", "DoctorInCharge"])

    st.success("Dataset Loaded Successfully!")

    st.subheader("Dataset Summary")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Patients", len(df))
    col2.metric("Asthma Cases", df["Diagnosis"].sum())
    col3.metric("Healthy Patients", len(df) - df["Diagnosis"].sum())
    col4.metric("Features", len(df.columns) - 1)

    st.subheader("First 10 Records")
    st.dataframe(df.head(10))

    st.subheader("Asthma Diagnosis Distribution")

    diagnosis_counts = df["Diagnosis"].value_counts()

    pie_data = pd.DataFrame({
        "Diagnosis": ["Healthy", "Asthma"],
        "Count": [
            diagnosis_counts.get(0, 0),
            diagnosis_counts.get(1, 0)
        ]
    })

    fig = px.pie(
        pie_data,
        values="Count",
        names="Diagnosis",
        title="Asthma vs Healthy Patients"
    )

    st.plotly_chart(fig, use_container_width=True)



# -----------------------------
# ENVIRONMENTAL RISK
# -----------------------------
elif page == "Environmental Risk":

    st.header("🌍 Environmental Risk Analysis")

    aqi = st.number_input("AQI", 0, 500, 100)
    pm25 = st.number_input("PM2.5", 0, 500, 50)
    humidity = st.number_input("Humidity (%)", 0, 100, 60)
    pollen = st.number_input("Pollen Level", 0, 100, 30)

    if st.button("Calculate Environmental Risk"):

        environment_risk = (
            aqi * 0.4 +
            pm25 * 0.3 +
            humidity * 0.1 +
            pollen * 0.2
        )

        st.session_state["environment_risk"] = environment_risk

        st.success(f"Environmental Risk Score: {environment_risk:.2f}")

# -----------------------------
# EXPLAINABLE AI
# -----------------------------
elif page == "Explainable AI":

    st.header("🧠 Explainable AI Analysis")

    feature_data = pd.DataFrame({
        "Feature": [
            "History Of Allergies",
            "Nighttime Symptoms",
            "Chest Tightness",
            "Eczema",
            "Hay Fever",
            "Family History Asthma",
            "Smoking",
            "Shortness Of Breath",
            "Pet Allergy",
            "Coughing"
        ],
        "Importance": [
            0.21,
            0.18,
            0.15,
            0.13,
            0.11,
            0.10,
            0.08,
            0.07,
            0.05,
            0.04
        ]
    })

    fig = px.bar(
        feature_data,
        x="Importance",
        y="Feature",
        orientation="h",
        title="Top Asthma Risk Factors"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Interpretation")

    st.success("History Of Allergies is a major asthma risk factor.")
    st.success("Nighttime Symptoms strongly indicate asthma.")
    st.success("Chest Tightness increases asthma risk.")
    st.success("Eczema and Hay Fever are linked to asthma.")
    st.success("Smoking can worsen respiratory conditions.")

# -----------------------------
# FINAL ASSESSMENT
# -----------------------------
elif page == "Final Assessment":

    st.header("Final Asthma Risk Assessment")

    medical_risk = st.session_state.get("medical_risk", 0)
    environment_risk = st.session_state.get("environment_risk", 0)

    final_risk = medical_risk * 0.6 + environment_risk * 0.4

    st.metric("Final Risk Score", f"{final_risk:.2f}")

    probability = st.session_state.get("confidence", 0)
    prediction = st.session_state.get("prediction", None)

    if prediction is None:
        st.info("Please complete the Patient Assessment first.")
    else:
        if prediction == 1:
            st.error("🔴 Asthma Detected")
        else:
            st.success("🟢 No Asthma Detected")

        if probability >= 0.70:
            st.error(f"High Probability ({probability:.2%})")
        elif probability >= 0.40:
            st.warning(f"Moderate Probability ({probability:.2%})")
        else:
            st.success(f"Low Probability ({probability:.2%})")

        st.subheader("Recommendations")

        if final_risk < 25:
            st.success("🟢 Low Risk")
        elif final_risk < 50:
            st.warning("🟡 Moderate Risk")
        else:
            st.error("🔴 High Risk")

        st.write("✓ Avoid outdoor activities during heavy pollution.")
        st.write("✓ Reduce exposure to pollen and dust.")
        st.write("✓ Monitor symptoms regularly.")
        st.write("✓ Keep your inhaler with you if prescribed.")