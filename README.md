# Customer Churn Analysis & Retention Strategy

## Project Overview

This project analyzes customer churn patterns in a telecommunications dataset of **505,206 customers** to identify behavioral drivers of churn and develop data-driven retention strategies. The analysis spans from raw data extraction to statistical validation and actionable business recommendations.

---

## 📂 Project Structure

```
CHURN-ANALYSIS-FROM-SQL-TO-ML/
│
├── Data/
│   ├── Raw/
│   │   ├── customer_churn_dataset-training-master.csv
│   │   └── customer_churn_dataset-testing-master.csv
│   │
│   └── Cleaned/
│       └── customer_churn_dataset.csv
│
├── Notebooks/
│   ├── 01_Data_cleaning.ipynb
│   ├── 02_SQL_Analysis.ipynb
│   ├── 03_Visual_analysis.ipynb
│   ├── 04_Statistical_Validation.ipynb
│   ├── 05_Logistic_Regression_analysis.ipynb
│   └── 06_Decision_tree_analysis.ipynb
│
├── Business_Recommendation.md
└── README.md
```

## Key Findings

### 1. Churn Distribution
- **55.5%** of customers churned (280,492 customers)
- **44.5%** retained (224,714 customers)
- The dataset is reasonably balanced, making it suitable for behavioral analysis

### 2. Most Important Churn Drivers

| Rank | Feature | Key Finding | Churn Rate Gap | High-Risk Customers |
|------|---------|-------------|----------------|---------------------|
| 1 | Support Calls | Churn jumps from 0.29 (0-2 calls) to 0.91 (5-10 calls) | ~62% | 183k |
| 2 | Payment Delay | Churn jumps from 0.47 (medium delay) to 0.94 (high delay) | ~47% | 111k |
| 3 | Total Spend | Churn drops sharply from 0.88 (low spend) to 0.41 (high spend) | ~47% | 151k |
| 4 | Contract Length | Monthly contracts have 0.90 churn vs 0.46 for annual/quarterly | ~44% | 109k |

### 3. Statistical Validation (Cramér's V)

| Feature | Cramér's V | Interpretation |
|---------|------------|----------------|
| Issue Level | 0.549 | Strong association with churn |
| Spend Level | 0.432 | Strong association with churn |
| Delay Level | 0.416 | Strong association with churn |
| Contract Length | 0.367 | Moderate-strong association with churn |

All features showed statistically significant association with churn (p < 0.001), confirming the univariate findings.

### 4. Logistic Regression Model Performance

| Metric | Score |
|--------|-------|
| Accuracy | 88.5% |
| Precision | 88.8% |
| Recall | 90.8% |
| F1 Score | 89.8% |

### 5. Odds Ratios (Logistic Regression)

| Feature | Odds Ratio | Interpretation |
|---------|------------|----------------|
| Low Spend | 7.72× | 7.7× higher churn than high spend customers |
| Monthly Contract | 7.31× | 7.3× higher churn than annual/quarterly customers |
| Medium Issues | 0.108× | Lower churn (relative to high issues baseline) |
| Medium Delay | 0.079× | Lower churn (relative to high delay baseline) |
| Low Delay | 0.063× | Lower churn |
| Low Issues | 0.058× | Lower churn |

### 6. High-Risk Customer Segments (Churn Rate > 80%)

| Issue Level | Delay Level | Spend Level | Contract Length | Churn Rate | Customer Count |
|-------------|-------------|-------------|-----------------|------------|----------------|
| High Issues | High Delay | High Spend | Monthly | 98.0% | 11,713 |
| High Issues | High Delay | Low Spend | Monthly | 97.7% | 9,627 |
| High Issues | High Delay | Low Spend | Quarterly | 97.6% | 9,790 |
| High Issues | High Delay | Low Spend | Annual | 97.3% | 9,778 |
| High Issues | High Delay | High Spend | Quarterly | 95.6% | 11,254 |
| High Issues | Medium Delay | High Spend | Monthly | 95.6% | 5,694 |
| High Issues | High Delay | High Spend | Annual | 95.3% | 11,338 |
| High Issues | Medium Delay | Low Spend | Monthly | 95.3% | 4,598 |

