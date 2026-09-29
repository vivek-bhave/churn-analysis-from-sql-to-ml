# Networking & Security Group Choices

## 1. Overview

The Churn DSS application is deployed within an **AWS VPC** and uses an **EC2 Security Group** to control network access to the application.

The networking configuration is designed to provide public access to the application while restricting administrative access to the EC2 instance.

---

## 2. Security Group Configuration

The EC2 instance is associated with a dedicated **Security Group** that controls inbound network traffic.

The main inbound rules are:

| Port   | Protocol | Source                 | Purpose               |
| ------ | -------- | ---------------------- | --------------------- |
| `22`   | TCP      | Developer's IP address | SSH administration    |
| `8501` | TCP      | Public                 | Streamlit application |
| `8000` | TCP      | Public                 | FastAPI API           |

---

## 3. SSH Access

SSH access through port `22` is restricted to the **developer's IP address**.

This prevents unrestricted internet access to the SSH service while allowing the developer to remotely manage the EC2 instance.

---

## 4. Application Access

The Streamlit frontend is exposed through port `8501` so that users can access the deployed application through a web browser.

The FastAPI backend is exposed through port `8000` for API access.

---

## 5. Database Network Security

MariaDB uses port `3306` internally between the Docker containers.

The database port is **not exposed through the EC2 Security Group** and is not directly accessible from the public internet.

The backend communicates with MariaDB through the internal Docker network.

---

## 6. Outbound Traffic

The EC2 instance allows outbound network traffic required for normal application operation, including communication with external services and package repositories when required.

---

## 7. Version 1 Networking Decision

For Version 1, the application uses a simple networking architecture consisting of:

* One AWS VPC
* One public subnet
* One EC2 instance
* One Security Group
* Public access to the application
* Restricted SSH access
* Internal database communication

This configuration keeps the deployment simple while providing basic network isolation and access control.

More advanced networking, such as private subnets, load balancers, and separate backend infrastructure, can be considered for future production deployments.
