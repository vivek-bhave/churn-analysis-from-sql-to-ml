# Database Choice

Three relational databases were evaluated for the Decision Support System:

- **Option 1:** MariaDB
- **Option 2:** MySQL
- **Option 3:** PostgreSQL

The databases were evaluated against the functional and non-functional system requirements of the Real-Time Customer Engagement Decision Support System.

## Functional Requirement Support

The database should support all functional requirements of the Recommendation Service, including storing customer profiles, recommendation rules, recommendation actions, engineered customer features, and supporting CRUD operations and relational queries required by the Decision Support System.

- **MariaDB:** Fully supports the required relational schema for customer profiles, recommendation rules, and recommendation actions. Supports indexed lookups, filtering on multiple engineered features, transactions, and CRUD operations required by the Recommendation Service.

- **MySQL:** Fully supports the same relational schema, CRUD operations, transactions, indexing, and multi-column filtering required by the Decision Support System.

- **PostgreSQL:** Fully supports the relational schema, CRUD operations, transactions, indexing, complex filtering, and relational queries required for customer engagement workflows.

**Conclusion:** All three databases satisfy the functional requirements of the Decision Support System. Each database can efficiently store and retrieve customer profiles, recommendation rules, recommendation actions, and the engineered customer features used by the Recommendation Service.

## Query Performance

The database should retrieve customer profiles, recommendation rules, and recommendation actions with low query latency during customer engagement workflows.

- **MariaDB:** Provides fast indexed lookups for customer profiles, recommendation rules, and recommendation actions.
- **MySQL:** Provides similar indexed query performance for the same relational workload.
- **PostgreSQL:** Also provides efficient query execution for indexed relational lookups and transactions.

**Conclusion:** The Decision Support System uses a relatively small recommendation rule table (around 30 business rules) and indexed recommendation actions. For this workload, MariaDB, MySQL, and PostgreSQL all provide sufficiently low query latency, so query performance is not a deciding factor in the database selection.

## Operational Overhead

The database should minimize the operational overhead of installation, configuration, deployment, and maintenance while integrating with the FastAPI backend and Docker-based deployment environment.

- **MariaDB:** Lightweight, easy to install and configure, and integrates seamlessly with Docker and the Python backend. It provides all the required relational database capabilities with minimal operational complexity.

- **MySQL:** Offers a very similar operational experience to MariaDB. Installation, configuration, Docker deployment, and maintenance effort are comparable, making it an equally suitable choice for this project.

- **PostgreSQL:** Integrates well with modern deployment environments and provides excellent production-grade tooling. However, it introduces additional configuration and administration complexity because of its broader feature set, which is not required for the current transactional workload of the Decision Support System.

**Conclusion:** MariaDB and MySQL are both suitable choices for this project from an operational perspective. PostgreSQL is a powerful database for larger and more complex applications, but its additional operational complexity is unnecessary for the current scope of the Decision Support System. MariaDB was selected because the development team was already familiar with it on Linux, allowing faster setup and lower development overhead without sacrificing any required functionality.