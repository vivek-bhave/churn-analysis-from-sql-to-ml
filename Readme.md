# Real-Time Customer Engagement Decision Support System

An AI-powered Decision Support System (DSS) that assists support staff and autonomous AI agents in making real-time customer engagement decisions. The system predicts customer churn risk, explains the reasons behind each prediction using explainable AI, and recommends personalized engagement strategies to improve customer experience and retention during live interactions.

## Problem Statement

Customer engagement decisions are made across both human-operated support systems and automated customer engagement workflows. During live customer interactions, these systems need timely customer intelligence to understand behavior, identify churn risk, and determine the most appropriate engagement strategy before the interaction ends.

Support staff require decision support while interacting with customers, whereas AI agents and automation workflows require a reliable API that can provide the same intelligence programmatically for real-time customer engagement tasks such as proactive outreach, prioritization, or personalized responses.

Offline or batch-oriented analytics generate insights after data processing is complete, making them unsuitable for scenarios where engagement decisions must be made immediately. Live customer engagement instead requires a real-time Decision Support System capable of returning predictions, explanations, and engagement recommendations on demand.

## Users and User Requirement

The Real-Time Customer Engagement Decision Support System is consumed by three different clients, each with a different responsibility in the customer engagement workflow.

### 1. Customer Interaction Client

**Who:** Human CRM agents, chatbots, voice bots, email responders, or any client responsible for engaging with customers through calls, chat, email, social media, or support tickets.

**Job:** Provide customer support by using customer intelligence from the Decision Support System before interacting with a customer.

**Requirements:**

1. The client needs to know the customer's churn risk and the reasons behind that risk before starting an interaction so they can choose the most appropriate approach for the conversation.

2. The client needs a quick response from the system because customer interactions often begin immediately, such as answering an incoming phone call or responding to a new support request.

3. The client needs the system to remain available even when many customers contact support simultaneously, so multiple customer requests can be handled without delays.

### 2. Customer Monitoring AI Agent

**Who:** A background AI agent.

**Job:** Continuously monitor customer events and behaviour independently of customer interactions, identify customers who require proactive engagement, and automate retention actions whenever appropriate.

**Requirements:**

1. The AI agent needs to continuously monitor customer events and evaluate every customer without waiting for a customer interaction to begin.

2. The AI agent needs to identify customers who are at risk of churn and understand the reasons behind that prediction before taking any action.

3. The AI agent needs to automatically execute low-cost and medium-cost engagement recommendations before a customer's churn risk increases, enabling proactive customer engagement.

4. The AI agent needs to escalate customers requiring high-cost retention actions to a Retention Manager instead of executing those actions itself.

5. The AI agent needs the system to remain available across all services because it monitors every customer continuously, and customer events may arrive in bursts.

6. The AI agent needs a fast response from the system so that engagement recommendations can be automated before a customer's churn risk increases.

---

### 3. Senior Retention Manager

**Who:** Senior CRM users responsible for retention decisions and high-value customer engagement.

**Job:** Review escalated customers and approve expensive retention actions.

**Requirements:**

1. The manager needs to review customers who have been escalated by the Customer Monitoring AI Agent.

2. The manager needs to understand the customer's churn risk and the reasons behind that prediction before approving any retention action.

3. The manager needs complete customer context, including relevant customer history and behaviour, to make informed retention decisions.

4. The manager needs access to all engagement recommendations, including low-, medium-, and high-cost actions, because they are responsible for approving expensive retention strategies.

5. The manager needs the system to respond quickly so escalated customers can be reviewed and retention decisions can be made without unnecessary delays.

6. The manager needs the system to remain available even during periods of high customer volume, ensuring escalated cases can always be reviewed.

## System Requirements

The system requirements are derived from the requirements of the Customer Interaction Client, Customer Monitoring AI Agent, and Senior Retention Manager. They define the capabilities and quality attributes that the Decision Support System must provide to support real-time customer engagement workflows.

### Functional Requirements

1. The system must predict customer churn risk for any customer whenever requested by a client.

2. The system must generate explainable reasons for every churn prediction so that clients understand why the customer is considered at risk.

3. The system must identify whether a customer is a High Business Value customer or a Low Business Value customer and provide that information to support customer engagement and retention decisions.

4. The system must generate engagement recommendations categorized into Low-, Medium-, and High-cost actions.

5. The system must enforce role-based decision actions, ensuring each client receives only the information and recommendations appropriate for its responsibility.

