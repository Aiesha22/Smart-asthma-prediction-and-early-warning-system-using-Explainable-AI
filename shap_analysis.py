import shap
import joblib
import pandas as pd
import numpy as np

# Load Random Forest model
model = joblib.load("models/asthma_model.pkl")


def get_shap_values(input_df):

    explainer = shap.TreeExplainer(model)

    shap_values = explainer.shap_values(input_df)

    if isinstance(shap_values, list):
        values = shap_values[1][0]

    elif isinstance(shap_values, np.ndarray):

        if shap_values.ndim == 3:
            values = shap_values[0, :, 1]

        elif shap_values.ndim == 2:
            values = shap_values[0]

        else:
            values = shap_values

    explanation = pd.DataFrame({
        "Feature": input_df.columns,
        "SHAP Value": values
    })

    explanation["Impact"] = explanation["SHAP Value"].apply(
        lambda x: "Increases Risk" if x > 0 else "Decreases Risk"
    )

    explanation["Abs"] = explanation["SHAP Value"].abs()

    explanation = explanation.sort_values(
        by="Abs",
        ascending=False
    )

    explanation.drop(columns="Abs", inplace=True)

    return explanation