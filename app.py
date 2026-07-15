import plotly.graph_objects as go
import streamlit as st
import pandas as pd
import plotly.express as px
import joblib
from report import generate_report
from shap_analysis import get_shap_values
from weather_api import get_weather
from early_warning import early_warning
from login import login 

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    login()
    st.stop()

if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()  

st.sidebar.markdown("---")

if st.sidebar.button("🚪 Logout"):

    st.session_state["logged_in"] = False
    st.rerun()      

from translations import translations
from database import (
    create_table,
    create_users_table,
    save_prediction,
    load_history,
    delete_history

)
create_table()
create_users_table()

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Smart Asthma Prediction",
    layout="wide"
)

# -----------------------------
# Language Selection
# -----------------------------
language = st.sidebar.selectbox(
    "🌐 Select Language",
    ["English", "Telugu", "Hindi", "Tamil", "Urdu"]
)

# Selected language dictionary
t = translations[language]

# Load trained machine learning model
model = joblib.load("models/asthma_model.pkl")
create_table()
create_users_table()

st.title(t["title"])
st.markdown(t["system_description"])

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

    col1, col2 = st.columns(2)

    with col1:

        age = st.number_input(
            t["age"],
            1,
            100,
            25
        )

        bmi = st.number_input(
            t["bmi"],
            10.0,
            50.0,
            22.0
        )

        smoking = st.selectbox(
            t["smoking"],
            ["YES", "NO"]
        )

        allergies = st.selectbox(
            t["history_allergies"],
            ["YES", "NO"]
        )


    with col2:

        hay_fever = st.selectbox(
            t["hay_fever"],
            ["YES", "NO"]
        )

        family_history = st.selectbox(
            t["family_history"],
            ["YES", "NO"]
        )

        wheezing = st.selectbox(
            t["wheezing"],
            ["YES", "NO"]
        )

        chest_tightness = st.selectbox(
            t["chest_tightness"],
            ["YES", "NO"]
        )

        nighttime = st.selectbox(
            t["nighttime"],
            ["YES", "NO"]
        )

        eczema = st.selectbox(
            t["eczema"],
            ["YES", "NO"]
        )


    if st.button(t["predict"]):

        input_df = pd.DataFrame({

            "Age": [age],

            "BMI": [bmi],

            "Smoking": [
                1 if smoking == "YES" else 0
            ],

            "HistoryOfAllergies": [
                1 if allergies == "YES" else 0
            ],

            "Eczema": [
                1 if eczema == "YES" else 0
            ],

            "HayFever": [
                1 if hay_fever == "YES" else 0
            ],

            "FamilyHistoryAsthma": [
                1 if family_history == "YES" else 0
            ],

            "Wheezing": [
                1 if wheezing == "YES" else 0
            ],

            "ChestTightness": [
                1 if chest_tightness == "YES" else 0
            ],

            "NighttimeSymptoms": [
                1 if nighttime == "YES" else 0
            ]

        })


        prediction = model.predict(input_df)[0]

        probability = model.predict_proba(input_df)[0][1]


        st.session_state["input_df"] = input_df
        st.session_state["prediction"] = prediction
        st.session_state["confidence"] = probability

        st.session_state["medical_risk"] = probability * 100

        st.session_state["age"] = age
        st.session_state["bmi"] = bmi



        medical_risk = probability * 100

        environment_risk = st.session_state.get(
            "environment_risk",
            0
        )


        final_risk = (
            medical_risk * 0.6 +
            environment_risk * 0.4
        )



        save_prediction(
            age,
            bmi,
            "Asthma" if prediction == 1 else "Healthy",
            probability,
            final_risk
        )



        st.success(
            f"{t['prediction_probability']}: {probability:.2%}"
        )


        if prediction == 1:

            st.error(
                t["asthma_detected"]
            )

        else:

            st.success(
                t["healthy_detected"]
            )
