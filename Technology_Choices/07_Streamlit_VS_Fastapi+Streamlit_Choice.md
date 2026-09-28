## Streamlit + FastAPI Architecture Choice

Two application architectures were evaluated for the Real-Time Customer Engagement Decision Support System.

- **Option 1:** Streamlit Only
- **Option 2:** Streamlit + FastAPI *(Selected)*

The application architectures were evaluated against the functional and non-functional system requirements of the Decision Support System.

---

### 1. Functional Requirement Support

The architecture should support all functional requirements of the Decision Support System, including customer input collection, churn prediction, SHAP explanation generation, recommendation generation, business value calculation, and database interaction.

- **Streamlit Only:** Supports all required functionality within a single Streamlit application.
- **Streamlit + FastAPI:** Supports the same functionality by separating the user interface from the backend business services.

**Conclusion:** Both architectures satisfy the functional requirements of the Decision Support System.

---

### 2. Asynchronous Processing

The architecture should efficiently process multiple requests while waiting for database or network operations.

- **Streamlit Only:** Processes requests synchronously within the Streamlit application.
- **Streamlit + FastAPI:** Supports asynchronous request handling using `async` and `await`, allowing multiple requests to be processed concurrently during I/O operations.

**Conclusion:** Streamlit + FastAPI is preferred because asynchronous processing improves responsiveness when multiple CRM clients or AI agents send requests simultaneously.

---

### 3. Scalability Across Multiple Clients

The architecture should support multiple client applications using the same backend business logic.

- **Streamlit Only:** The business logic is tightly coupled with the Streamlit dashboard and is primarily designed for a single client interface.
- **Streamlit + FastAPI:** Exposes reusable REST APIs that can be consumed by the Streamlit dashboard, Customer Interaction Client, Customer Monitoring AI Agent, and future web or mobile applications.

**Conclusion:** Streamlit + FastAPI is preferred because it provides a reusable backend that can serve multiple client types without duplicating business logic.

---

### 4. Fault Tolerance

The architecture should isolate frontend and backend failures whenever possible.

- **Streamlit Only:** The user interface and business logic run within the same application, so an application failure affects the complete system.
- **Streamlit + FastAPI:** The frontend and backend run as independent services. If the frontend encounters an issue, the backend APIs can continue running independently, and vice versa.

**Conclusion:** Streamlit + FastAPI provides better fault tolerance through separation of frontend and backend services.

---

### 5. Code Maintainability

The architecture should keep the user interface, business logic, machine learning pipeline, and database operations easy to maintain as the project grows.

- **Streamlit Only:** UI code, prediction logic, recommendation logic, and database operations remain in the same application, making the codebase harder to organize as functionality increases.
- **Streamlit + FastAPI:** Separates responsibilities between the presentation layer and the application layer, making backend services easier to test, modify, and extend without affecting the frontend.

**Conclusion:** Streamlit + FastAPI is preferred because separating concerns improves long-term code maintainability.

---

### 6. Operational Complexity

The architecture should minimize development, deployment, and maintenance complexity for the project.

- **Streamlit Only:** Requires only a single application to develop, deploy, and maintain, resulting in the lowest operational complexity.
- **Streamlit + FastAPI:** Requires two applications (frontend and backend), API communication, and separate deployment or containerization, introducing additional operational overhead.

**Conclusion:** Streamlit Only has lower operational complexity because it is a single application architecture. Streamlit + FastAPI introduces additional complexity in exchange for better scalability, maintainability, asynchronous processing, and fault tolerance.

---

### Streamlit + FastAPI Architecture Decision

For this project, **Streamlit + FastAPI** was selected because it satisfies all functional requirements while providing asynchronous request handling, reusable APIs for multiple client types, better fault tolerance, and improved code maintainability through separation of concerns.

Although **Streamlit Only** offers lower operational complexity and is sufficient for small demonstration applications, the Decision Support System was designed as a modular backend service that can support CRM clients, AI monitoring agents, and future applications through a common FastAPI API layer.