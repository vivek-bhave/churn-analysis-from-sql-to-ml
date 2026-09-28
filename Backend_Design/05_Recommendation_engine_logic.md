# Recommendation Engine Logic

The Recommendation Engine converts the engineered customer behaviour into **actionable retention strategies**. While the machine learning models identify customers at risk of churn, the recommendation engine determines **what engagement or retention actions should be taken** for that customer.

The service uses a **rule-based decision system** backed by MariaDB. It matches a customer's behavioural profile against predefined recommendation rules, retrieves the associated retention actions, applies role-based access control, and returns a structured recommendation response to the frontend.

---

## Purpose

The Recommendation Engine performs five responsibilities:

* Match a customer's engineered behavioural profile with a predefined recommendation rule.
* Retrieve all retention actions associated with the matched rule.
* Filter recommendations based on the requesting client's permissions.
* Organize recommendations into business-friendly categories.
* Return a structured response for the frontend.

Unlike the ML prediction service, this component is **deterministic**—the same customer profile always maps to the same recommendation rule.

---

## Recommendation Engine Pipeline

`CustomerInput → Rule Matching → Fetch Recommendation Actions → Role-Based Filtering → Group & Sort Recommendations → JSON Response`

---

## Stage 1 — Database Connection

### Purpose

The recommendation engine connects to **MariaDB** to retrieve recommendation rules and retention actions.

### Processing Logic

The backend creates a database connection using environment variables, allowing the same service to run locally and inside Docker without changing the application logic.

| Environment Variable | Purpose                             |
| -------------------- | ----------------------------------- |
| `DB_HOST`            | MariaDB hostname or container name. |
| `DB_PORT`            | Database port (3306).               |
| `DB_USER`            | Database username.                  |
| `DB_PASSWORD`        | Database password.                  |
| `DB_NAME`            | Churn database name.                |

A new connection is created only when a database query is executed and is closed immediately after the query completes.

### Output

An active MariaDB connection used for querying recommendation rules and actions.

---

## Stage 2 — Rule Matching

### Purpose

The first decision made by the recommendation engine is identifying **which recommendation rule matches the customer**.

### Input Features

The engine receives the engineered behavioural profile generated during request validation.

| Behavioural Feature | Purpose                         |
| ------------------- | ------------------------------- |
| Delay Level         | Payment delay behaviour.        |
| Issue Level         | Complaint frequency.            |
| Spend Level         | Customer spending category.     |
| Contract Length     | Subscription commitment.        |
| Tenure Level        | Customer relationship strength. |

### Processing Logic

Before querying the database, the backend converts ML feature labels into the format used inside the recommendation database.

Examples include:

* `High Delay` → `High`
* `Medium Issues` → `Medium`
* `High Spend` → `High`

Tenure is grouped into two business categories:

| Engineered Feature             | Database Category |
| ------------------------------ | ----------------- |
| High Tenure                    | High              |
| Very Low / Low / Medium Tenure | Non-High          |

The backend then performs a SQL lookup in the `recommendation_rules` table using all five engineered features.

### Rule Matching Strategy

Each unique combination of behavioural and profile features maps to a predefined rule (`R01`–`R22`).

If no rule matches the customer profile, the recommendation engine returns an empty recommendation response instead of failing.

### Output

A single matched recommendation rule containing:

* Rule ID.
* Behavioural profile.
* List of associated action IDs.

---

## Stage 3 — Fetch Recommendation Actions

### Purpose

Once a recommendation rule is identified, the backend retrieves the complete retention actions associated with that rule.

### Processing Logic

The matched rule stores action IDs as a comma-separated list.

Example:

```text
A05,A06,A07,A08,A09
```

The backend:

1. Splits the string into individual action IDs.
2. Queries the `recommendation_actions` table.
3. Retrieves complete metadata for every action.

Each action contains:

| Attribute        | Purpose                                         |
| ---------------- | ----------------------------------------------- |
| Action Category  | Business grouping of the recommendation.        |
| Service Category | Reactive or Proactive intervention.             |
| Cost             | Low, Medium, or High implementation cost.       |
| Recommendation   | Customer engagement action.                     |
| Authority Level  | Permission required to view the recommendation. |

### Output

A list of complete recommendation actions associated with the matched rule.

---

## Stage 4 — Role-Based Decision Logic (RBAC)

### Purpose

Not every client should receive every recommendation. The backend filters actions according to the requesting client's authority level.

### Client Types

| Client Type        | Access Level                            |
| ------------------ | --------------------------------------- |
| interaction_client | Customer-facing interface.              |
| monitoring_agent   | Internal monitoring dashboard.          |
| manager            | Manager dashboard with complete access. |

### Decision Logic

| Client Type        | Recommendation Access                                |
| ------------------ | ---------------------------------------------------- |
| interaction_client | No recommendations returned.                         |
| monitoring_agent   | Only recommendations with `authority_level = all`.   |
| manager            | All recommendations, including manager-only actions. |

If a monitoring agent encounters a manager-only recommendation, the backend sets an **escalation flag** instead of exposing the restricted action.

### Output

* Filtered recommendation list.
* Escalation indicator (`True` / `False`).

---

## Stage 5 — Recommendation Grouping and Sorting

### Purpose

The recommendation engine restructures the filtered actions into a format that is easier for the frontend to display.

### Processing Logic

Recommendations are grouped into two levels:

**Level 1 — Action Category**

Examples:

* Baseline Engagement
* Early Intervention
* Reactive Recovery
* Loyalty Reward
* VIP Engagement
* Feedback

**Level 2 — Service Category**

Each category contains:

* Reactive recommendations.
* Proactive recommendations.

### Sorting Strategy

Recommendations follow business priority instead of alphabetical order.

**Service Priority**

1. Reactive
2. Proactive

**Cost Priority**

1. Low
2. Medium
3. High

This ordering ensures that immediate interventions appear before long-term engagement strategies and lower-cost actions appear before more expensive retention campaigns.

### Output Structure

The backend returns a nested recommendation structure grouped by business category and service category.

---

## Final API Response

The recommendation engine returns a standardized JSON object.

```json
{
  "rule_id": "R13",
  "recommendations": {
    "Reactive Recovery": {
      "Reactive": [
        {
          "action_id": "A09",
          "recommendation": "Provide text and calls with human (if necessary).",
          "cost": "High"
        }
      ]
    }
  },
  "escalation_required": true
}
```

The frontend uses this response directly to render recommendation sections, cost labels, and escalation notifications.

---

## Design Decisions

| Decision                      | Rationale                                                                          |
| ----------------------------- | ---------------------------------------------------------------------------------- |
| MariaDB Rule Engine           | Keeps business rules separate from ML models and backend code.                     |
| Behaviour-Based Rule Matching | Generates deterministic recommendations for the same customer profile.             |
| SQL Parameterized Queries     | Prevents SQL injection and safely binds customer inputs.                           |
| RBAC Filtering                | Restricts high-cost or sensitive recommendations to authorized users.              |
| Category & Service Grouping   | Produces frontend-ready recommendation sections.                                   |
| Priority-Based Sorting        | Displays recommendations in business-priority order instead of alphabetical order. |

---

## Output of the Recommendation Engine

The Recommendation Engine produces:

* Matched recommendation rule.
* Filtered retention actions.
* Escalation status for restricted recommendations.
* Structured recommendation categories sorted by business priority.

This output is merged into the unified API response and displayed alongside churn prediction, business value, and SHAP explanations in the Decision Support System.


