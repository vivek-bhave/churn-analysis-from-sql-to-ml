## Model Performance Comparison
#### Business Value Definition

> For this analysis, customer business value is approximated using multiple customer characteristics. High business-value customers are those with **High Spend, Annual/Quarterly Contract Length, Premium/Standard Subscription Type, Medium/High Tenure, High Usage Frequency, and Low Last Interaction**. Conversely, low business-value customers are characterized by **Low Spend, Monthly Contract Length, Basic Subscription Type, Low/Very Low Tenure, Low Usage Frequency, and High Last Interaction**.

**Objective:** To identify the model that minimizes the misclassification of high-business value churn customers while reducing unnecessary retention campaigns for low business customer segments.

### Model Performance Metrics

| Model | Features Used | Accuracy | Precision | Recall | F1-Score | ROC-AUC | False Positives (FP) | False Negatives (FN) |
|:------|:--------------|---------:|----------:|-------:|---------:|--------:|---------------------:|---------------------:|
| Logistic Regression | 4 | **88.52%** | 88.76% | 90.81% | 89.78% | 91.96% | 6,449 | 5,155 |
| Decision Tree | 4 | **89.67%** | 88.67% | 93.33% | 90.94% | 92.32% | 6,692 | 3,742 |
| Random Forest | 4 | **89.67%** | 88.67% | 93.33% | 90.94% | 92.34% | 6,692 | 3,742 |
| XGBoost | 4 | **89.67%** | 88.67% | 93.33% | 90.94% | 92.34% | 6,692 | 3,742 |
| Random Forest | All Features | **91.56%** | 88.58% | 97.35% | 92.76% | 94.29% | 7,039 | 1,484 |
| XGBoost | All Features | **91.59%** | 88.58% | 97.42% | 92.79% | 94.42% | 7,049 | **1,448** |

#### Performance Interpretation

- **Accuracy:** Overall percentage of correctly classified customers.
- **Precision:** Percentage of predicted churn customers who actually churned.
- **Recall:** Percentage of actual churn customers correctly identified by the model.
- **F1-Score:** Harmonic mean of Precision and Recall, providing a balanced evaluation.
- **ROC-AUC:** Measures the model's ability to distinguish churn and non-churn customers across all classification thresholds.
- **False Positives (FP):** Customers predicted to churn but who actually stayed, potentially increasing unnecessary retention costs.
- **False Negatives (FN):** Customers predicted not to churn but who actually churned, representing missed retention opportunities and potential revenue loss.


## Model Comparison

### 1. Logistic Regression (4 Features)

- Achieved **0.9% higher Precision** than the tree-based models, resulting in fewer false positives.
- Compared to the tree-based models, Logistic Regression misclassified fewer **Monthly Contract (12.28%)**, **Low Payment Delay (0.33%)**, **Low Issue Level (0.81%)**, and **High Spend (0.58%)** non-churning customers.
- Captures linear relationships between the engineered features and customer churn, making the model simple and highly interpretable.
- Cannot effectively capture complex non-linear interactions between customer characteristics.
- Misses the lowest false postives compared all other models.

### Tree-Based Models (4 Features)

- Achieved **0.15% higher Accuracy**, **2.52% higher Recall**, and **0.37% higher ROC-AUC** than Logistic Regression.
- Successfully captured complex non-linear relationships between customer characteristics.
- Reduced false negatives across key customer segments compared to Logistic Regression, including **Monthly Contract (7.20%)**, **Low Payment Delay (5.47%)**, **Low Issue Level (10.42%)**, and **High Spend customers (4.82%)**, improving identification of valuable churn customers.
- Decision Tree, Random Forest, and XGBoost produced nearly identical performance because the engineered features already captured most of the dominant churn patterns.

### 2. Decision Tree

- Learns non-linear decision boundaries but uses a fully grown tree (`min_samples_split=2`, `min_samples_leaf=1`), making it more prone to overfitting.

### 3. Random Forest

- Reduces model variance by averaging predictions from multiple decision trees, producing more robust and stable predictions while maintaining similar performance.

### 4. XGBoost

- Improves generalization through sequential boosting, correcting errors made by previous trees and reducing model bias while maintaining comparable performance.

### Tree-Based Models (All Features)

### Random Forest
- Achieved **2.89% higher Accuracy**, **5.01% higher Recall**, and **1.95% higher ROC-AUC** than 4 Featured Tree based models.
- Captured higher churning customers than all 4 featured models 
- Has lower False Negatives compared to all 4 featured models 


### XGBoost
- Achieved **0.3% higher Accuracy**, **0.07% higher Recall**, and **0.13% higher ROC-AUC** than All Featured Random forest.
-  Loses highest non-churning customers 

## Model Selection 
- The choice of the model depends on the type of the problem.
-  The problems can be missing the churning customers, missing the non-churning customers in prediction or both

### Missing Churning Customers in prediction
**Problem Statement**:The high business value customers contribute the long-term revenue and healthy relationship with platform.Losing them can to lead higher business loss.

- Missing high business value customers is usually much more costlier than missing non-churning customers.
- XGBoost lost lowest level of churning customers
#### Business Comparison (Random Forest vs XGBoost)

- Both Random Forest and XGBoost identified high business-value customer segments equally well.
- Both models produced identical false-negative rates for:
  - High Spend customers (4.88%)
  - Annual Contract customers (4.08%)
  - Quarterly Contract customers (3.85%)
  - Premium Subscription customers (2.82%)
  - Standard Subscription customers (2.48%)
  - High Tenure customers (2.73%)
  - Medium Tenure customers (2.17%)
  - High Usage Frequency customers (2.82%)
  - Low Last Interaction customers (3.53%)

- Therefore, neither model demonstrates an advantage in retaining high business-value customers based on segment-level false-negative analysis.

- Since both models exhibit identical business performance, XGBoost was preferred because it achieved a slightly higher ROC-AUC score, indicating marginally better ranking ability and generalization.



### Missing Non-Churning customers in prediction
**Problem Statement**:When the low business value customers are missclassifed then applying the retetion stratergies on them may not foster strong relationship compared to high business value customers.
- The logistic regression lost the lowest non-churning customers
- It has highest precision
- Compared to the tree-based models, Logistic Regression misclassified fewer **Monthly Contract (12.28%)**, **Low Payment Delay (0.33%)**, **Low Issue Level (0.81%)**, and **High Spend (0.58%)** non-churning customers.
- So, We choose logistic regression for this problem.