### 7. Decision Tree Rules for High Churn

| Business Rule | Samples | Churn Rate |
|---------------|---------|------------|
| High Issues AND Monthly Contract | 17,145 | 97.89% |
| High Issues | 33,721 | 96.42% |
| High Issues AND Medium Delay AND Monthly Contract | 8,271 | 95.54% |
| High Issues AND Medium Delay | 16,857 | 93.82% |
| High Spend AND Monthly Contract AND High Delay | 7,335 | 93.69% |
| Low Spend AND High Delay AND Medium Issues | 7,273 | 93.68% |
| Low Spend AND High Delay | 10,728 | 92.93% |
| High Issues AND Low Delay AND Low Spend AND Annual Contract | 10,739 | 86.51% |
| High Issues AND Low Delay AND Low Spend | 21,107 | 86.20% |
| High Issues AND Low Delay AND High Spend AND Monthly Contract | 12,743 | 85.94% |
| High Spend AND Monthly Contract | 13,861 | 85.59% |
| High Spend AND High Delay | 13,073 | 85.38% |
| Low Spend AND Monthly Contract | 11,527 | 85.05% |
| High Issues AND Low Delay AND High Spend | 26,161 | 83.47% |

### 8. Bivariate Interaction Analysis

#### Support Calls × Total Spend

| Issue Level | Spend Level | Churn Rate |
|-------------|-------------|------------|
| High Issues | Low Spend | 91.75% |
| High Issues | High Spend | 90.00% |
| Medium Issues | Low Spend | 86.20% |
| Low Issues | Low Spend | 82.98% |

#### Payment Delay × Total Spend

| Delay Level | Spend Level | Churn Rate |
|-------------|-------------|------------|
| High Delay | Low Spend | 95.68% |
| High Delay | High Spend | 92.93% |
| Medium Delay | Low Spend | 88.38% |
| Low Delay | Low Spend | 83.27% |

#### Contract Length × Support Calls

| Contract Length | Issue Level | Churn Rate |
|----------------|-------------|------------|
| Monthly | High Issues | 91.85% |
| Annual | High Issues | 90.30% |
| Quarterly | High Issues | 90.23% |
| Monthly | Medium Issues | 88.45% |
| Monthly | Low Issues | 87.92% |

#### Contract Length × Payment Delay

| Contract Length | Delay Level | Churn Rate |
|----------------|-------------|------------|
| Monthly | High Delay | 95.96% |
| Quarterly | High Delay | 93.43% |
| Annual | High Delay | 93.16% |
| Monthly | Medium Delay | 91.40% |
| Monthly | Low Delay | 85.68% |

---

## Business Recommendations

### 1. Retention Strategy for Low-Value Profile Customers (Low Spend)

#### High-Risk Segment 1

**Customer Profile:**
- Low Spend
- Any Contract Length
- High Issues
- High Payment Delay

**Recommended Actions:**
- **Prevent High Issues:** Resolve customer queries before customers reach the High Issues threshold (≤ 4 support calls)
- **Prevent High Payment Delay:** Initiate automated payment reminders before customers reach the High Payment Delay threshold

**Retention Strategy:**
- Focus on low-cost and scalable interventions:
  - Automated email reminders
  - SMS notifications
  - Chatbot assistance
  - Self-service support portals

#### High-Risk Segment 2

**Customer Profile:**
- Low Spend
- Monthly Contract
- Low Issues
- Medium/High Payment Delay

**Recommended Actions:**
- **Increase Customer Commitment:** Offer targeted renewal incentives before renewal date
  - Discounted Annual or Quarterly plans
  - Loyalty rewards
  - Discount vouchers
