## EC2 Instance Name — `churn-dss-server`

We named the EC2 instance **`churn-dss-server`** to clearly identify its purpose within the project.

**Why this choice?**

- `churn-dss` identifies the project.
- `server` indicates that this EC2 instance hosts the deployed application.
- A consistent naming convention makes future infrastructure easier to manage when additional servers or AWS resources are added.

## AMI Choice — Ubuntu Server 24.04 LTS

We selected **Ubuntu Server 24.04 LTS** as the Amazon Machine Image (AMI) for the EC2 instance.

**Why this choice?**

- Ubuntu is a stable and widely used Linux operating system for cloud deployments.
- It has excellent support for Docker, FastAPI, Python, and MariaDB, which are the core technologies used in this project.
- Ubuntu has a large developer community and extensive documentation, making deployment and troubleshooting easier.
- The **24.04 LTS (Long Term Support)** release provides long-term security updates and a stable environment for production-style deployments.

This AMI provides a reliable Linux environment for deploying the complete Churn DSS application using Docker Compose.

## CPU Architecture — 64-bit (x86)

We selected the **64-bit (x86)** CPU architecture for the EC2 instance.

**Why this choice?**

- x86 is the most widely supported CPU architecture for cloud servers.
- It provides maximum compatibility with Docker images, Python libraries, FastAPI, and MariaDB used in this project.
- The development environment also uses an x86-based Linux machine, so the deployment environment remains consistent.
- Choosing x86 reduces the chances of architecture-related compatibility issues during deployment.

Although AWS also offers ARM-based instances, x86 was selected for Version 1 because compatibility and deployment simplicity were prioritized over architecture-specific cost optimizations.

## EC2 Instance Type — `t3.small`

We selected the **t3.small** EC2 instance type for the Churn DSS deployment.

**Why this choice?**

- It provides **2 vCPUs** and **2 GB RAM**, which is sufficient for running Docker Compose, FastAPI, MariaDB, and the frontend together on a single EC2 instance.
- The T3 family is designed for applications with low to moderate traffic that occasionally require CPU bursts, making it suitable for this project.
- It balances performance and cost while supporting concurrent API requests in Version 1 of the application.

The instance can be upgraded later if the application receives higher traffic or additional services are deployed.

---

## EC2 Key Pair — `churn-dss-key`

We created a dedicated SSH key pair named **`churn-dss-key`**.

**Why this choice?**

- It provides secure authentication for connecting to the EC2 instance.
- The private `.pem` key remains on the local machine, while AWS stores the corresponding public key.
- This is more secure than password-based login and is the standard method for accessing Linux EC2 instances.

## Security Group

We created a dedicated Security Group for the EC2 instance.

**Why this choice?**

- SSH access is allowed only from **My IP** instead of the entire internet.
- This restricts administrative access to the developer's machine and reduces the attack surface.
- HTTP and HTTPS ports were not opened during the initial launch because the application had not been deployed yet.

Additional web access rules can be added later after the application is running.

---

## Storage — 20 GB gp3 EBS

We selected a **20 GB gp3 EBS root volume** for the EC2 instance.

**Why this choice?**

- It provides enough storage for Ubuntu, Docker, FastAPI, MariaDB, frontend files, logs, and future package updates.
- gp3 is AWS's recommended SSD storage for general-purpose workloads.
- The storage size is sufficient for Version 1 while leaving room for application growth.

---

## File System — None

We selected **None** for additional file systems.

**Why this choice?**

- The entire application runs inside a single EC2 instance using Docker Compose.
- Docker volumes provide the required local storage for containers and the MariaDB database.
- Shared storage services such as EFS, FSx, or S3 are unnecessary in the current architecture and can be added in future versions if the application is distributed across multiple servers.