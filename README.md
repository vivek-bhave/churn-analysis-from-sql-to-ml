## Churn Analysis: From SQL to Understanding to ML

### Problem Statement

Customer churn is not just a metric — it reflects the point where the relationship between a customer and a company begins to break.

When customers leave, the impact is not limited to lost revenue. It increases acquisition costs and weakens long-term value. Because of this, predicting churn is useful, but understanding *why it happens* is more important.

This project approaches churn as a behavioral problem rather than only a predictive task.

Instead of directly building models, the analysis begins by exploring how customer behavior changes across different conditions, identifying where noticeable shifts in churn occur.

The goal is to move step by step:
from observation → structured understanding → validated learning through machine learning.

---

### Key Findings

Out of all features analyzed, only **4** showed a strong and consistent association with churn:

| Feature | Why It Matters |
|---------|----------------|
| **Support Calls** | Churn jumps from ~29% (0-2 calls) to ~91% (5+ calls) |
| **Payment Delay** | Churn jumps from ~47% (medium delay) to ~94% (high delay) |
| **Total Spend** | Low spend customers churn at ~88%, high spend at ~41% |
| **Contract Length** | Monthly contracts churn at ~90%, annual/quarterly at ~46% |

Other features like tenure, usage frequency, last interaction, age, and gender showed weak or inconsistent patterns and were not considered important for churn prediction.

---

### Approach

1. **SQL-Based Behavioral Analysis**
   - Identify patterns in churn across different features
   - Detect thresholds where customer behavior shifts
   - Construct meaningful groupings based on churn patterns

2. **Graphical Analysis**
   - Visualize trends and validate observed patterns

3. **Statistical Analysis**
   - Check whether observed differences are consistent and meaningful

4. **Interpretable Machine Learning**
   - Use models like Logistic Regression and Decision Trees
   - Validate whether the 4 key features hold under a learning framework

---

### Dataset

The dataset includes customer-level behavioral and demographic features such as:

- Age
- Tenure
- Usage Frequency
- Support Calls
- Payment Delay
- Subscription Type
- Contract Length
- Total Spend
- Last Interaction

**Target Variable:**
- Churn (1 = customer left, 0 = customer stayed)