# Deployment Workflow: GitHub → EC2

## 1. Overview

The Churn DSS application uses **GitHub as the source code repository** and **Amazon EC2 as the deployment environment**.

The deployment workflow allows the application code to be pulled from GitHub onto the EC2 instance and deployed using Docker Compose.

---

## 2. Deployment Workflow

The overall deployment process is:

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
```

---

## 3. Initial Deployment

The initial deployment consists of the following steps:

1. Create and configure the AWS EC2 instance.
2. Install Docker and Docker Compose on the EC2 instance.
3. Clone the GitHub repository onto the EC2 instance.
4. Configure the deployment `.env` file.
5. Build the application containers using Docker Compose.
6. Start the application services using Docker Compose.
7. Configure the AWS Security Group for required network access.
8. Verify the deployed application through the Streamlit interface.

---

## 4. Application Updates

When changes are pushed to the GitHub repository, the EC2 instance can be updated by pulling the latest code and rebuilding the containers.

The update workflow is:

```text
Developer
    │
    ▼
Push changes
    │
    ▼
GitHub
    │
    ▼
EC2
    │
    ├── git pull
    │
    ▼
Docker Compose
    │
    ├── Build updated images
    │
    ▼
Updated Containers
```

The application can be rebuilt and started using:

```bash
sudo docker compose up -d --build
```

---

## 5. Configuration Separation

The `.env` file is maintained separately from the GitHub repository.

Therefore, pulling the latest application code from GitHub does not overwrite the deployment-specific environment configuration.

This keeps application source code and deployment credentials separate.

---

## 6. Version 1 Deployment Decision

For Version 1, a **GitHub → EC2 → Docker Compose** deployment workflow was selected because it is simple to manage and appropriate for the current single-instance deployment.

A full CI/CD pipeline was not introduced in Version 1.

Future versions can automate the deployment process using a CI/CD platform when automated testing, image building, and deployment become necessary.