- **Prevent High Payment Delay:** Automated payment reminders and flexible payment assistance

**Retention Strategy:**
- Proactive engagement through commitment-building initiatives

---

### 2. Retention Strategy for High-Value Profile Customers (High Spend)

#### High-Risk Customer Profiles

**Segment 1:** High Spend, High Issues, High Payment Delay
**Segment 2:** High Spend, Monthly Contract

**Recommended Actions:**

**Priority 1 – Prevent High Issues:**
- Priority customer support
- Dedicated service representatives
- Faster issue resolution

**Priority 2 – Prevent High Payment Delay:**
- Personalized payment reminders
- Account management support
- Flexible payment assistance

**Priority 3 – Increase Long-Term Customer Commitment:**
- Discounted annual or quarterly plans
- Loyalty rewards
- Bonus subscription months
- Personalized renewal offers
- Exclusive premium benefits

**Priority 4 – Protect High-Value Customers:**
- Premium loyalty programs
- Exclusive offers
- Personalized product recommendations
- Early access to new products or services
- Dedicated customer support
- VIP membership programs

---

## Technical Implementation

### Technologies Used

- **Database:** MySQL
- **Data Extraction:** SQL, SQLAlchemy, PyMySQL
- **Data Processing:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Statistical Analysis:** SciPy (Chi-Square, Cramér's V)
- **Machine Learning:** Scikit-learn (Logistic Regression, Decision Tree)
- **Environment:** Jupyter Notebooks

### Key Code Snippets

#### SQL Analysis (Support Calls Churn Rate)

```sql
SELECT 
    Support_Calls,
    AVG(CASE WHEN Churn = 1 THEN 1 ELSE 0 END) AS churn_rate
FROM churn
GROUP BY Support_Calls
ORDER BY Support_Calls;
```

#### Chi-Square Test Implementation

```python
from scipy.stats import chi2_contingency

def cramers_v(table):
    chi2 = chi2_contingency(table)[0]
    n = table.sum().sum()
    r, k = table.shape
    return np.sqrt(chi2 / (n * min(r - 1, k - 1)))
```

#### Logistic Regression

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train, y_train)

# Odds Ratios
odds_ratios = np.exp(model.coef_[0])
```

#### Decision Tree for Rule Extraction

```python
from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier(random_state=42, max_depth=4)
dt.fit(X_train, y_train)

# Extract rules
from sklearn.tree import export_text
rules = export_text(dt, feature_names=list(X_train.columns))
```

---

## Key Insights Summary

1. **High Issues is the strongest churn predictor** – Customers with 5+ support calls churn at 90%+ rates
2. **Monthly contracts double churn rates** – Monthly customers churn 7.3× more than annual/quarterly customers
3. **High payment delay is critical** – Churn jumps from 48% to 94% after 20 days of delay
4. **Low spend customers are fragile** – Churn increases from 41% to 88% for low spend customers
5. **Combinations matter** – Multiple risk factors amplify churn probability exponentially
6. **High-value customers also churn** – Even high spend customers churn at significant rates when issues arise
7. **Segmented strategies are essential** – Low-value customers need scalable, automated interventions; high-value customers justify personalized engagement

---

## Conclusion

This analysis identified four key behavioral drivers of churn: **Support Calls, Payment Delay, Total Spend, and Contract Length**. These features show large, consistent gaps in churn rates across meaningful customer segments. Features like tenure, usage frequency, last interaction, subscription type, age, and gender have weak or inconsistent associations with churn and are less useful for predicting customer departure.

The bivariate and multivariate analyses confirmed that churn is driven by the combined effect of customer issues, payment behavior, spending patterns, and contract type. Customers experiencing high issue levels and significant payment delays represent the highest-risk segment and should be prioritized for retention strategies.

The business recommendations are segmented by customer value, ensuring that retention investments are proportional to customer lifetime value. Low-value customers benefit from scalable, automated interventions, while high-value customers justify personalized engagement and premium retention programs.