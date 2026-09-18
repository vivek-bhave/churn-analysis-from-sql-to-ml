# Architecture Choice

Two software architectures were evaluated for the Real-Time Customer Engagement Decision Support System.

- **Option 1:** Monolithic Architecture *(Selected)*
- **Option 2:** Microservices Architecture

The architectures were evaluated against the functional and non-functional system requirements of the Decision Support System.


## 5.1 Functional Requirement Support

The architecture should support all functional requirements of the Decision Support System, including churn prediction, SHAP explanation generation, recommendation generation, role-based decision logic, and database interaction through a single customer request workflow.

- **Monolithic Architecture:** Supports all functional workflows within a single FastAPI application where the Churn Prediction Service, SHAP Reasoning Service, Recommendation Service, and Role-Based Decision Logic share the same codebase and database connection.

- **Microservices Architecture:** Supports the same functional workflows by separating each business capability into independent services that communicate through APIs while interacting with a shared database or multiple databases.

**Conclusion:** Both monolithic and microservices architectures satisfy the functional requirements of the Decision Support System.

## 5.2 Inter-Service Communication Latency

The architecture should minimize communication latency between internal business services because every customer request passes through multiple services before a response is returned to CRM clients or AI agents.

- **Monolithic Architecture:** Communication between the Churn Prediction Service, SHAP Reasoning Service, Recommendation Service, and Role-Based Decision Logic occurs through direct Python function calls within the same application process, resulting in minimal communication overhead.

- **Microservices Architecture:** Each business service communicates through HTTP or gRPC requests, requiring request serialization, network communication, and response deserialization between services before completing a customer request.

**Conclusion:** Monolithic architecture provides lower inter-service communication latency because internal function calls are faster than network-based communication between independent services.
## 5.3 Independent Scalability

The architecture should support scaling individual business services when different services receive significantly different workloads from different clients.

- **Monolithic Architecture:** Scales the entire application as a single deployment unit. Every customer request passes through the same pipeline—Churn Prediction, SHAP Reasoning, and Recommendation Service—so all three services receive approximately the same number of requests per unit time. Scaling the complete application is sufficient for the current workload.

- **Microservices Architecture:** Allows the Churn Prediction Service, SHAP Service, and Recommendation Service to scale independently based on the workload received by each service. This is beneficial when one service becomes a bottleneck while the others receive fewer requests.

**Conclusion:** For the current Decision Support System, every customer request flows through all business services, so independent scaling provides little practical benefit. A monolithic architecture is therefore sufficient and keeps the system simpler. If future production traffic is dominated by Customer Interaction Clients that only require churn prediction and SHAP reasoning, the ML and SHAP services could be separated into microservices and scaled independently without scaling the Recommendation Service.

### 5.4 Operational Overhead

The architecture should minimize the operational overhead of deployment, monitoring, debugging, and maintenance while keeping the Decision Support System easy to manage in production.

- **Monolithic Architecture:** The entire application is deployed as a single unit, requiring one Docker container, one deployment pipeline, centralized logging, and a single monitoring configuration. Updates, debugging, and maintenance are performed in one application.

- **Microservices Architecture:** Each business service is deployed independently, requiring multiple Docker containers, separate deployment pipelines, service communication, distributed logging, monitoring for each service, and version management across services.

**Conclusion:** Monolithic architecture has lower operational overhead because the entire Decision Support System is deployed, monitored, and maintained as a single application. Microservices provide deployment flexibility but introduce additional operational complexity that is unnecessary for the current project scope.

### 5.5 Failure Isolation

The architecture should isolate failures so that a failure in one business service does not unnecessarily stop other parts of the Decision Support System.

- **Monolithic Architecture:** All business services run within the same application. If the entire application fails, the complete Decision Support System becomes unavailable. However, supporting service failures can be handled within the application. For example, if the SHAP or Recommendation Service encounters an error, the system can still return the churn prediction while informing the client that the supporting service is temporarily unavailable.

- **Microservices Architecture:** Each business service runs independently. If one service fails, the remaining services can continue operating. For example, the Recommendation Service can become unavailable while the Churn Prediction and SHAP services continue serving customer requests independently.

**Conclusion:** Microservices provide stronger failure isolation because failures remain confined to individual services instead of affecting the entire application. For the current Decision Support System, the core ML Prediction and SHAP Service is the primary business service, while Recommendation are supporting services. A monolithic architecture can still provide the primary prediction service when a supporting service fails, but a failure of the monolithic application makes the entire system unavailable.

## Architecture Technology Decision

**Selected Architecture:** **Monolithic Architecture**

A monolithic architecture was selected because it satisfies all functional requirements of the Real-Time Customer Engagement Decision Support System while providing lower inter-service latency, sufficient scalability for the current request workflow, lower operational overhead, and a simpler deployment architecture.

Monolithic architecture was preferred over microservices for the following reasons:

- **Functional Requirement Support:** Supports churn prediction, SHAP explanation generation, recommendation generation, role-based decision logic, and database interaction within a single FastAPI application.

- **Inter-Service Communication Latency:** The Churn Prediction Service, SHAP Service, and Recommendation Service communicate through direct Python function calls instead of HTTP requests, reducing internal communication latency during real-time customer engagement.

- **Independent Scalability:** Every customer request currently passes through the ML Prediction Service, SHAP Service, and Recommendation Service, so each service receives approximately the same number of requests. Scaling the entire application is sufficient for the current workload.

- **Operational Overhead:** The complete application is deployed, monitored, and maintained as a single Dockerized FastAPI service, reducing deployment and maintenance complexity.

- **Failure Isolation:** Microservices provide better isolation when independent services fail. However, in the current system, SHAP and Recommendation are supporting services while ML Prediction is the primary business service. The application can still return churn predictions if a supporting service is temporarily unavailable through appropriate error handling.

**Why Not Microservices?**

Microservices become beneficial when different business services experience significantly different traffic patterns or need to scale independently. For example, if Customer Interaction Clients generate a much larger number of requests that only require churn prediction and SHAP reasoning, the ML Prediction Service and SHAP Service could be separated and scaled independently from the Recommendation Service.

For the current project, the services are tightly coupled, share the same request pipeline and database, and are deployed together. Therefore, a **Monolithic Architecture** provides the simplest and most appropriate design for this version of the Decision Support System.