# VPC Architecture Choices for Churn DSS

The Churn Decision Support System is deployed inside a **single Virtual Private Cloud (VPC)**. The goal of this design is to keep the deployment simple for the first version while leaving room for future scaling and production improvements.

---

## VPC CIDR Block — `10.0.0.0/16`

We created the VPC with the CIDR block **10.0.0.0/16**.

**Why this choice?**

- It provides a large private IP address space (65,536 IP addresses).
- We do not need that many IPs today, but it gives enough room for future scaling.
- If the application grows, we can create additional subnets for load balancers, databases, monitoring services, or more application servers without redesigning the network.

This decision was made for future scalability rather than today's requirements.

---

## Number of Availability Zones — 1

We selected **1 Availability Zone**.

**Why this choice?**

- Availability Zones are used for **high availability**, not for deciding how many EC2 instances we can create.
- A single Availability Zone can contain multiple EC2 instances if required.
- Since Version 1 of Churn DSS uses only **one EC2 instance**, creating multiple Availability Zones would add unnecessary infrastructure complexity.

### Future Improvement

If higher availability becomes necessary, we can deploy EC2 instances in multiple Availability Zones and use a Load Balancer to route traffic if one Availability Zone becomes unavailable.

---

## Number of Public Subnets — 1

We created **1 Public Subnet**.

**Why this choice?**

- The EC2 instance hosting the application needs to be accessible from the internet.
- Since we are using one Availability Zone and one EC2 instance, a single public subnet is sufficient.
- This keeps the network design simple while allowing users to access the application through its public IP.

---

## Number of Private Subnets — 0

We created **0 Private Subnets**.

**Why this choice?**

- The frontend, FastAPI backend, and MariaDB database all run inside the same EC2 instance using Docker Compose.
- Docker already provides internal networking between containers.
- Creating separate AWS private subnets would increase operational complexity without adding meaningful benefits in this deployment.

### Future Improvement

If the backend or database is moved to separate AWS services (such as Amazon RDS or ECS), private subnets can be introduced.

---

## Public Subnet CIDR Block — `/20`

AWS automatically created the public subnet using a **/20** CIDR block.

**Why keep the default?**

- A `/20` subnet provides more than 4,000 usable private IP addresses.
- It is much more than our current needs, but it leaves enough address space inside the VPC for future subnet creation.
- Using the default subnet layout also keeps the VPC organized for future expansion.

---

## NAT Gateway — None

We selected **No NAT Gateway**.

**Why this choice?**

- NAT Gateway is useful for resources inside **private subnets** that need internet access.
- Our EC2 instance is already inside a public subnet and can access the internet through the Internet Gateway.
- Adding a NAT Gateway would increase cost without providing any benefit for this version of the project.

---



## DNS Options — Enabled

Both **DNS Resolution** and **DNS Hostnames** are enabled.

**Why this choice?**

- The EC2 instance needs DNS resolution to install packages, pull Docker images, and access GitHub.
- DNS hostnames also help AWS resources communicate correctly inside the VPC.
- These settings are required for a smooth deployment experience.

---

## Summary of VPC Design Decisions

| Choice | Reason |
|--------|--------|
| **1 VPC** | Single isolated network for the entire application. |
| **CIDR `10.0.0.0/16`** | Large private IP space for future scaling. |
| **1 Availability Zone** | One EC2 deployment, reduced complexity and cost. |
| **1 Public Subnet** | Internet-facing EC2 for the application frontend. |
| **0 Private Subnets** | Docker networking is sufficient for Version 1. |
| **Public Subnet `/20`** | Plenty of IP addresses and room for future subnet expansion. |
| **No NAT Gateway** | No private subnet, so NAT is unnecessary. |
| **DNS Enabled** | Required for internet access and AWS networking. |