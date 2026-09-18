import streamlit as st
import requests
import os


# ----------------------------------------------------
# FastAPI Backend
# ----------------------------------------------------
BACKEND_HOST = os.getenv("API_URL", "http://backend:8000")
API_URL = f"{BACKEND_HOST}/predict"

st.set_page_config(
    page_title="Real-Time Customer Engagement Decision Support System",
    page_icon="🤖",
    layout="wide",
)

# ----------------------------------------------------
# Page Styling
# ----------------------------------------------------
st.markdown("""
<style>
.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}
div[data-testid="stMetricValue"]{
    font-size:28px;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# Helper Functions
# ----------------------------------------------------

def customer_business_value(result):
    st.subheader("💎 Customer Business Value")

    value = result["business_value"]

    col1, col2 = st.columns([2,3])

    with col1:
        if value == "High Business Value":
            st.success("### HIGH BUSINESS VALUE")
        else:
            st.warning("### LOW BUSINESS VALUE")

    with col2:
        st.markdown("**Business Value Indicators**")

        if value == "High Business Value":
            st.markdown("- 🟢 High Spend")
            st.markdown("- 🟢 Annual / Quarterly Contract")
        else:
            st.markdown("- 🟡 Low Spend")
            st.markdown("- 🟡 Monthly Contract")


def prediction_card(result):
    """Display ONLY the selected model output."""

    st.subheader("🚨 AI Prediction Engine")

    if result["predicted_churn"] == 1:
        model_name = "XGBoost"
        prediction = "HIGH CHURN RISK"
        probability = result["churn_probability"] * 100

        st.error(f"## 🔴 {prediction}")
        st.metric("Churn Probability", f"{probability:.1f}%")

        st.caption(
            "Selected Model: XGBoost (used because it identified the customer as a churn risk)."
        )

    else:
        model_name = "Logistic Regression"
        probability = result["retention_probability"] * 100

        if result["predicted_retention"] == 1:
            prediction = "RETENTION OPPORTUNITY"
            st.info(f"## 🔵 {prediction}")
        else:
            prediction = "NO RETENTION NEEDED"
            st.success(f"## 🟢 {prediction}")

        st.metric("Churn Probability", f"{probability:.1f}%")

        st.caption(
            "Selected Model: Logistic Regression (used because XGBoost did not predict churn)."
        )

    col1, col2 = st.columns(2)

    col1.metric("Model Used", model_name)
    col2.metric("Business Value", result["business_value"])

def shap_card(result):
    """SHAP explanation using original customer feature names."""

    st.subheader("🧠 Why did the AI make this prediction?")

    if result["predicted_churn"] == 1:
        st.caption("SHAP explanation generated using XGBoost.")
    else:
        st.caption("SHAP explanation generated using Logistic Regression.")

    shap = result["shap_explanation"]

    contributions = shap["relative_contributions"]
    directions = shap["directions"]

    # Engineered feature -> Original customer feature
    feature_names = {
        "Delay_Level": "Payment Delay",
        "Issue_Level": "Support Calls",
        "Spend_Level": "Total Spend",
        "Contract Length": "Contract Length",
        "Age_Group": "Age",
        "LI_Level": "Last Interaction",
        "UF_Level": "Usage Frequency",
        "Tenure_Level": "Tenure",
        "Subscription Type": "Subscription Type",
        "Gender": "Gender",
    }

    ordered = sorted(
        contributions.items(),
        key=lambda x: x[1],
        reverse=True
    )[:5]

    for feature, percent in ordered:

        display_name = feature_names.get(feature, feature)
        direction = directions[feature]

        left, right = st.columns([5, 1])

        with left:

            if direction == "increases_risk":
                st.markdown(f"🔴 **{display_name}**")
                st.progress(percent / 100)
                st.caption("Increasing churn probability")

            else:
                st.markdown(f"🟢 **{display_name}**")
                st.progress(percent / 100)
                st.caption("Decreasing churn probability")

        with right:
            st.metric("Impact", f"{percent:.1f}%")
def recommendation_card(rule_id, recommendations):

    st.subheader("🎯 Recommended Actions")

    st.success(f"Recommendation Rule Applied: **{rule_id}**")

    for category, services in recommendations.items():

        with st.container(border=True):

            st.markdown(f"### {category}")

            for service_type, actions in services.items():

                st.markdown(f"#### {service_type} Service")

                for action in actions:

                    badge = {
                        "Low": "🟢 Low Cost",
                        "Medium": "🟡 Medium Cost",
                        "High": "🔴 High Cost"
                    }[action["cost"]]

                    st.markdown(
                        f"""
**{action["recommendation"]}**

{badge}
"""
                    )

                st.divider()


def service_status(result):

    st.subheader("⚙️ AI Service Status")

    c1, c2, c3 = st.columns(3)

    c1.success("Prediction Service")

    if result["shap_status"] == "success":
        c2.success("SHAP Service")
    else:
        c2.error("SHAP Service")

    if result["recommendation_status"] == "success":
        c3.success("Recommendation Engine")
    else:
        c3.error("Recommendation Engine")


# ----------------------------------------------------
# Header
# ----------------------------------------------------

st.title("🤖 Real-Time Customer Engagement Decision Support System")

st.markdown("""
AI-powered Decision Support System for **real-time customer engagement, churn prediction,
SHAP explainability, and role-based retention recommendations**.
""")

st.divider()

# ----------------------------------------------------
# Customer Input Form
# ----------------------------------------------------

with st.form("customer_form"):

    st.subheader("Customer Information")
    client_type = st.selectbox(
    "Client Type",
    [
        "interaction_client",
        "monitoring_agent",
        "manager"
    ],
    format_func=lambda x: {
        "interaction_client": "Customer Interaction Client",
        "monitoring_agent": " Customer Monitoring AI Agent",
        "manager": "Senior Retention Manager"
    }[x]
)

    col1, col2 = st.columns(2)

    with col1:

        age = st.number_input("Age", 18, 100, value=35)

        gender = st.selectbox(
            "Gender",
            ["Female", "Male"]
        )

        tenure = st.number_input(
            "Tenure (Months)",
            0,
            120,
            value=24
        )

        usage = st.number_input(
            "Usage Frequency",
            0,
            20,
            value=10
        )

        support_calls = st.number_input(
            "Support Calls",
            0,
            20,
            value=5
        )

    with col2:

        subscription = st.selectbox(
            "Subscription Type",
            ["Basic", "Standard", "Premium"]
        )

        contract = st.selectbox(
            "Contract Length",
            ["Monthly", "Quarterly", "Annual"]
        )

        total_spend = st.number_input(
            "Total Spend",
            value=1200.0
        )

        last_interaction = st.number_input(
            "Last Interaction (Days)",
            value=18
        )

        payment_delay = st.number_input(
            "Payment Delay (Days)",
            value=22
        )

    submitted = st.form_submit_button(
        "🚀 Evaluate Customer",
        use_container_width=True
    )

# ----------------------------------------------------
# API Call
# ----------------------------------------------------

if submitted:

    payload = {
        "client_type": client_type,
        "problem": "high_value_customer_loss",
        "data": {
            "Age": age,
            "Gender": gender,
            "Tenure": tenure,
            "Usage Frequency": usage,
            "Support Calls": support_calls,
            "Subscription Type": subscription,
            "Contract Length": contract,
            "Total Spend": total_spend,
            "Last Interaction": last_interaction,
            "Payment Delay": payment_delay,
        }
    }

    try:

        with st.spinner("Evaluating customer..."):

            response = requests.post(
                API_URL,
                json=payload,
                timeout=10
            )

        response.raise_for_status()

        result = response.json()

    except requests.exceptions.ConnectionError:

        st.error(
            "❌ Unable to connect to FastAPI backend. Make sure Uvicorn is running."
        )
        st.stop()

    except requests.exceptions.RequestException as e:

        st.error(f"API Error: {e}")
        st.stop()

    # ----------------------------------------------------
    # Dashboard Output
    # ----------------------------------------------------

    st.divider()
    customer_business_value(result)
    st.caption(f"Client Session: {client_type.replace('_', ' ').title()}")

    st.divider()
    prediction_card(result)

    st.divider()

    # -----------------------------
    # SHAP Explanation (ALL CLIENTS)
    # -----------------------------
    if result["shap_status"] == "success":
        shap_card(result)
    else:
        st.warning("SHAP explanation unavailable.")

    st.divider()

    # ----------------------------------------
    # Recommendations (Role-Based Access)
    # ----------------------------------------
    if result["recommendation_status"] == "success":

        # Customer Interaction Client
        if client_type == "interaction_client":
            st.subheader("🎯 Engagement Recommendations")
            st.info(
                "Customer Interaction Clients receive customer intelligence only. "
                "Engagement recommendations are available to the Customer Monitoring AI Agent and Retention Manager."
            )

        # AI Monitoring Agent
        elif client_type == "monitoring_agent":

            recommendation_card(
                result["recommendation_rule"],
                result["recommendations"]
            )

            # Show escalation ONLY ONCE
            if result["escalation_required"]:
                st.error(
                    "🚨 Escalation Required: High-cost retention action detected. Forward this customer to the Retention Manager."
                )

        # Manager
        elif client_type == "manager":

            recommendation_card(
                result["recommendation_rule"],
                result["recommendations"]
            )

    else:
        st.warning("Recommendation engine unavailable.")

    st.divider()

    service_status(result)