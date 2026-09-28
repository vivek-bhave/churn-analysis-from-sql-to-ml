# Request Validation Layer

The **Request Validation Layer** is the entry point of the backend prediction pipeline. It is implemented using **Pydantic** to validate incoming API requests, enforce data constraints, and perform feature engineering before the request reaches the machine learning models and recommendation engine.

This layer guarantees that every downstream component receives a structured and validated customer profile with both raw customer attributes and engineered business features.

---

## Purpose

The Request Validation Layer performs four responsibilities:

* Validate incoming customer data against predefined schemas.
* Enforce numerical and categorical constraints.
* Generate engineered categorical features required by the machine learning pipeline.
* Convert the JSON request into strongly typed Python objects for the backend.

---

## Input Schema — `CustomerInput`

`CustomerInput` defines the complete customer profile required for churn prediction and recommendation generation.

### Customer Features

| Feature           | Type        | Validation                 | Description                                      |
| ----------------- | ----------- | -------------------------- | ------------------------------------------------ |
| Age               | Float       | 0 ≤ Age less than 120      | Customer age.                                    |
| Gender            | Categorical | Female, Male               | Customer gender.                                 |
| Tenure            | Float       | Tenure ≥ 0                 | Duration of customer relationship.               |
| Usage Frequency   | Float       | Usage Frequency ≥ 0        | Weekly customer engagement frequency.            |
| Support Calls     | Float       | Support Calls ≥ 0          | Weekly support interactions or complaints.       |
| Subscription Type | Categorical | Basic, Standard, Premium   | Customer subscription tier.                      |
| Contract Length   | Categorical | Monthly, Quarterly, Annual | Subscription contract duration.                  |
| Total Spend       | Float       | Total Spend ≥ 0            | Total customer spending.                         |
| Last Interaction  | Float       | Last Interaction ≥ 0       | Days since the customer's last interaction.      |
| Payment Delay     | Float       | Payment Delay ≥ 0          | Days delayed in subscription renewal or payment. |

### Validation Rules

Pydantic automatically validates every incoming request before executing the prediction endpoint.

* Rejects missing required fields.
* Rejects invalid categorical values.
* Rejects values outside the allowed numeric range.
* Converts validated JSON into a `CustomerInput` object.

If validation fails, FastAPI returns a **422 Validation Error** without executing the prediction pipeline.

---

## Automatic Feature Engineering

The validation model also computes engineered categorical features using `@computed_field`. These features are derived immediately after validation and become part of the validated customer object.

| Engineered Feature | Derived From     | Business Logic                            |
| ------------------ | ---------------- | ----------------------------------------- |
| Issue Level        | Support Calls    | Low (0–2), Medium (3–4), High (5+)        |
| Delay Level        | Payment Delay    | Low (0–15), Medium (16–20), High (21+)    |
| Spend Level        | Total Spend      | Low (≤508), High ({">"}508)               |
| Age Group          | Age              | Very Young, Young Adult, Old Adult, Old   |
| LI Level           | Last Interaction | Low LI (≤15 days), High LI ({">"}15 days) |
| UF Level           | Usage Frequency  | Low UF (≤9), High UF ({">"}9)             |
| Tenure Level       | Tenure           | Very Low, Low, Medium, High               |

### Why Feature Engineering Happens Here

Feature engineering is performed inside the validation layer instead of the machine learning service because:

* Both ML models use engineered categorical features as model inputs.
* The recommendation engine uses the same engineered features for business rule matching.
* SHAP explanations use the same transformed feature representation.
* Feature transformation is implemented once and reused throughout the backend.

This eliminates duplicate preprocessing logic across multiple backend services.

---

## Request Wrapper — `PredictionRequest`

The backend API accepts a wrapper request model containing request metadata and customer data.

### Request Structure

| Field       | Purpose                                                                              |
| ----------- | ------------------------------------------------------------------------------------ |
| client_type | Identifies the requesting client (interaction client, monitoring agent, or manager). |
| data        | Validated `CustomerInput` object containing customer attributes.                     |

### Client Types

| Client Type        | Backend Purpose                                     |
| ------------------ | --------------------------------------------------- |
| interaction_client | Customer-facing AI interaction interface.           |
| monitoring_agent   | Internal support monitoring dashboard.              |
| manager            | Manager portal with complete recommendation access. |

The `client_type` is **request metadata**, not a customer feature. It is later used by the Recommendation Engine to apply **Role-Based Decision Logic (RBAC)** and filter recommendations according to user permissions.

---

## Output of the Validation Layer

After successful validation, the backend produces a structured `CustomerInput` object containing:

* Validated raw customer attributes.
* Automatically generated engineered business features.
* A standardized feature representation shared across the ML prediction service, SHAP explainability service, and recommendation engine.

This validated object becomes the single source of truth for all downstream backend processing stages.
