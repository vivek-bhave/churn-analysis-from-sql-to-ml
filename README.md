## Churn Analysis: From SQL to Understanding to ML

### Problem Statement

Customer churn is not just a metric — it reflects the point where the relationship between a customer and a company begins to break.

When customers leave, the impact is not limited to lost revenue. It increases acquisition costs and weakens long-term value.
Because of this, predicting churn is useful, but understanding *why it happens* is more important.

This project approaches churn as a behavioral problem rather than only a predictive task.

Instead of directly building models, the analysis begins by exploring how customer behavior changes across different conditions, identifying where noticeable shifts in churn occur.

The goal is to move step by step:
from observation → to structured understanding → to validated learning through machine learning.

---

### Approach

1. **SQL-Based Behavioral Analysis**

   * Identifying patterns in churn across different features
   * Detecting thresholds where customer behavior shifts
   * Constructing meaningful groupings based on churn patterns

   Key features identified:

   * Support Calls
   * Payment Delay
   * Total Spend
   * Contract Length
   * Last Interaction
   * Gender

2. **Graphical Analysis**

   * Visualizing trends and validating observed patterns

3. **Statistical Analysis**

   * Checking whether observed differences are consistent and meaningful

4. **Interpretable Machine Learning**

   * Using models like Logistic Regression and Decision Trees
   * Understanding feature importance and decision boundaries
   * Validating whether earlier insights hold under a learning framework

---

### Dataset

The dataset includes customer-level behavioral and demographic features such as:

* Age
* Tenure
* Usage Frequency
* Support Calls
* Payment Delay
* Subscription Type
* Contract Length
* Total Spend
* Last Interaction

**Target Variable:**

* Churn (1 = customer left, 0 = customer stayed)
