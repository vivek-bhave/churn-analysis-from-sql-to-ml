# Cloud Platform Choice

Three cloud platforms were evaluated for deploying the Real-Time Customer Engagement Decision Support System.

- **Option 1:** Google Cloud Run *(Selected)*
- **Option 2:** Render
- **Option 3:** AWS

The cloud platforms were evaluated against the functional and non-functional system requirements of the Decision Support System.

---

## Functional Requirement Support

The cloud platform should deploy a containerized FastAPI application, expose REST APIs for churn prediction, support Docker-based deployment, and integrate with the backend services required by the Decision Support System.

- **Google Cloud Run:** Fully supports containerized FastAPI applications through Docker images and managed serverless deployment.

- **Render:** Supports Docker-based deployment and REST API hosting for FastAPI applications.

- **AWS:** Fully supports containerized applications through services such as ECS, App Runner, and Lambda containers.

**Conclusion:** All three cloud platforms satisfy the functional deployment requirements of the Decision Support System.

---

## Low Latency

The cloud platform should provide low network latency so CRM agents and AI monitoring agents receive churn predictions and customer intelligence before engagement decisions are made.

- **Google Cloud Run:** Provides deployment in the **Mumbai (`asia-south1`) region**, allowing requests from Indian users to travel a shorter network path.

- **Render:** The nearest deployment region is **Singapore**, resulting in comparatively higher latency for users located in India.

- **AWS:** Also provides infrastructure in the **Mumbai region**, enabling similarly low network latency for Indian users.

**Conclusion:** Google Cloud Run and AWS both satisfy the low-latency requirement for Indian users, while Render is less suitable because its nearest deployment region is outside India.

---

## High Availability

The cloud platform should remain available during customer engagement workflows and automatically recover from unhealthy application instances.

- **Google Cloud Run:** Provides built-in health checks, self-healing, and managed availability by automatically replacing unhealthy container instances.

- **Render:** Provides managed application hosting with availability features, but exposes fewer production-grade availability controls.

- **AWS:** Provides high availability through managed infrastructure and availability zones, but requires more service configuration depending on the deployment architecture.

**Conclusion:** Google Cloud Run and AWS both satisfy the high-availability requirement, while Cloud Run provides these capabilities with less operational management.

---

## Horizontal Scalability

The cloud platform should automatically scale when multiple CRM agents and AI monitoring agents generate prediction requests simultaneously.

- **Google Cloud Run:** Automatically creates additional container instances based on request concurrency and CPU utilization, making it well suited for bursty real-time API traffic.

- **Render:** Supports autoscaling, but provides fewer scaling controls and configuration options compared to Cloud Run.

- **AWS:** Supports highly configurable autoscaling policies across multiple compute services, making it suitable for very large production workloads.

**Conclusion:** All three platforms support horizontal scaling. Google Cloud Run provides automatic scaling with minimal configuration, while AWS offers greater flexibility at the cost of increased infrastructure complexity.

---

## Operational Overhead

The cloud platform should minimize deployment, infrastructure management, monitoring, and maintenance complexity for the Decision Support System.

- **Google Cloud Run:** Serverless container deployment with minimal infrastructure management, making it easy to deploy and maintain a Dockerized FastAPI application.

- **Render:** Also offers simple deployment and low operational overhead for small applications.

- **AWS:** Requires configuring and managing additional cloud services depending on the deployment architecture, resulting in higher operational complexity.

**Conclusion:** Google Cloud Run and Render both provide low operational overhead, while AWS introduces additional infrastructure configuration that is unnecessary for the current project scope.

---

## Cloud Platform Technology Decision

For this project, **Google Cloud Run** was selected because it satisfies all functional requirements while providing low latency for Indian users, built-in high availability, automatic horizontal scaling, and low operational overhead for deploying a containerized FastAPI application.

Google Cloud Run was preferred over Render and AWS for the following reasons:

- **Functional Requirement Support:** Supports Docker-based deployment of the complete FastAPI application.
- **Low Latency:** Mumbai region provides lower latency for Indian users.
- **High Availability:** Built-in health checks and self-healing reduce operational management.
- **Horizontal Scalability:** Automatically scales container instances during bursts of customer requests.
- **Operational Overhead:** Provides serverless deployment with minimal infrastructure configuration.

Render is a good option for simple application hosting but offers fewer scaling and regional deployment options for this project. AWS satisfies all deployment requirements but introduces additional operational complexity that is unnecessary for the current monolithic Decision Support System.