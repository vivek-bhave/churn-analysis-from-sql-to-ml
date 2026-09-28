# Churn Database Logic

The customer is described by many features. Some features describe the **customer profile**, while other features describe **customer behaviour**. The goal here is to choose the features that build the customer's profile and the features that best describe how the customer behaves.

We focus more on the behavioural features that have a high association with customer churn because those customers deserve the correct recommendations. Otherwise, we can lose them quickly, as they are usually at higher risk of churning.

## Customer Behaviour and Profile Features

The features that describe a customer are divided into **customer profile features** and **customer behaviour features**.

### Customer Profile Features

These features describe the customer's value and long-term relationship with the platform.

- **Spend Level** — Customer spending category.
- **Contract Length** — Customer subscription commitment.
- **Tenure Level** — Strength and duration of the customer's relationship with the platform.

These features determine **how costly a retention recommendation** a customer should receive.

**Example:** A customer with **High Spend**, **Annual Contract Length**, and **High Tenure Level** may receive higher-cost retention recommendations because the customer has higher business value.

---

### Customer Behaviour Features

These features describe how the customer interacts with the platform and their recent behavioural patterns.

- **Issue Level** — Customer complaint frequency.
- **Delay Level** — Payment delay behaviour.

These features determine **whether the customer requires proactive or reactive service**.

**Example:** A customer with **High Issue Level** and **High Delay Level** may receive **Reactive** service recommendations because the customer is showing stronger churn-risk behaviour.

The behavioural features were selected through customer behaviour analysis using SQL to identify the customer characteristics most strongly associated with churn.



**📓 Customer Behaviour Analysis:** `Notebooks/02_Customer_behavior_analysis.ipynb`

> **📝 Note:** The complete recommendation database, including all **22 recommendation rules (R01–R22)** and **18 recommendation actions (A01–A18)**, is provided separately in the Excel file. If you want to explore every rule, action mapping, service category, cost level, and authority level in detail, refer to **`Recommendation_Rules_Database.xlsx`**.



