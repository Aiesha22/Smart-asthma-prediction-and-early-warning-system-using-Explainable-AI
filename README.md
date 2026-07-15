# 🫁 Smart Asthma Prediction and Early Detection System using Explainable AI

## 📌 Overview

The **Smart Asthma Prediction and Early Detection System** is an AI-powered healthcare application designed to predict asthma risk at an early stage using Machine Learning and Explainable AI (XAI).

The system combines **patient health information**, **environmental factors**, and **weather conditions** to provide asthma risk prediction, personalized recommendations, and explainable insights using SHAP.

The goal of this project is to support early detection, improve awareness of asthma triggers, and help users understand the factors influencing their prediction.

---

# 🚀 Features

## 🔐 User Authentication

- User Registration
- Email OTP Verification
- Secure Password Hashing
- Login System
- Forgot Password with Email Verification Code


## 🩺 Asthma Risk Prediction

- Predicts asthma risk using Machine Learning models
- Provides prediction probability/confidence score
- Classifies users into:
  - Asthma Risk
  - Healthy


## 🧠 Explainable AI (XAI)

- SHAP-based model explanation
- Identifies important factors affecting prediction
- Improves transparency and trust in AI decisions


## 🌍 Environmental Risk Analysis

The system considers environmental conditions:

- Air Quality
- Weather Conditions
- Temperature
- Humidity


## ⚠️ Early Warning System

Provides:

- Risk alerts
- Personalized recommendations
- Preventive suggestions


## 📊 Data Analytics Dashboard

Includes:

- Dataset visualization
- Feature analysis
- Risk distribution
- Environmental insights


## 🌐 Multi-Language Support

The application supports:

- English
- Telugu
- Hindi
- Tamil
- Urdu


## 📄 Report Generation

Generates prediction reports containing:

- Patient information
- Risk level
- Confidence score
- Recommendations

---

# 🏗️ System Architecture
             User
              |
              |
      Streamlit Web Application
              |
    -------------------------
    |                       |

    
---

# 🛠️ Technologies Used

## Programming Language

- Python


## Machine Learning

- Scikit-learn
- XGBoost
- Random Forest


## Explainable AI

- SHAP


## Data Processing

- Pandas
- NumPy


## Visualization

- Plotly
- Matplotlib


## Application Framework

- Streamlit


## Database

- SQLite


## Other Tools

- Git
- GitHub
- VS Code

---

# 📂 Project Structure
Smart-Asthma-Prediction-XAI/

│
├── app.py
├── login.py
├── register.py
├── forgot_password.py
├── database.py
├── email_utils.py
├── translations.py
│
├── models/
│ └── asthma_model.pkl
│
├── explainability/
│ └── shap_analysis.py
│
├── data/
│ ├── asthma_disease_data.csv
│ ├── Air Quality.csv
│ └── weather_dataset_2025.csv
│
├── requirements.txt
├── README.md
└── .gitignore


---

# 📊 Machine Learning Models

The project uses:

## Random Forest Classifier

Used for asthma risk classification.

Advantages:

- Handles complex medical features
- Reduces overfitting
- Provides feature importance


## XGBoost Classifier

Used for improved prediction performance.

Advantages:

- High accuracy
- Efficient learning
- Handles structured medical data


---

# 📈 Explainable AI using SHAP

SHAP (SHapley Additive exPlanations) is used to explain model predictions.

It helps answer:

- Why was asthma risk predicted?
- Which factors increased risk?
- Which factors reduced risk?

Example factors:

- Age
- BMI
- Smoking
- Allergies
- Wheezing
- Family History
- Environmental Conditions

<Markdown>
<p align="center">
<img src="assets/logo.png" width="200">
</p>

<h1 align="center">
Smart Asthma Prediction and Early Detection System using Explainable AI
</h1>

<p align="center">
AI-powered asthma risk prediction using Machine Learning and Explainable AI
</p>