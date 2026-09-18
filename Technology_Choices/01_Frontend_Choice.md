# 1. Frontend Choice

Two frontend options were considered for the Decision Support System:

- **Option 1:** HTML, CSS, and JavaScript (Traditional Web Frontend)
- **Option 2:** Streamlit (Python-Based Frontend)

The frontend technologies were evaluated against the system requirements of the Real-Time Customer Engagement Decision Support System.

---

## 1.1 Functional Requirement Support

The frontend should display all functional outputs of the Decision Support System, including churn risk prediction, SHAP explanations, customer business value, customer context, and engagement recommendations.

- **HTML/CSS/JavaScript:** Fully supports all functional requirements through a custom web interface.
- **Streamlit:** Fully supports all functional requirements through built-in dashboard components and visualization widgets.

**Conclusion:** Both frontend technologies satisfy the functional requirements of the Decision Support System.

---

## 1.2 Python Integration

The frontend should integrate seamlessly with Python-based machine learning models, SHAP explanations, Pandas DataFrames, and visualization libraries.

- **HTML/CSS/JavaScript:** Requires communication with Python through REST APIs and JSON responses.
- **Streamlit:** Provides native integration with Python code, machine learning models, SHAP, Pandas, Plotly, and Matplotlib.

**Conclusion:** Streamlit is preferred because it provides native Python integration without requiring an API communication layer for frontend rendering.

---

## 1.3 Operational Overhead

The frontend should minimize development, deployment, and maintenance complexity.

- **HTML/CSS/JavaScript:** Requires a separate frontend project, build process, deployment pipeline, and ongoing maintenance.
- **Streamlit:** Uses a single Python application with lower deployment and maintenance complexity.

**Conclusion:** Streamlit has lower operational overhead for this project.

---

## 1.4 Development Effort

The frontend should allow rapid development and easier implementation of machine learning dashboards.

- **HTML/CSS/JavaScript:** Requires building the interface, styling, routing, and frontend components from scratch.
- **Streamlit:** Provides ready-to-use UI components, forms, charts, tables, and layout utilities using Python.

**Conclusion:** Streamlit requires less development effort for a machine learning dashboard application.

---

## 1.5 Authentication Support

The frontend should support secure user authentication for different client roles such as CRM agents, AI agents, and Senior Retention Managers.

- **HTML/CSS/JavaScript:** Easily integrates with authentication mechanisms such as JWT, OAuth, Firebase Authentication, Auth0, or custom login systems.
- **Streamlit:** Supports authentication through additional libraries or custom implementations, but it is not a built-in frontend authentication framework.

**Conclusion:** HTML/CSS/JavaScript provides greater flexibility for implementing authentication and user login workflows.

---

## 1.6 Long-Term Flexibility

The frontend should remain extensible as the Decision Support System evolves into a larger production application.

- **HTML/CSS/JavaScript:** Better suited for large-scale production applications with responsive UI, reusable components, routing, authentication, and integration with multiple frontend frameworks.
- **Streamlit:** Well suited for dashboards and internal decision support tools, but offers less flexibility for building complex production web applications.

**Conclusion:** HTML/CSS/JavaScript provides greater long-term flexibility for scaling the frontend into a full production web application.

## Frontend Technology Decision

For this project, **Streamlit** was selected as the frontend technology because it provides native Python integration, lower operational overhead, and significantly reduces development effort while satisfying all functional requirements of the Decision Support System.

The objective of this project is to demonstrate a **working real-time Decision Support System prototype** rather than develop a production-ready enterprise web application. Given the limited development time and a small development team, Streamlit allows the frontend, machine learning logic, and visualizations to be developed and maintained within a single Python ecosystem.

A traditional **HTML/CSS/JavaScript** frontend offers stronger support for authentication workflows and greater long-term flexibility for production-scale applications. However, for the scope of this demonstration project, **Streamlit was preferred** because it enables faster implementation with lower operational complexity while meeting the project's functional requirements.