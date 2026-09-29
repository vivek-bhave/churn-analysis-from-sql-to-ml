# Environment Variable and Secret Management

## 1. Overview

The Churn DSS application uses **environment variables** to manage deployment-specific configuration separately from the application code.

The deployment configuration is stored in a `.env` file and loaded by Docker Compose and the backend container.

---

## 2. Why Environment Variables Were Used

Environment variables were selected to provide:

* **Separation of configuration from application code.**
* **Secure handling of database credentials.**
* **Different configuration values for different environments.**
* **Simpler deployment configuration on the EC2 instance.**
* **Avoidance of hardcoded credentials in the source code.**

This allows the application code and deployment configuration to be managed independently.

---

## 3. Database Configuration

The `.env` file contains the configuration required for the MariaDB database and backend connection.

The configuration includes:

* Database host
* Database port
* Database name
* Database username
* Database password
* MariaDB initialization credentials

The backend reads these values through environment variables when establishing the database connection.

---

## 4. `.env` File Protection

The `.env` file contains sensitive database credentials and is therefore **not committed to GitHub**.

The file is added to `.gitignore`:

```gitignore
.env
.env.local
```

This prevents deployment credentials from being accidentally pushed to the public repository.

---

## 5. Deployment Configuration

The `.env` file is created separately on the deployment environment.

For the EC2 deployment:

```text
EC2 Instance
     │
     ├── Application Repository
     │
     └── .env
           │
           ▼
     Docker Compose
           │
      ┌────┴────┐
      ▼         ▼
   Backend   MariaDB
```

Docker Compose loads the environment variables and provides the required configuration to the relevant services.

---

## 6. Version 1 Security Approach

For Version 1, sensitive configuration is managed through a local `.env` file on the EC2 instance rather than storing credentials directly in the GitHub repository.

This approach is suitable for the current single-instance academic deployment.

For a future production deployment, a dedicated secrets-management solution can be considered.
