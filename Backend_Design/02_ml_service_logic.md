# Machine Learning Prediction Logic

The **Machine Learning Prediction Layer** is responsible for generating churn intelligence from a validated customer profile. Instead of relying on a single predictive model, the Decision Support System executes **two complementary machine learning models** in parallel and combines their outputs to support both customer retention decisions and model explainability.

The prediction layer consists of three stages:

1. Business Value Classification
2. Dual Model Prediction (XGBoost + Logistic Regression)
3. Model Selection for Explainability

---

## Purpose

The prediction layer transforms engineered customer features into business intelligence that can be consumed by downstream services.

Its responsibilities are:

* Classify the customer's business value.
* Predict the probability that a customer will churn.
* Predict the probability that a customer belongs to the retention (non-churn) segment.
* Select the appropriate model for SHAP explainability.

---

## Model Loading

Both trained pipelines are loaded during application startup using **Joblib**.

| Model                        | Purpose                                  |
| ---------------------------- | ---------------------------------------- |
| XGBoost Pipeline             | Predicts customer churn probability.     |
| Logistic Regression Pipeline | Predicts customer retention probability. |

Loading models during startup avoids repeated disk loading for every API request and keeps inference latency low.

---

### Stage 1 — Business Value Classification

#### Purpose

Before running the machine learning models, the backend classifies the **business value** of the customer. This classification is independent of churn prediction and is included in the API response as business intelligence for the user.

Its purpose is to help support teams and managers understand the importance of a customer and choose an appropriate level of engagement during retention efforts.

#### Classification Logic

| Business Value            | Criteria                                     |
| ------------------------- | -------------------------------------------- |
| **High Business Value**   | High Spend **and** Annual/Quarterly Contract |
| **Medium Business Value** | High Spend **or** Annual/Quarterly Contract  |
| **Low Business Value**    | Low Spend **and** Monthly Contract           |

#### Why Business Value is Calculated

Business value represents the customer's overall importance from a business perspective rather than their likelihood of churning.

* **High Business Value** customers contribute higher revenue and have longer-term contractual commitment, making them candidates for premium retention efforts.
* **Medium Business Value** customers satisfy one important business criterion and may require moderate engagement.
* **Low Business Value** customers receive standard engagement and retention treatment.

This classification is displayed in the frontend so managers and support staff can quickly understand customer priority while reviewing churn predictions and recommendations.

#### Output

The backend returns one of three business value categories in the API response:

* High Business Value
* Medium Business Value
* Low Business Value

The frontend uses this output to visually indicate customer priority and support more informed customer engagement decisions.


## Stage 2 — Dual Model Prediction

### Why Two Models?

Rather than selecting a single "best" model, the backend uses two models because they perform better on **different customer segments**.

* **XGBoost** is better at identifying customers who are likely to churn.
* **Logistic Regression** performs better at identifying customers who are likely to remain with the service (non-churn customers).

The backend therefore uses each model for the scenario where it provides stronger decision support instead of forcing one model to handle both interpretations.

### Feature Engineering for Each Model

Each model receives a feature set aligned with how it was trained.

#### XGBoost Input Features

XGBoost receives a richer customer profile containing behavioral, demographic, and subscription information.

| Feature Group         | Features                                                                             |
| --------------------- | ------------------------------------------------------------------------------------ |
| Customer Behaviour    | Issue Level, Delay Level, Spend Level, Usage Frequency Level, Last Interaction Level |
| Customer Profile      | Age Group, Gender, Subscription Type                                                 |
| Customer Relationship | Contract Length, Tenure Level                                                        |

This feature set allows the model to capture complex interactions between customer behaviour and churn risk.

#### Logistic Regression Input Features

Logistic Regression receives a smaller business-oriented feature set.

| Feature Group      | Features                 |
| ------------------ | ------------------------ |
| Customer Behaviour | Issue Level, Delay Level |
| Customer Value     | Spend Level              |
| Subscription       | Contract Length          |

This simplified feature space produces an interpretable model focused on retention-oriented business indicators.

---

## Parallel Model Execution

Both models execute for every prediction request.

### XGBoost Prediction

The XGBoost pipeline produces:

* Churn probability.
* Binary churn prediction using a threshold of **0.50**.

### Logistic Regression Prediction

The Logistic Regression pipeline produces:

* Retention probability.
* Binary retention prediction using a threshold of **0.50**.

Running both models simultaneously ensures that the backend has predictions from both perspectives without requiring multiple API requests.

---

## Model Selection Strategy

The backend uses a simple routing strategy after inference.

| Condition                       | Selected Model      |
| ------------------------------- | ------------------- |
| Customer predicted as Churn     | XGBoost             |
| Customer predicted as Non-Churn | Logistic Regression |

The selected model becomes the source for SHAP explainability.

This design ensures that explanations are generated using the model responsible for the prediction being communicated to the user.

---

## Why This Architecture Was Chosen

The prediction pipeline intentionally separates **churn identification** from **retention interpretation**.

* XGBoost captures complex nonlinear customer behaviour associated with churn risk.
* Logistic Regression provides a simpler and more interpretable decision boundary for customers predicted to stay.
* Both predictions are returned in a unified API response, allowing downstream services to use churn probability, retention probability, and business value together.

This architecture keeps the prediction service modular while allowing explainability and recommendation logic to operate on the most appropriate model output.

---

### Detailed Model Performance Comparison

The complete machine learning experimentation process—including preprocessing, feature engineering, evaluation metrics, confusion matrices, ROC curves, business-value analysis, and the rationale for selecting **XGBoost** for churn prediction and **Logistic Regression** for retention prediction—is documented separately in the model comparison notebook.

> 📓 **Detailed Model Performance Comparison:** See `Notebooks/08_Model_Performace_Comparison.md`.