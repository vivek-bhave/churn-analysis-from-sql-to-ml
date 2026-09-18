from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd
from joblib import load
from pathlib import Path

from app.main import PredictionRequest, HighValueCustomerLossInput

from app.Services.shap_service import (
    explain_logistic,
    explain_xgboost,
)

from app.Services.recommendation_engine import generate_recommendations

# --------------------------------------------------
# Load Models
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[2]
MODEL_DIR = BASE_DIR / "Models"

logistic_model = load(MODEL_DIR / "logistic_regression_pipeline.joblib")
xg_model = load(MODEL_DIR / "xgboost_pipeline.joblib")

app = FastAPI()


# --------------------------------------------------
# Business Value Routing
# --------------------------------------------------

def business_value(data):
    """
    High Business Value:
    - High Spend
    - Annual / Quarterly Contract

    Everything else is Low Business Value.
    """

    if (
        data.spend_level == "High Spend"
        and data.Contract_Length in ["Annual", "Quarterly"]
    ):
        return "High Business Value"

    return "Low Business Value"


# --------------------------------------------------
# Prediction API
# --------------------------------------------------

@app.post("/predict")
def predict(request: PredictionRequest):

    # Frontend always sends high_value_customer_loss
    client_type = request.client_type
    data = HighValueCustomerLossInput(**request.data)

    customer_value = business_value(data)

    # --------------------------------------------------
    # XGBoost Input
    # --------------------------------------------------

    xg_input = pd.DataFrame([{
        "Issue_Level": data.issue_level,
        "Delay_Level": data.delay_level,
        "Spend_Level": data.spend_level,
        "Contract Length": data.Contract_Length,
        "Age_Group": data.age_group,
        "LI_Level": data.li_level,
        "Tenure_Level": data.tenure_level,
        "UF_Level": data.uf_level,
        "Gender": data.Gender,
        "Subscription Type": data.Subscription_Type,
    }])

    # --------------------------------------------------
    # Stage 1 : Run BOTH Models
    # --------------------------------------------------

    # XGBoost Prediction
    churn_probability = float(
        xg_model.predict_proba(xg_input)[0][1]
    )
    predicted_churn = int(churn_probability >= 0.50)

    # Logistic Regression Prediction
    logistic_input = pd.DataFrame([{
        "Issue_Level": data.issue_level,
        "Delay_Level": data.delay_level,
        "Spend_Level": data.spend_level,
        "Contract Length": data.Contract_Length,
    }])

    retention_probability = float(
        logistic_model.predict_proba(logistic_input)[0][1]
    )
    predicted_retention = int(retention_probability >= 0.50)

    # --------------------------------------------------
    # Stage 2 : Select SHAP Model Only
    # --------------------------------------------------

    if predicted_churn == 1:
        shap_function = explain_xgboost
        shap_input = xg_input
    else:
        shap_function = explain_logistic
        shap_input = logistic_input
    # --------------------------------------------------
    # SHAP Service
    # --------------------------------------------------

    try:
        shap_explanation = shap_function(shap_input)
        shap_status = "success"

    except Exception as e:
        print(f"SHAP service failed: {e}")

        shap_status = "unavailable"
        shap_explanation = {}

    # --------------------------------------------------
    # Recommendation Engine
    # --------------------------------------------------

    try:
        recommendations = generate_recommendations(
            client_type=client_type,
            delay_level=data.delay_level,
            issue_level=data.issue_level,
            contract_length=data.Contract_Length,
            spend_level=data.spend_level,
            tenure_level=data.tenure_level,
        )

        recommendation_status = "success"

    except Exception as e:
        print(f"Recommendation service failed: {e}")

        recommendation_status = "unavailable"

        recommendations = {
            "rule_id": None,
            "recommendations": {},
            "escalation_required": False,
        }

    # --------------------------------------------------
    # Unified Response
    # --------------------------------------------------

    return JSONResponse(
    status_code=200,
    content={
        "business_value": customer_value,

        # XGBoost Output
        "predicted_churn": predicted_churn,
        "churn_probability": round(churn_probability, 4),

        # Logistic Regression Output
        "predicted_retention": predicted_retention,
        "retention_probability": round(retention_probability, 4),

        # SHAP (comes from whichever model was selected)
        "shap_status": shap_status,
        "shap_explanation": shap_explanation,

        # Recommendation Engine
        "recommendation_status": recommendation_status,
        "recommendation_rule": recommendations["rule_id"],
        "recommendations": recommendations["recommendations"],
        "escalation_required": recommendations["escalation_required"],
    }
)