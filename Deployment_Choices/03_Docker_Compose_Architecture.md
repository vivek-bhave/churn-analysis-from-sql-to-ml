
# Docker Compose Architecture Choices

## 1. Overview

**Docker Compose** is used to define and orchestrate the three containers required by the Churn DSS application.

Instead of managing each container separately, Docker Compose provides a single configuration for building, starting, networking, and managing the application services.

The Version 1 deployment consists of:

- **Database** — MariaDB
- **Backend** — FastAPI
- **Frontend** — Streamlit

All three services run on the same AWS EC2 instance.

---

## 2. Why Docker Compose Was Selected

Docker Compose was selected because it provides:

- **Simple multi-container management** through a single configuration.
- **Defined service dependencies** between the frontend, backend, and database.
- **Automatic Docker networking** between application services.
- **Centralized environment configuration** using `.env`.
- **Persistent database storage** through Docker volumes.
- **Simpler deployment and updates** on the EC2 instance.

This avoids manually starting and configuring each container individually.

---

## 3. Service Architecture

The Docker Compose configuration defines three services:

| Service | Container | Responsibility |
|---|---|---|
| `database` | `churn_database` | Stores recommendation rules and actions |
| `backend` | `churn_backend` | Provides the FastAPI API, ML inference, SHAP explanations, and business logic |
| `frontend` | `churn_frontend` | Provides the Streamlit user interface |

The service relationship is:

```text
                    Docker Compose
                          │
          ┌───────────────┼───────────────┐
          │               │               │
          ▼               ▼               ▼
   ┌────────────┐  ┌────────────┐  ┌────────────┐
   │  Frontend  │  │  Backend   │  │  Database  │
   │  Streamlit │──►│  FastAPI   │──►│  MariaDB   │
   │   :8501    │  │   :8000    │  │   :3306    │
   └────────────┘  └────────────┘  └────────────┘
````

---

## 4. Service Dependencies

The services are configured with dependencies to establish the intended startup order:

```text
Database
   ↓
Backend
   ↓
Frontend
```

The backend depends on the database, while the frontend depends on the backend.

This ensures that the application components are started in the required order.

---

## 5. Docker Networking

Docker Compose provides an internal network for communication between the containers.

The backend can communicate with the MariaDB container internally, while the frontend communicates with the backend API.

MariaDB is **not exposed through a public host port**, reducing unnecessary external access to the database.

---

## 6. Port Exposure

Only the application services that need external access expose ports on the EC2 instance:

| Service   |   Port | Access                       |
| --------- | -----: | ---------------------------- |
| Streamlit | `8501` | Public application interface |
| FastAPI   | `8000` | Exposed API endpoint         |
| MariaDB   | `3306` | Internal Docker network only |

The database therefore remains accessible to the backend without being directly exposed to the internet.

---

## 7. Persistent Database Storage

A Docker named volume is used for MariaDB:

```text
mariadb_data
```

The volume ensures that database data persists even if the MariaDB container is recreated or restarted.

The SQL initialization script is also mounted into the MariaDB container to initialize the recommendation database when required.

---

## 8. Environment Configuration

Environment-specific configuration is managed through a `.env` file rather than hardcoding database credentials directly into the application configuration.

The `.env` file contains database connection and MariaDB configuration values used by Docker Compose and the backend.

The `.env` file is excluded from Git using `.gitignore` so that credentials are not committed to the repository.

---

## 9. Deployment Approach

The complete application can be started or rebuilt using Docker Compose:

```bash
sudo docker compose up -d --build
```

This allows the frontend, backend, and database services to be built and started together.

For future updates, the deployment workflow is:

```text
GitHub
   ↓
git pull
   ↓
Docker Compose rebuild
   ↓
Updated containers
```

---

## 10. Version 1 Design Decision

For Version 1, Docker Compose was selected instead of a more complex container orchestration platform.

Running the three services through Docker Compose on a single EC2 instance provides a simple deployment architecture suitable for the current application.

More advanced orchestration can be considered in future versions if the application requires independent service scaling, higher availability, or distributed deployment.

```
```