# -----------------------------
# DATASET ANALYTICS
# -----------------------------
elif page == "Dataset Analytics":

    st.header(t["dataset_analytics"])

    # Load dataset
    df = pd.read_csv("data/asthma_disease_data.csv")

    # Sidebar Filters
    st.sidebar.subheader(t["dataset_filters"])

    age_range = st.sidebar.slider(
        t["age_range"],
        int(df["Age"].min()),
        int(df["Age"].max()),
        (
            int(df["Age"].min()),
            int(df["Age"].max())
        )
    )

    diagnosis = st.sidebar.selectbox(
        t["diagnosis"],
        [
            t["all"],
            t["healthy"],
            t["asthma"]
        ]
    )

    # Apply filters
    filtered_df = df[
        (df["Age"] >= age_range[0]) &
        (df["Age"] <= age_range[1])
    ]

    if diagnosis == t["healthy"]:
        filtered_df = filtered_df[filtered_df["Diagnosis"] == 0]

    elif diagnosis == t["asthma"]:
        filtered_df = filtered_df[filtered_df["Diagnosis"] == 1]


    # Remove unwanted columns
    filtered_df = filtered_df.drop(
        columns=["PatientID", "DoctorInCharge"],
        errors="ignore"
    )


    st.success(t["dataset_loaded"])


    # Dashboard Overview
    st.subheader(t["dashboard_overview"])


    total_patients = len(filtered_df)
    asthma_cases = len(filtered_df[filtered_df["Diagnosis"] == 1])
    healthy_cases = len(filtered_df[filtered_df["Diagnosis"] == 0])
    average_age = filtered_df["Age"].mean()


    col1, col2, col3, col4 = st.columns(4)


    with col1:
        st.metric(
            t["total_patients"],
            total_patients
        )


    with col2:
        st.metric(
            t["asthma_cases"],
            asthma_cases
        )


    with col3:
        st.metric(
            t["healthy_patients"],
            healthy_cases
        )


    with col4:
        st.metric(
            t["average_age"],
            f"{average_age:.1f}"
        )


    # Pie Chart
    st.subheader(t["diagnosis_distribution"])


    diagnosis_counts = filtered_df["Diagnosis"].value_counts()


    pie_data = pd.DataFrame({
        "Diagnosis": [
            t["healthy"],
            t["asthma"]
        ],
        "Count": [
            diagnosis_counts.get(0,0),
            diagnosis_counts.get(1,0)
        ]
    })


    fig = px.pie(
        pie_data,
        values="Count",
        names="Diagnosis",
        title=t["asthma_vs_healthy"]
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # Age Distribution
    st.subheader(t["age_distribution"])


    fig = px.histogram(
        filtered_df,
        x="Age",
        nbins=20,
        title=t["patient_age_distribution"]
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # BMI Distribution
    st.subheader(t["bmi_distribution"])


    fig = px.histogram(
        filtered_df,
        x="BMI",
        nbins=20,
        title=t["bmi_distribution"]
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # Show Data
    st.subheader(t["first_records"])


    st.dataframe(
        filtered_df.head(10)
    )



# -----------------------------
# ENVIRONMENTAL RISK
# -----------------------------
elif page == "Environmental Risk":

    st.header(t["environmental_risk_analysis"])

    city = st.text_input(
        t["enter_city"],
        "Chennai"
    )

    if st.button(t["get_live_weather"]):

        weather = get_weather(city)

        if weather is None:
            st.error(t["city_not_found"])

        else:

            st.success(t["weather_success"])

            st.write(
                f"{t['temperature']}: {weather['temperature']} °C"
            )

            st.write(
                f"{t['humidity']}: {weather['humidity']} %"
            )

            st.write(
                f"{t['weather']}: {weather['condition']}"
            )


            aqi = st.number_input(
                t["aqi"],
                0,
                500,
                100
            )

            pm25 = st.number_input(
                t["pm25"],
                0,
                500,
                50
            )

            pollen = st.number_input(
                t["pollen"],
                0,
                100,
                30
            )


            if st.button(
                t["calculate_environmental_risk"]
            ):

                environment_risk = (
                    aqi * 0.4 +
                    pm25 * 0.3 +
                    weather["humidity"] * 0.1 +
                    pollen * 0.2
                )


                st.session_state["environment_risk"] = environment_risk
                st.session_state["humidity"] = weather["humidity"]
                st.session_state["aqi"] = aqi


                st.success(
                    f"{t['environmental_risk_score']}: {environment_risk:.2f}"
                )
# -----------------------------
# EXPLAINABLE AI
# -----------------------------
elif page == "Explainable AI":

    st.header(t["explainable_ai_analysis"])

    if "input_df" not in st.session_state:

        st.info(t["complete_patient_assessment"])

    else:

        input_df = st.session_state["input_df"]

        explanation = get_shap_values(input_df)


        fig = px.bar(
            explanation.head(10),
            x="SHAP Value",
            y="Feature",
            orientation="h",
            title=t["top_features"],
            color="Impact",
            color_discrete_map={
                t["increases_risk"]: "#ef553b",
                t["decreases_risk"]: "#00cc96",
            },
        )


        fig.update_layout(
            yaxis={"categoryorder": "total ascending"}
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


        st.subheader(
            t["feature_explanation"]
        )


        for _, row in explanation.head(5).iterrows():

            feature = row["Feature"]


            if feature == "Age":
                msg = t["age_msg"]

            elif feature == "BMI":
                msg = t["bmi_msg"]

            elif feature == "Smoking":
                msg = t["smoking_msg"]

            elif feature == "HistoryOfAllergies":
                msg = t["allergy_msg"]

            elif feature == "FamilyHistoryAsthma":
                msg = t["family_msg"]

            elif feature == "Wheezing":
                msg = t["wheezing_msg"]

            elif feature == "ChestTightness":
                msg = t["chest_msg"]

            elif feature == "NighttimeSymptoms":
                msg = t["night_msg"]

            elif feature == "HayFever":
                msg = t["hayfever_msg"]

            elif feature == "Eczema":
                msg = t["eczema_msg"]

            else:
                msg = t["default_msg"]



            if row["SHAP Value"] > 0:

                st.error(
                    f"🔺 **{feature}**\n\n{msg}\n\n{t['increased_prediction']}"
                )

            else:

                st.success(
                    f"🔹 **{feature}**\n\n{msg}\n\n{t['decreased_prediction']}"
                )

# -----------------------------
# FINAL ASSESSMENT
# -----------------------------
elif page == "Final Assessment":

    st.header(t["final_asthma_risk"])

    # Get values from session state
    medical_risk = st.session_state.get("medical_risk", 0)
    environment_risk = st.session_state.get("environment_risk", 0)
    prediction = st.session_state.get("prediction", None)
    probability = st.session_state.get("confidence", 0)


    # Calculate final risk
    final_risk = medical_risk * 0.6 + environment_risk * 0.4
    st.session_state["final_risk"] = final_risk


    # Gauge Chart
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=final_risk,
        title={
            "text": t["final_risk_score"]
        },
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "darkred"},
            "steps": [
                {"range": [0, 25], "color": "lightgreen"},
                {"range": [25, 50], "color": "yellow"},
                {"range": [50, 75], "color": "orange"},
                {"range": [75, 100], "color": "red"}
            ]
        }
    ))


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # Risk Summary
    st.subheader(t["risk_summary"])


    col1, col2, col3 = st.columns(3)


    with col1:
        st.metric(
            t["medical_risk"],
            f"{medical_risk:.1f}%"
        )


    with col2:
        st.metric(
            t["environmental_risk"],
            f"{environment_risk:.1f}%"
        )


    with col3:
        st.metric(
            t["final_risk"],
            f"{final_risk:.1f}%"
        )


    # Check prediction
    if prediction is None:

        st.info(
            t["complete_assessment"]
        )

    else:

        st.subheader(
            t["prediction"]
        )


        if prediction == 1:

            st.error(
                t["asthma_detected"]
            )

        else:

            st.success(
                t["healthy_detected"]
            )


        # Confidence
        st.subheader(
            t["prediction_confidence"]
        )


        if probability >= 0.70:

            st.error(
                f"{t['high_probability']} ({probability:.2%})"
            )


        elif probability >= 0.40:

            st.warning(
                f"{t['moderate_probability']} ({probability:.2%})"
            )


        else:

            st.success(
                f"{t['low_probability']} ({probability:.2%})"
            )


        # Recommendations
        st.subheader(
            t["recommendations"]
        )


        if final_risk < 25:

            st.success(
                t["low_risk"]
            )

            st.success(
                t["continue_healthy"]
            )

            st.success(
                t["exercise"]
            )

            st.success(
                t["hydrated"]
            )


        elif final_risk < 50:

            st.warning(
                t["moderate_risk"]
            )

            st.warning(
                t["wear_mask"]
            )

            st.warning(
                t["avoid_pollen"]
            )

            st.warning(
                t["monitor_symptoms"]
            )


        else:

            st.error(
                t["high_risk"]
            )

            st.error(
                t["consult_doctor"]
            )

            st.error(
                t["carry_inhaler"]
            )

            st.error(
                t["avoid_smoke"]
            )

            st.error(
                t["oxygen"]
            )


        # Early Warning
        st.subheader(
            t["early_warning"]
        )


        humidity = st.session_state.get("humidity", 60)
        aqi = st.session_state.get("aqi", 100)


        warning = early_warning(
            final_risk,
            humidity,
            aqi
        )


        st.info(warning)


        # PDF Report
        st.subheader(
            t["report"]
        )


        if st.button(
            t["generate_pdf"]
        ):

            age = st.session_state.get("age", 0)
            bmi = st.session_state.get("bmi", 0)


            generate_report(
                "Asthma_Report.pdf",
                age=age,
                bmi=bmi,
                prediction="Asthma" if prediction == 1 else "Healthy",
                probability=probability,
                medical_risk=medical_risk,
                environment_risk=environment_risk,
                final_risk=final_risk
            )


            with open(
                "Asthma_Report.pdf",
                "rb"
            ) as pdf_file:

                st.download_button(
                    label=t["download_report"],
                    data=pdf_file,
                    file_name="Asthma_Report.pdf",
                    mime="application/pdf"
                )

# -----------------------------
# PATIENT HISTORY
# -----------------------------
elif page == "Patient History":

    st.header(t["patient_history_title"])

    history = load_history()


    if history.empty:

        st.info(
            t["no_history"]
        )


    else:

        col1, col2, col3 = st.columns(3)


        col1.metric(
            t["total_predictions"],
            len(history)
        )


        col2.metric(
            t["asthma_cases"],
            len(history[history["prediction"] == "Asthma"])
        )


        col3.metric(
            t["healthy_cases"],
            len(history[history["prediction"] == "Healthy"])
        )


        st.dataframe(history)


        if st.button(
            t["clear_history"]
        ):

            delete_history()

            st.success(
                t["history_deleted"]
            )

            st.rerun()