6. The system must support escalation of customers from the Customer Monitoring AI Agent to the Senior Retention Manager whenever a High-cost retention action is required.

### Non-Functional Requirements

1. The system must provide low response time so customer support clients and AI agents receive customer intelligence before engagement decisions are made.

2. The system must maintain high availability so it remains operational during peak customer traffic and bursts of customer events.

3. The system must support concurrent requests from multiple CRM clients and AI agents without degrading performance.

4. The system must be scalable to handle increasing numbers of customers, interactions, and monitoring events.

5. The system must be reliable so predictions, explanations, and recommendations are consistently available across customer engagement workflows.

6. The system must provide secure, role-based access to decision intelligence and decision actions for different clients.



## High-Level Design

The High-Level Design (HLD) describes the overall structure of the **Real-Time Customer Engagement Decision Support System (DSS)**. It defines the system boundary, external environment, system inputs and outputs, and the flow of information between external clients and the DSS before discussing the internal implementation.

---

### 1. System Boundary

The **Real-Time Customer Engagement Decision Support System (DSS)** is the central decision intelligence platform responsible for processing customer information and generating customer engagement intelligence and decision actions.

The system boundary separates the internal Decision Support System from all external entities that interact with it. Any client sending data to the DSS or consuming outputs from the DSS is considered part of the external environment.

---

### 2. External Environment

The external environment consists of all entities that interact with the Decision Support System but are not part of its internal implementation.

| External Entity | Role |
|-----------------|------|
| **Customer Interaction Client** | Uses customer intelligence before interacting with customers through calls, chat, email, social media, or support tickets. |
| **Customer Monitoring AI Agent** | Continuously monitors customer behaviour and automates proactive customer engagement. |
| **Senior Retention Manager** | Reviews escalated customers and approves high-cost retention actions. |

---
## Live System Demonstration

The deployed application can be accessed here:

