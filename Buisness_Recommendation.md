# Business Recommendations

The customer churn analysis identified two distinct customer profiles based on **Spending Level**, each requiring a different retention strategy. While the primary churn drivers (High Issues, High Payment Delay, and Monthly Contract) are common across customer groups, the recommended business interventions differ according to customer lifetime value and expected return on investment.

---

# 1. Retention Strategy for Low-Value Profile Customers (Low Spend)

## High-Risk Segment 1

### Customer Profile

* Low Spend
* Any Contract Length
* High Issues
* High Payment Delay

### Recommended Actions

#### Priority 1 – Prevent High Issues

Resolve customer queries **before customers reach the High Issues threshold (≤ 4 support calls)** to prevent escalation into the highest-risk category.

#### Priority 2 – Prevent High Payment Delay

Initiate automated payment reminders or payment assistance **before customers reach the High Payment Delay threshold (≥ 508 payment delay)**.

### Retention Strategy

Since these customers contribute relatively lower customer lifetime value, retention efforts should focus on **low-cost and scalable interventions**, including:

* Automated email reminders
* SMS notifications
* Chatbot assistance
* Self-service support portals

These strategies reduce retention costs while addressing the primary factors associated with churn.

### Supporting Evidence

* **Threshold Analysis (SQL):** Data-driven thresholds were identified for Support Calls (≤ 4) and Payment Delay (≥ 508), providing operational trigger points for early intervention.
* **Logistic Regression:** Low Spend, High Issues, and High Payment Delay were identified as statistically significant contributors to churn.
* **Segment Analysis:** Low Spend customers experiencing High Issues and High Payment Delay formed one of the highest-risk churn segments.
* **Statistical Validation:** Chi-Square Test and Cramer's V confirmed statistically significant associations between Spending Level, Issue Level, Payment Delay, and churn.

---

## High-Risk Segment 2

### Customer Profile

* Low Spend
* Monthly Contract
* Low Issues
* Medium/High Payment Delay

### Recommended Actions

#### Priority 1 – Increase Customer Commitment

Offer targeted renewal incentives before the monthly contract renewal date, including:

* Discounted Annual or Quarterly plans
* Loyalty rewards
* Discount vouchers
* Personalized renewal offers

These incentives encourage higher spending while increasing long-term customer commitment.

#### Priority 2 – Prevent High Payment Delay

Initiate automated payment reminders or flexible payment assistance **before customers reach the High Payment Delay threshold (≥ 508 payment delay).**

### Retention Strategy

These customers have not yet accumulated severe service issues. Therefore, proactive engagement through commitment-building initiatives is likely to be more cost-effective than reactive retention after customers become high-risk.

### Supporting Evidence

* **Logistic Regression:** Monthly Contract, Low Spend, and High Payment Delay were significant predictors of churn.
* **Segment Analysis:** Monthly Low Spend customers with Medium/High Payment Delay exhibited elevated churn risk.
* **Threshold Analysis (SQL):** High Payment Delay provides an operational trigger for proactive intervention.
* **Statistical Validation:** Chi-Square Test and Cramer's V confirmed statistically significant associations between Contract Length, Spending Level, Payment Delay, and churn.

---

# 2. Retention Strategy for High-Value Profile Customers (High Spend)

Unlike low-value customers, high-value customers generate substantially greater customer lifetime value. Therefore, investing in personalized and proactive retention strategies is economically justified.

## High-Risk Customer Profiles

### Segment 1

* High Spend
* High Issues
* High Payment Delay

### Segment 2

* High Spend
* Monthly Contract
* Particularly customers approaching the High Issues or High Payment Delay thresholds

### Recommended Actions

#### Priority 1 – Prevent High Issues

Resolve customer queries **before customers reach the High Issues threshold (≤ 4 support calls)** through:

* Priority customer support
* Dedicated service representatives
* Faster issue resolution

#### Priority 2 – Prevent High Payment Delay

Initiate personalized payment reminders, account management support, or flexible payment assistance **before customers reach the High Payment Delay threshold (≥ 508 payment delay).**

#### Priority 3 – Increase Long-Term Customer Commitment

For High Spend customers on Monthly Contracts, encourage migration to Quarterly or Annual subscriptions by offering:

* Discounted annual or quarterly plans
* Loyalty rewards
* Bonus subscription months
* Personalized renewal offers
* Exclusive premium benefits

#### Priority 4 – Protect High-Value Customers

Strengthen long-term customer relationships through:

* Premium loyalty programs
* Exclusive offers
* Personalized product recommendations
* Early access to new products or services
* Dedicated customer support
* VIP membership programs

The objective is to protect customer lifetime value rather than relying primarily on price discounts.

### Supporting Evidence

* **Threshold Analysis (SQL):** Support Call (≤ 4) and Payment Delay (≥ 508) thresholds provide operational trigger points for proactive retention.
* **Logistic Regression:** High Issues, High Payment Delay, and Monthly Contract remained statistically significant predictors of churn.
* **Segment Analysis:** High Spend customers with High Issues and High Payment Delay formed one of the highest-risk churn segments. Additionally, High Spend customers on Monthly Contracts exhibited elevated churn rates, demonstrating that high spending alone does not guarantee long-term customer commitment.
* **Statistical Validation:** Chi-Square Test and Cramer's V confirmed statistically significant associations between Spending Level, Contract Length, Issue Level, Payment Delay, and churn.

---

# Overall Business Strategy

The analysis suggests that customer retention should be **segmented by customer value rather than applying a single strategy to all customers.**

* **Low-Value Customers:** Focus on scalable, low-cost automated interventions and commitment-building incentives before customers enter high-risk behavioral thresholds.
* **High-Value Customers:** Prioritize proactive issue resolution, personalized customer engagement, premium retention programs, and conversion from monthly to long-term subscription plans to maximize customer lifetime value.

By integrating threshold-based early warning systems, statistical validation, customer segmentation, and predictive modeling insights, organizations can implement targeted retention campaigns that optimize both customer satisfaction and business profitability.
