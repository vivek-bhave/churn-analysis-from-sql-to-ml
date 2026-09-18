from joblib import load
from pathlib import Path
import shap
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]
MODEL_DIR = BASE_DIR / "Models"

logistic_model = load(MODEL_DIR / "logistic_regression_pipeline.joblib")
xg_model = load(MODEL_DIR / "xgboost_pipeline.joblib")

logistic_preprocessor = logistic_model.named_steps["preprocessor"]
logistic_classifier = logistic_model.named_steps["model"]

xg_preprocessor = xg_model.named_steps["preprocessor"]
xg_classifier = xg_model.named_steps["model"]

background_data = pd.read_csv(
    MODEL_DIR / "shap_background_lr.csv"
)

background_transformed = logistic_preprocessor.transform(background_data)

logistic_explainer = shap.LinearExplainer(
    logistic_classifier,
    background_transformed
)



def explain_logistic(input_df):
    X_transformed = logistic_preprocessor.transform(input_df)
    shap_values = logistic_explainer.shap_values(X_transformed)
    feature_names = logistic_preprocessor.get_feature_names_out()
    contributions = dict(
        zip(feature_names, shap_values[0])
    )
    aggregated_contributions = {
        "Issue_Level": 0,
        "Delay_Level": 0,
        "Spend_Level": 0,
        "Contract Length": 0
    }

    for feature, value in contributions.items():

        if "Issue_Level" in feature:
            aggregated_contributions["Issue_Level"] += value

        elif "Delay_Level" in feature:
            aggregated_contributions["Delay_Level"] += value

        elif "Spend_Level" in feature:
            aggregated_contributions["Spend_Level"] += value

        elif "Contract Length" in feature:
            aggregated_contributions["Contract Length"] += value
    aggregated_contributions = {
        feature: float(value)
        for feature, value in aggregated_contributions.items()
    }

    print(aggregated_contributions)
    total_contribution = sum(
    abs(value)
    for value in aggregated_contributions.values()
)
    
    relative_contributions = {
        feature: (abs(value) / total_contribution) * 100
        for feature, value in aggregated_contributions.items()
    }

    print(relative_contributions)

    directions = {
        feature: "increases_risk" if value > 0 else "decreases_risk"
        for feature, value in aggregated_contributions.items()
    }

    print(directions)

    return {
    "contributions": aggregated_contributions,
    "relative_contributions": relative_contributions,
    "directions": directions
}



background_data_xg = pd.read_csv(
    MODEL_DIR / "shap_background_xg.csv"
)
print(background_data_xg.columns.tolist())
print(background_data_xg.shape)

background_transformed = xg_preprocessor.transform(
    background_data_xg
)

xg_explainer = shap.TreeExplainer(
    xg_classifier
)

def explain_xgboost(input_df):
    X_transformed = xg_preprocessor.transform(input_df)

    shap_values = xg_explainer.shap_values(X_transformed)

    feature_names = xg_preprocessor.get_feature_names_out()

    contributions = dict(
        zip(feature_names, shap_values[0])
    )

    aggregated_contributions = {
        "Issue_Level": 0,
        "Delay_Level": 0,
        "Spend_Level": 0,
        "Contract Length": 0,
        "Age_Group": 0,
        "LI_Level": 0,
        "Tenure_Level": 0,
        "UF_Level": 0,
        "Gender": 0,
        "Subscription Type": 0
    }

    for feature, value in contributions.items():

        if "Issue_Level" in feature:
            aggregated_contributions["Issue_Level"] += value

        elif "Delay_Level" in feature:
            aggregated_contributions["Delay_Level"] += value

        elif "Spend_Level" in feature:
            aggregated_contributions["Spend_Level"] += value

        elif "Contract Length" in feature:
            aggregated_contributions["Contract Length"] += value

        elif "Age_Group" in feature:
            aggregated_contributions["Age_Group"] += value

        elif "LI_Level" in feature:
            aggregated_contributions["LI_Level"] += value

        elif "Tenure_Level" in feature:
            aggregated_contributions["Tenure_Level"] += value

        elif "UF_Level" in feature:
            aggregated_contributions["UF_Level"] += value

        elif "Gender" in feature:
            aggregated_contributions["Gender"] += value

        elif "Subscription Type" in feature:
            aggregated_contributions["Subscription Type"] += value
    aggregated_contributions = {
        feature: float(value)
        for feature, value in aggregated_contributions.items()
    }

    print(aggregated_contributions)

    total_contribution = sum(
        abs(value)
        for value in aggregated_contributions.values()
    )

    relative_contributions = {
        feature: (abs(value) / total_contribution) * 100
        for feature, value in aggregated_contributions.items()
    }

    print(relative_contributions)

    directions = {
        feature: "increases_risk" if value > 0 else "decreases_risk"
        for feature, value in aggregated_contributions.items()
    }

    print(directions)

    return {
        "contributions": aggregated_contributions,
        "relative_contributions": relative_contributions,
        "directions": directions
    }










    


