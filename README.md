# 🫁 Smart Asthma Prediction and Early Detection System using Explainable AI

## 📌 Project Overview

The **Smart Asthma Prediction and Early Detection System using Explainable AI** is a machine learning-based healthcare application designed to predict asthma risk by combining **patient medical data**, **environmental factors**, and **weather conditions**. The system provides an early assessment of asthma risk along with personalized recommendations and explainable AI insights to help users understand the prediction.

This project is developed using **Python**, **Streamlit**, **Scikit-learn**, **XGBoost**, and **SHAP (Explainable AI)** to create an interactive and user-friendly dashboard.

---

## 🎯 Objectives

* Predict asthma risk using patient health information.
* Analyze environmental conditions that may trigger asthma.
* Provide personalized recommendations for asthma prevention.
* Explain prediction results using Explainable AI (SHAP).
* Support multiple languages for improved accessibility.

---

## ✨ Features

* 👤 Patient Medical Assessment
* 🌍 Environmental Risk Analysis
* 🌦️ Weather Data Integration
* 🤖 Machine Learning-Based Prediction
* 📊 Explainable AI (SHAP)
* 📈 Interactive Dashboard using Streamlit
* 💾 SQLite Database Integration
* 🌐 Multilingual User Interface (English, Telugu, Hindi, Tamil, Urdu)
* 💡 Personalized Health Recommendations

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Libraries

* Streamlit
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* SHAP
* Plotly
* Joblib
* SQLite3

### Database

* SQLite

### Development Tools

* Visual Studio Code
* Git
* GitHub

---

## 📂 Project Structure

```text
Smart Asthma Prediction and Early Detection System/
│
├── app.py
├── database.py
├── asthma.db
├── requirements.txt
├── README.md
│
├── data/
│   ├── asthma_disease_data.csv
│   ├── Air Quality.csv
│   └── weather_dataset_2025.csv
│
├── explainability/
│   └── shap_analysis.py
│
├── models/
│   ├── xgboost_model.py
│   ├── risk_score.py
│   ├── environment_risk.py
│   └── final_risk_score.py
│
├── notebooks/
│
├── utils/
│
└── translations.py
```

---

## 📊 Dataset

The project uses three datasets:

### 1. Patient Medical Dataset

Contains:

* Age
* Gender
* BMI
* Smoking Status
* Family History
* Lung Function (FEV1, FVC)
* Symptoms
* Diagnosis

### 2. Air Quality Dataset

Contains:

* CO
* NO₂
* NOx
* O₃
* Temperature
* Humidity
* Air Quality Indicators

### 3. Weather Dataset

Contains:

* Temperature
* Humidity
* Wind Speed
* Rainfall
* Weather Condition

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

### Navigate to the project folder

```bash
cd YOUR_REPOSITORY
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

```bash
streamlit run app.py
```

The application will start locally and can be accessed in your browser.

---

## 📈 Workflow

1. Enter patient medical information.
2. Analyze environmental and weather conditions.
3. Predict asthma risk using trained machine learning models.
4. Display Explainable AI (SHAP) visualizations.
5. Generate personalized recommendations.
6. View the interface in the selected language.

---

## 🤖 Machine Learning Models

* Random Forest Classifier
* XGBoost Classifier

---

## 📊 Explainable AI

The project uses **SHAP (SHapley Additive exPlanations)** to explain model predictions by showing how each feature contributes to the final asthma risk score.

---

## 🌐 Multilingual Support

The application supports:

* English
* Telugu
* Hindi
* Tamil
* Urdu

---

## 🔮 Future Enhancements

* Real-time AQI integration
* IoT sensor integration
* Mobile application
* Doctor dashboard
* Cloud deployment
* Patient history tracking
* Email and SMS alerts
* Hospital integration
* Voice assistance
* Wearable device integration

---

## 👩‍💻 Author

**Shaik Aiesha**

B.Tech – Computer Science Engineering (DFS & AI)

Dr. M.G.R. Educational and Research Institute

GitHub: https://github.com/Aiesha22

---

## 📄 License

This project is developed for academic and educational purposes.
