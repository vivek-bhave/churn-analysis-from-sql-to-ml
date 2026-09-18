# Backend Choice

Three backend frameworks were evaluated for the Decision Support System:

- **Option 1:** FastAPI
- **Option 2:** Flask
- **Option 3:** Django

The backend technologies were evaluated against the functional and non-functional system requirements of the Real-Time Customer Engagement Decision Support System.

---

## Functional Requirement Support

The backend should support all functional requirements of the Decision Support System, including REST APIs, churn prediction requests, SHAP explanation generation, recommendation generation, database interaction, and role-based decision workflows.

- **FastAPI:** Fully supports all required API endpoints, business logic, machine learning integration, and database operations required by the DSS.
- **Flask:** Fully supports the functional requirements through custom API routes, business logic, and database integration.
- **Django:** Fully supports the functional requirements through Django REST Framework, database models, views, and business logic.

**Conclusion:** All three frameworks satisfy the functional requirements of the Decision Support System.

---

## Low Latency

The backend should provide low response latency so CRM clients and AI agents receive customer intelligence before engagement decisions are made.

- **FastAPI:** Designed for API-first applications with minimal request-processing overhead, making it well suited for low-latency real-time inference.
- **Flask:** Lightweight framework capable of providing low-latency API responses for REST-based applications.
- **Django:** Can provide low-latency APIs but includes additional framework components that introduce more request-processing overhead than lightweight API frameworks.

**Conclusion:** FastAPI is the preferred choice for minimizing API response latency in a real-time customer engagement workflow.

---

## Concurrent Request Handling

The backend should efficiently process multiple customer requests simultaneously so requests from CRM clients and AI agents do not wait unnecessarily while other requests are waiting for database or network operations.

- **FastAPI:** Supports asynchronous request handling, allowing multiple customer requests to be processed concurrently while other requests wait for I/O operations such as database queries.
- **Flask:** Processes requests synchronously by default, so concurrent request handling requires additional configuration or deployment setup.
- **Django:** Supports asynchronous capabilities in newer versions, but many request-processing components remain synchronous by default.

**Conclusion:** FastAPI is the preferred choice because it provides native support for concurrent request handling, making it suitable for CRM clients and AI monitoring agents generating simultaneous requests.

---

## Scalability

The backend should be able to serve requests from multiple client types, including web applications, mobile applications, and AI agents, through a common API interface without requiring changes to the core business logic.

- **FastAPI:** Designed for API-first applications and easily exposes reusable REST APIs that can be consumed by web applications, mobile applications, AI agents, and other services from the same backend.

- **Flask:** Can expose REST APIs for multiple clients, but requires more manual API organization as the application grows.

- **Django:** Supports REST APIs through Django REST Framework and can serve multiple clients, but includes additional framework components intended for full-stack web applications.

**Conclusion:** FastAPI is the preferred choice because its API-first design makes the backend easily consumable by multiple client types while keeping the business logic independent of the client interface.

## Role-Based Security

The backend should enforce role-based access control so each client receives only the decision intelligence and decision actions permitted for its role.

- **FastAPI:** Supports role-based authorization through dependency injection, middleware, and API-level permission checks, making it straightforward to restrict responses for different client roles.

- **Flask:** Supports role-based authorization through custom middleware or authentication extensions, but requires more manual implementation of access control logic.

- **Django:** Provides built-in authentication and permission mechanisms through Django and Django REST Framework, enabling role-based authorization for API endpoints.

**Role-Based Access in the Decision Support System**

| Client | Allowed Access |
|--------|----------------|
| **Customer Interaction Client** | Churn Risk Prediction, SHAP Values, and Customer Business Value. No access to engagement recommendations. |
| **Customer Monitoring AI Agent** | Churn Risk Prediction, SHAP Values, Customer Business Value, Low-Cost Recommendations, and Medium-Cost Recommendations. No access to High-Cost Recommendations. |
| **Senior Retention Manager** | Churn Risk Prediction, SHAP Values, Customer Business Value, and all Low-, Medium-, and High-Cost Recommendations. |

**Conclusion:** All three frameworks can implement role-based authorization. FastAPI and Django provide structured mechanisms for enforcing API-level permissions, while Flask requires more manual implementation of access control.

## Machine Learning Integration

The backend should integrate seamlessly with the machine learning pipeline, including XGBoost, SHAP, Pandas, NumPy, and the recommendation engine, while exposing prediction results through REST APIs.

- **FastAPI:** Provides native Python integration and is designed for serving machine learning inference through REST APIs with minimal additional configuration.
- **Flask:** Integrates easily with Python machine learning libraries and can expose ML models through REST APIs, but requires more manual API structure and request validation.
- **Django:** Supports machine learning integration through Django REST Framework, but the framework includes additional components intended for full-stack web applications that are not required for an API-first ML service.

**Conclusion:** FastAPI is the preferred choice because it provides an API-first architecture with seamless integration for Python-based machine learning inference and explainable AI services.

## Backend Technology Decision

For this project, **FastAPI** was selected as the backend framework because it satisfies all functional requirements of the Decision Support System while providing seamless machine learning integration, low-latency API responses, native concurrent request handling, scalability for multiple client types, and support for role-based security.

FastAPI was preferred over Flask and Django for the following reasons:

- **Functional Requirement Support:** Supports all REST APIs, business logic, database interaction, and role-based workflows required by the DSS.
- **Machine Learning Integration:** Integrates naturally with XGBoost, SHAP, Pandas, NumPy, and the recommendation engine within the same Python ecosystem.
- **Low Latency:** Optimized for API-centric applications with minimal request-processing overhead for real-time customer engagement.
- **Concurrent Request Handling:** Supports asynchronous request processing, allowing multiple CRM clients and AI agents to be served simultaneously.
- **Scalability:** Exposes reusable REST APIs that can be consumed by web applications, mobile applications, and AI agents without changing the backend business logic.
- **Role-Based Security:** Enables API-level authorization so each client receives only the decision intelligence and decision actions permitted for its role.

Flask and Django can also implement the required functionality. However, FastAPI was chosen because its API-first design aligns better with the real-time, machine learning-driven architecture of the Decision Support System.