**[Open Churn DSS Application](http://15.206.146.200:8501/)**

The following screenshots demonstrate the key capabilities of the system.

### 3. System Inputs


#### 1. Client Inputs
The Decision Support System receives different types of inputs depending on the client interacting with it.

| Source | Input to DSS |
|--------|--------------|
| **Customer Interaction Client** | Customer ID / Customer Query |
| **Customer Monitoring AI Agent** | Customer Events |
| **Senior Retention Manager** | Approval / Review Request |

![Client type](Images/client_type.jpeg)

#### 2. Customer Input

The customer profile used for churn analysis is entered into the system.

![Customer Input](Images/customer_input.png)

---

### 4. System Outputs

The Decision Support System returns role-specific decision intelligence and decision actions to different clients.

| Destination | Output from DSS |
|-------------|-----------------|
| **Customer Interaction Client** | Business value,Churn Risk Prediction and SHAP Values |
| **Customer Monitoring AI Agent** | Business value,Churn Risk Prediction, SHAP Values, Low-Cost Recommendations, and Medium-Cost Recommendations |
| **Senior Retention Manager** | Business value,Churn Risk Prediction, SHAP Values, and All Recommendations (Low, Medium, and High Cost) |

#### 1. Business Value

The system categorizes customers into three business value levels: **Low, Medium, and High**. This classification helps determine the appropriate level of customer engagement and associated intervention cost.

**Low Business Value**

Customers classified as having low business value are assigned **low-cost engagement strategies**, allowing the system to recommend interventions that are appropriate for their business value.

![Low Business Value](Images/low_business_value.png)

**Medium Business Value**

Customers classified as having medium business value are assigned **medium-cost engagement strategies**, enabling the system to recommend interventions appropriate to their business value.

![Medium Business Value](Images/medium_business_value.png)

**High Business Value**

Customers classified as having high business value are assigned **high-cost engagement strategies**, allowing the system to recommend higher-value interventions when appropriate.

![High Business Value](Images/high_business_value.png)

#### 2. Churn Risk

The **churn risk** indicates the likelihood of a customer leaving the service. This assessment helps determine whether the customer requires **proactive or reactive engagement strategies** based on the level of churn risk.

The choice of model can also serve as an important input for the **AI Monitoring Agent**, enabling it to identify customers requiring attention and support appropriate engagement decisions.

![Churn Risk](Images/churn_risk.png)

#### 3. Relative Percentage of SHAP Values

The **relative percentage of SHAP values** shows the contribution of each customer feature to the predicted churn risk.

It indicates the relative extent to which each feature contributed toward the customer's churn prediction, providing an interpretable explanation of the model's decision.

![Relative Percentage of SHAP Values](Images/Relative_percentage_shap_values.png)

#### 4. Recommendations

**Recommendation for Customer Interaction Client**

The **Customer Interaction Client** does not receive recommendations. The recommendations generated by the system primarily focus on customer engagement strategies and interventions, which are intended to support broader retention and engagement decisions rather than the direct customer interaction process.

![Recommendation for Customer Interaction Client](Images/Recommondation%20for%20Customer%20Interaction%20Client.png)

**Recommendation for Customer Monitoring AI Agent**

The **Customer Monitoring AI Agent** has access to **low- and medium-cost recommendations**. High-cost recommendations are not directly available to the AI agent in order to maintain appropriate human oversight and avoid fully automated execution of high-impact interventions.

High-cost recommendations are instead **escalated to the Senior Retention Manager** for review and decision-making.

![Recommendation for Customer Monitoring AI Agent](Images/Recommondation%20for%20Customer%20Monitoring%20AI%20Agent.png)

**Recommendation for Senior Retention Manager**

The **Senior Retention Manager** has access to the complete set of recommendations, including **high-cost recommendations escalated by the Customer Monitoring AI Agent**.

The Senior Retention Manager reviews these escalated recommendations and makes the final decision regarding whether the proposed high-cost intervention should be applied.

![Recommendation for Senior Retention Manager](Images/Recommendation%20for%20Senior%20Retention%20Manager.jpeg)

#### 5. Availability of Services

The system provides a **service availability status** for the core services required by the decision-support system, including the **Prediction Service, SHAP Service, and Recommendation Service**.

Each service is represented by a status indicator:

- **Green** — The service is available and operational.
- **Red** — The service is unavailable or not operational.

This provides a quick indication of the operational status of the system's core services.

![Availability of Services](Images/Availibility%20of%20services.png)


---

### 5. Data Flow Diagram — Level 0 (Context Diagram)

The Level 0 Data Flow Diagram represents the Decision Support System as a single logical process. It shows the information exchanged between the DSS and the external entities without exposing the internal processing logic.

![DFD Level 0](Images/DFD_Level_0_RTCEDSS.png)

*Figure 1. Data Flow Diagram (Level 0): Context Diagram of the Real-Time Customer Engagement Decision Support System.*

---

### 6. Context Diagram Description

The **Customer Interaction Client** sends a customer identifier or customer query to the DSS and receives the customer's churn risk prediction and SHAP explanation before customer engagement.

The **Customer Monitoring AI Agent** continuously sends customer events to the DSS. In return, it receives churn predictions, SHAP explanations, and low- and medium-cost engagement recommendations to automate proactive customer engagement.

The **Senior Retention Manager** receives complete customer intelligence along with all engagement recommendations for escalated customers. The manager reviews the recommendations and sends approval or review decisions for high-cost retention actions back to the DSS.



### 2. Data Flow Diagram — Level 1 (Business Data Flow)

The Level 1 Data Flow Diagram decomposes the **Real-Time Customer Engagement Decision Support System (DSS)** into its three major business services. It illustrates how a customer request is processed inside the DSS to generate churn predictions, explainable reasoning, engagement recommendations, and role-specific decision outputs.

#### DFD Level 1

![DFD Level 1](Images/DFD_Level_1_RTCEDSS.png)

*Figure 2. Data Flow Diagram (Level 1): Business data flow inside the Real-Time Customer Engagement Decision Support System.*

---

#### Internal Processes

| Process | Responsibility |
|---------|----------------|
| **P1. Churn Risk & Reasoning Service** | Predicts customer churn risk and generates SHAP-based explanations for the prediction. |
| **P2. Recommendation Service** | Generates customer engagement recommendations using customer profile information from the recommendation database. |
| **P3. Role-Based Decision Service** | Filters recommendations based on the requesting client and returns role-specific decision actions. |

---

#### Data Store

| Data Store | Description |
|------------|-------------|
| **D1. Recommendation Database** | Stores customer profile information and generated engagement recommendations used by the Recommendation Service. |

---

#### Level 1 Data Flow Description

The three external clients send customer information to the Decision Support System through a common **Customer Input** flow. Inside the DSS, the customer input is distributed to the **Churn Risk & Reasoning Service** and the **Recommendation Service**.

The **Churn Risk & Reasoning Service** independently processes customer input and returns **Churn Risk Prediction** and **SHAP Values**.

The **Recommendation Service** retrieves the required **Customer Profile** from the **Recommendation Database** and generates customer engagement recommendations. The generated recommendations are passed to the **Role-Based Decision Service**, which filters recommendation levels according to the client's role.

The final outputs returned by the DSS are:

- **Customer Interaction Client:** Churn Risk Prediction and SHAP Values.
- **Customer Monitoring AI Agent:** Churn Risk Prediction, SHAP Values, Low-Cost Recommendations, and Medium-Cost Recommendations.
- **Senior Retention Manager:** Churn Risk Prediction, SHAP Values, and all Low-, Medium-, and High-Cost Recommendations.

## Technology Choice 

### Frontend Choice

**Possible Options**

- **Streamlit** *(Selected)*
- HTML, CSS, and JavaScript (Traditional Web Frontend)

**Selected Technology:** **Streamlit**

Streamlit was selected because it satisfies the functional requirements of the Decision Support System while providing native Python integration, lower operational overhead, and faster development for a real-time decision-support dashboard prototype.

**Evaluation Factors**

- Functional Requirement Support
- Python Integration
- Operational Overhead
- Development Effort
- Authentication Support
- Long-Term Flexibility

> **Technology Decision:** Streamlit was selected based on the first four evaluation factors. HTML/CSS/JavaScript offers stronger authentication support and greater long-term flexibility for production-scale applications.

**Detailed Comparison:** [`Technology_Choices/01_Frontend_Choice.md`](Technology_Choices/01_Frontend_Choice.md#frontend-choice)

### Backend Choice

**Possible Options**

- **FastAPI** *(Selected)*
- Flask
- Django

**Selected Technology:** **FastAPI**

FastAPI was selected because it satisfies the functional requirements of the Decision Support System while providing seamless machine learning integration, low-latency API responses, native concurrent request handling, scalability across multiple client types, and straightforward implementation of role-based security.

**Evaluation Factors**

- Functional Requirement Support
- Machine Learning Integration
- Low Latency
- Concurrent Request Handling
- Scalability Across Multiple Clients
- Role-Based Security

> **Technology Decision:** FastAPI was selected because it satisfied all functional requirements and provided the best overall fit for a real-time, machine learning-driven Decision Support System serving multiple client types through a common API interface.

**Detailed Comparison:** [`Technology_Choices/02_Backend_Choice.md`](Technology_Choices/02_Backend_Choice.md#backend-choice)

### Database Choice

**Possible Options**

- **MariaDB** *(Selected)*
- MySQL
- PostgreSQL

**Selected Technology:** **MariaDB**

MariaDB was selected because it satisfies the functional requirements of the Decision Support System while providing an efficient relational database for customer profiles, recommendation rules, and recommendation actions with low operational overhead for this project's deployment environment.

**Evaluation Factors**

- Functional Requirement Support
- Query Performance
- Operational Overhead

> **Technology Decision:** MariaDB was selected because all three databases satisfy the functional requirements and provide sufficient query performance for the current workload. MariaDB and MySQL were equally suitable choices, while PostgreSQL introduced additional operational complexity that was unnecessary for the current scope of the Decision Support System. MariaDB was chosen due to team familiarity and simpler development setup on Linux.

**Detailed Comparison:** [`Technology_Choices/03_Database_Choice.md`](Technology_Choices/03_Database_Choice.md#database-choice)


## Data Science Pipeline Choice

Unlike a traditional churn prediction project that directly trains a machine learning model, this project follows a **business-first data science pipeline**. Every stage of the workflow was designed to convert raw customer data into business decisions that support real-time customer retention.

The pipeline was evaluated by choosing appropriate analytical methods for each stage of the customer churn problem instead of relying on a single machine learning technique.

### Selected Data Science Pipeline

| Pipeline Stage | Selected Method |
|----------------|-----------------|
| **Data Cleaning** | Missing value handling and noisy data preprocessing. |
| **Customer Behavior Analysis** | SQL-based behavioral segmentation and churn pattern discovery. |
| **Feature Engineering** | Business-driven engineered features (Issue Level, Delay Level, Spend Level, Contract Length). |
| **Statistical Validation** | Chi-Square Test, Cramér's V, and Logistic Regression Odds Ratios. |
| **Predictive Modeling** | Logistic Regression, Decision Tree, Random Forest, and XGBoost. |
| **Model Explainability** | SHAP (SHapley Additive Explanations). |
| **Business-Oriented Model Evaluation** | Segment-wise evaluation using customer business value, false positives, and false negatives. |

### Why This Pipeline Was Chosen

The pipeline was designed around the following data science objectives:

- **Understand customer behavior before modeling** using SQL analysis rather than treating feature engineering as a purely machine learning step.
- **Engineer interpretable business features** from customer behavior instead of relying only on raw numerical variables.
- **Validate feature importance statistically** before training predictive models.
- **Compare multiple machine learning models** using both predictive metrics and business-oriented evaluation criteria.
- **Explain every prediction** using SHAP so CRM agents and retention managers understand *why* a customer is predicted to churn.
- **Support business decision-making** by balancing churn prediction performance with retention cost and customer business value.

> **Pipeline Decision:** A business-first data science pipeline was selected to transform customer behavior into explainable churn predictions and actionable retention recommendations, making the model suitable for a real-time Decision Support System instead of a standalone prediction model.

**Detailed Pipeline & Methodology:** [`Technology_Choices/04_Data_Science_pipeline.md`](Technology_Choices/04_Data_Science_pipeline.md)

## Cloud Platform Choice

**Possible Options**

- **Google Cloud Run** *(Selected)*
- Render
- AWS

**Selected Technology:** **Google Cloud Run**

Google Cloud Run was selected because it satisfies the deployment requirements of the Decision Support System while providing low latency for Indian users, built-in high availability, automatic horizontal scaling, and low operational overhead for a containerized FastAPI application.

**Evaluation Factors**

- Functional Requirement Support
- Low Latency
- High Availability
- Horizontal Scalability
- Operational Overhead

> **Technology Decision:** Google Cloud Run was selected because it provides the required production capabilities with minimal infrastructure management. Render offers simpler hosting but fewer regional and scaling options, while AWS provides similar capabilities with greater operational complexity for the current project scope.

### Deployment Note

The application was initially planned for deployment on **Google Cloud Platform (Compute Engine)** using a Docker-based architecture. However, deployment on Google Cloud required enabling a prepaid billing account for Compute Engine, which was not feasible within the budget constraints of this academic project.

An alternative deployment platform, **Render**, was also evaluated. However, its deployment process required payment registration through a supported credit card, which was unavailable for this project.

To ensure the application could still be deployed and demonstrated within the available resources, the deployment was migrated to **Amazon Web Services (AWS)**.

AWS satisfies all the functional and non-functional deployment requirements originally identified for Google Cloud Platform, including Docker-based container deployment, REST API hosting, networking, horizontal scalability, high availability, and low-latency deployment through the **Mumbai (`ap-south-1`) region**. Although AWS introduces higher operational and configuration overhead than Google Cloud Run/Compute Engine, it provides the same required deployment capabilities and remains a production-grade cloud platform for the application's containerized microservices architecture. Therefore, AWS was selected as the final deployment platform while preserving the original Docker-based deployment workflow.


**Detailed Comparison:** [`Technology_Choices/05_Cloud_Service_Choice.md`](Technology_Choices/05_Cloud_Service_Choice.md#cloud-platform-choice)

## Architecture Choice

**Possible Options**

- **Monolithic Architecture** *(Selected)*
- Microservices Architecture

**Selected Architecture:** **Monolithic Architecture**

A monolithic architecture was selected because it satisfies the functional requirements of the Decision Support System while providing lower inter-service communication latency, sufficient scalability for the current request workflow, lower operational overhead, and simpler deployment and maintenance for a single FastAPI application.

**Evaluation Factors**

- Functional Requirement Support
- Inter-Service Communication Latency
- Independent Scalability
- Operational Overhead
- Failure Isolation

> **Technology Decision:** Monolithic architecture was selected because every customer request currently follows the same processing pipeline through the ML Prediction, SHAP, and Recommendation services, making a single deployment unit the simplest and most efficient design. Microservices provide better failure isolation and independent scaling, but those advantages are not required for the current scope of the Decision Support System.

**Detailed Comparison:** [`Technology_Choices/06_Architecture_Choice.md`](Technology_Choices/06_Architecture_Choice.md#architecture-choice)

### Streamlit + FastAPI Architecture Choice

**Possible Options**

- Streamlit Only
- **Streamlit + FastAPI** *(Selected)*

**Selected Architecture:** **Streamlit + FastAPI**

The application architecture separates the presentation layer from the backend application layer. Streamlit is used to build the interactive dashboard, while FastAPI exposes the machine learning prediction, SHAP explanation, recommendation engine, and database operations through reusable REST APIs.

**Evaluation Factors**

- Functional Requirement Support
- Asynchronous Processing
- Scalability Across Multiple Clients
- Fault Tolerance
- Code Maintainability
- Operational Complexity

> **Technology Decision:** Streamlit + FastAPI was selected because it provides a modular architecture with asynchronous request handling, reusable backend APIs, better fault isolation, and improved maintainability. Although a Streamlit-only application has lower operational complexity, separating the frontend and backend better supports the long-term design of the Decision Support System.

**Detailed Comparison:** [`Technology_Choices/07_Streamlit_VS_Fastapi+Streamlit_Choice.md`](Technology_Choices/07_Streamlit_VS_Fastapi+Streamlit_Choice.md#streamlit--fastapi-architecture-choice)


## Backend Design

The backend is implemented as a **FastAPI-based monolithic architecture** that orchestrates the complete decision support pipeline for customer churn prediction. A single API request flows through request validation, feature engineering, machine learning inference, explainability, business rule execution, role-based recommendation filtering, and unified response construction.

The backend processing pipeline consists of six stages:

1. Request Validation
2. Machine Learning Prediction Logic
3. SHAP Explainability Logic
4. Recommendation Engine Logic
5. Role-Based Decision Logic
6. Response Construction

---

### 1. Request Validation

The Request Validation layer is the entry point of the backend. It uses **Pydantic** to validate incoming customer data, enforce numerical and categorical constraints, and automatically generate engineered business features required throughout the prediction pipeline. This ensures that invalid requests are rejected before model inference and that every downstream component receives a standardized customer representation.

**📄 Detailed Documentation:** [Request Validation](Backend_Design/01_Request_Validation.md)

---

### 2. Machine Learning Prediction Logic

The Machine Learning Prediction layer executes the core inference pipeline of the Decision Support System. The backend first classifies the customer's business value (**High, Medium, or Low**) and then executes **XGBoost** and **Logistic Regression** in parallel. XGBoost is used to identify customers with a high likelihood of churn, while Logistic Regression estimates customer retention probability. The selected model is then passed to the SHAP Explainability Service before constructing a unified API response.

**📄 Detailed Documentation:** [Machine Learning Prediction Logic](Backend_Design/02_ml_service_logic.md)

### 3. SHAP Explainability Service

The SHAP Explainability Service explains **why** a customer was predicted to churn or remain with the service by identifying the contribution of each customer feature. The backend initializes separate SHAP explainers for **XGBoost (TreeExplainer)** and **Logistic Regression (LinearExplainer)** and automatically selects the appropriate explainer based on the prediction pipeline.

To improve real-time interpretability, SHAP values generated for **one-hot encoded features** are aggregated back into their original business features (such as *Issue Level* or *Contract Length*) by summing their contributions. The backend also converts these aggregated SHAP values into **relative contribution percentages**, allowing support staff and managers to quickly understand which customer characteristics contributed most to the churn prediction.

**📄 Detailed Documentation:** [SHAP Explainability Service](Backend_Design/03_shap_service_logic.md)

### 4. Churn Database Logic

The Churn Database is designed around a **behavioural customer profile** instead of storing recommendations for every individual customer. Customer features are divided into **customer profile features** (Spend Level, Contract Length, Tenure Level), which determine the cost and priority of retention strategies, and **customer behaviour features** (Issue Level, Delay Level), which determine whether the customer requires proactive or reactive intervention.

The database maps combinations of these engineered features to predefined recommendation rules, creating an interpretable and easily extensible rule-based retention system. The behavioural features were selected through SQL-based customer behaviour analysis to capture the customer characteristics most strongly associated with churn.

**📄 Detailed Documentation:** [Churn Database Logic](Backend_Design/04_churn_database_design.md)

### 5. Recommendation Engine Logic

The Recommendation Engine converts the engineered customer profile into **actionable retention strategies** using a rule-based decision system backed by **MariaDB**. It matches customer behaviour with predefined recommendation rules, retrieves the corresponding retention actions, applies **role-based access control (RBAC)** for different client types, and organizes recommendations into business-friendly categories sorted by service priority and implementation cost.

This design keeps business rules independent from machine learning models, making the recommendation system deterministic, interpretable, and easy to extend without modifying backend prediction logic.

**📄 Detailed Documentation:** [Recommendation Engine Logic](Backend_Design/05_Recommendation_engine_logic.md)

## Deployment Choices

### VPC Architecture Choices

The Churn DSS application is deployed inside a dedicated **Virtual Private Cloud (VPC)** to provide an isolated and scalable network environment. For Version 1, the architecture uses **one Availability Zone**, **one public subnet**, **no private subnets**, and **no NAT Gateway** to keep the deployment simple while leaving room for future production scaling with multiple Availability Zones, load balancers, and private backend services.

**Detailed documentation:** [01_VPC_Architecture_Choices.md](Deployment_Choices/01_VPC_Architecture_Choices.md)


### EC2 Deployment Choices

The Churn DSS application is deployed on a **single Amazon EC2 instance** running **Ubuntu Server 24.04 LTS** with the **64-bit x86 architecture**. The deployment uses a **t3.small** instance (2 vCPUs, 2 GB RAM) to provide enough resources for the frontend, FastAPI backend, and MariaDB containers while keeping the infrastructure cost-effective. The EC2 instance is secured using an **SSH key pair**, a dedicated **Security Group** with SSH access restricted to the developer's IP, and a **20 GB gp3 EBS volume** for persistent application and database storage.

**Detailed documentation:** [02_EC2_Choices.md](Deployment_Choices/02_EC2_Choices.md)


### Docker Compose Architecture

The Churn DSS application is deployed using **Docker Compose** on a single AWS EC2 instance. The application is divided into three containers, keeping the frontend, backend, and database isolated while allowing them to communicate through the internal Docker network.

```text
                         AWS EC2
                            │
                     Docker Compose
                            │
          ┌─────────────────┼─────────────────┐
          │                 │                 │
          ▼                 ▼                 ▼
   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
   │   Frontend   │  │   Backend    │  │   Database   │
   │   Streamlit  │──►│   FastAPI    │──►│   MariaDB    │
   │    :8501     │  │    :8000     │  │    :3306     │
   └──────────────┘  └──────────────┘  └──────────────┘
          │                 │                 │
          │                 │                 │
       User UI          ML + SHAP       Recommendation
                         + Business         Rules
                           Logic

```

* **Streamlit container** provides the user interface for interacting with the Churn DSS.
* **FastAPI container** handles prediction requests, ML inference, SHAP explanations, and business logic.
* **MariaDB container** stores the recommendation rules and actions used by the decision-support system.
* **Docker Compose** manages the three containers, their dependencies, networking, environment configuration, and persistent database storage.
* MariaDB is kept **internal to the Docker network** and is not directly exposed to the public internet.





**Detailed documentation:** [Docker Compose Architecture Choices](Deployment_Choices/03_Docker_Compose_Architecture.md)


### Environment Variable & Secret Management

Deployment-specific configuration is managed through **environment variables** using a `.env` file. This keeps database credentials and other configuration values separate from the application code and prevents sensitive information from being committed to GitHub.

The `.env` file is excluded through `.gitignore` and is maintained separately on the EC2 deployment environment. Docker Compose loads the required configuration for the backend and MariaDB services.

**Detailed documentation:** [Environment Variable and Secret Management](Deployment_Choices/04_Environment_Variable_and_Secret_Management.md)

### Networking & Security Group

The Churn DSS application is deployed within an **AWS VPC** using an **EC2 Security Group** to control network access.

The Version 1 configuration provides:

- **Port `22`** — SSH access restricted to the developer's IP address.
- **Port `8501`** — Public access to the Streamlit frontend.
- **Port `8000`** — Access to the FastAPI backend.
- **Port `3306`** — MariaDB remains internal to the Docker network and is not publicly exposed.

The deployment uses **one VPC, one public subnet, one EC2 instance, and one Security Group**, providing a simple networking architecture with restricted administrative access and internal database communication.

More advanced networking components such as private subnets and load balancers can be considered for future production deployments.

**Detailed documentation:** [Networking & Security Group Choices](Deployment_Choices/05_Networking_and_Security_Group_Choices.md)



### Deployment Workflow: GitHub → EC2

The Churn DSS application uses **GitHub as the source code repository** and **Amazon EC2 as the deployment environment**. The application is deployed and managed using Docker Compose.

The Version 1 workflow is:

```text
Developer
    │
    ▼
GitHub Repository
    │
    │ git pull
    ▼
AWS EC2
    │
    ▼
Docker Compose
    │
    ├──► Streamlit Container
    ├──► FastAPI Container
    └──► MariaDB Container
````

For application updates, changes are pushed to GitHub, pulled onto the EC2 instance, and the Docker containers are rebuilt using Docker Compose.

```bash
sudo docker compose up -d --build
```

The `.env` file is maintained separately on the EC2 instance, keeping deployment-specific credentials separate from the GitHub repository.

For Version 1, this **GitHub → EC2 → Docker Compose** workflow was selected because it is simple and suitable for the current single-instance deployment. A full CI/CD pipeline can be introduced in future versions.

**Detailed documentation:** [Deployment Workflow: GitHub → EC2](Deployment_Choices/07_Deployment_Workflow_GitHub_to_EC2.md)

### Future Enhancement

#### Context-Aware Recommendations

In the current version, the **Recommendation Engine operates independently based on customer attributes and predefined business rules**. Business value and churn risk are presented as separate decision-support outputs rather than being directly used as inputs to the recommendation engine.

This separation was intentionally maintained in Version 1 to keep the recommendation logic **simple, interpretable, and manageable**.

A future enhancement could introduce a more context-aware recommendation framework in which:

- **Business value** influences the appropriate cost or level of customer engagement.
- **Churn risk** influences whether the system prioritizes proactive or reactive engagement strategies.
- **Customer attributes** continue to determine the specific intervention applicable to the customer.

This could allow the system to move from independently generated recommendations toward a more integrated decision-support pipeline.

#### High Availability and Horizontal Scalability

The current Version 1 deployment uses a **single EC2 instance within a single Availability Zone**, which keeps the infrastructure simple and cost-effective for the academic deployment.

For a production-scale deployment where **high availability and horizontal scalability** are required, the architecture can be extended across **multiple Availability Zones**.

A future architecture could deploy application instances across **two Availability Zones**, allowing the system to continue operating if an instance or Availability Zone becomes unavailable.

The application tier can be horizontally scaled by running multiple instances of the Streamlit and FastAPI services behind a **load balancer**. This would distribute incoming requests across healthy instances and allow additional instances to be added as demand increases.

A future high-availability architecture could therefore follow:


                         Users
                           │
                           ▼
                    Load Balancer
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
       Availability Zone A       Availability Zone B
              │                         │
        ┌─────┴─────┐             ┌─────┴─────┐
        │ Application│             │ Application│
        │  Instance  │             │  Instance  │
        └────────────┘             └────────────┘
              │                         │
              └────────────┬────────────┘
                           │
                           ▼
                  Highly Available
                   Data Layer



This architecture would provide:

- Higher availability through deployment across multiple Availability Zones.
- Horizontal scalability by adding additional application instances as workload increases.
- Fault tolerance by allowing traffic to be redirected to healthy instances when an instance or Availability Zone becomes unavailable.
- Improved scalability compared with the current single-instance deployment.

This enhancement is intentionally left for a future production-oriented version because the current deployment focuses on demonstrating the complete Churn DSS functionality while keeping infrastructure complexity and cost manageable.

#### Authentication and Client-Specific Access

The current system demonstrates role-based behavior for the **Customer Interaction Client, Customer Monitoring AI Agent, and Senior Retention Manager**.

A future version could introduce **independent authentication and login mechanisms for each client**. Each authenticated user would be assigned an appropriate role and would only have access to the functionality and recommendations permitted for that role.

This would strengthen the existing role-based access model by moving from simulated client selection to **authenticated and authorized access control**.

#### Production-Ready Frontend

The current frontend is implemented using **Streamlit**, which is suitable for demonstrating the functionality of the Churn DSS and rapidly developing the user interface.

For a production deployment, the frontend could be redesigned using **HTML, CSS, and JavaScript** or a modern frontend framework. This would provide greater control over the user interface, user experience, responsiveness, and integration with the backend services.

#### Automated CI/CD Pipeline

The current deployment follows a **GitHub → EC2 → Docker Compose** workflow.

A future version could introduce an automated CI/CD pipeline that automatically builds, tests, and deploys new application versions after changes are pushed to the repository.

#### Advanced Monitoring and Model Lifecycle Management

The current system provides health checks for the **Prediction Service, SHAP Service, and Recommendation Service**.

A future production deployment could extend this with centralized logging, infrastructure monitoring, service-level metrics, model performance monitoring, and data-drift detection to support continuous operation and maintenance of the system.
