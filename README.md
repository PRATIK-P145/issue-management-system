# Issue Tracker API

A backend service for managing issues, comments, labels, and reports — built with a strong focus on data consistency, concurrency safety, and transactional correctness.

This project simulates a simplified issue tracking system (similar to Jira/GitHub Issues) and is designed to demonstrate real-world backend engineering practices.

---

## 🚀 Features

### Core Functionality
- Create, retrieve, update, and list issues
- Optimistic concurrency control using versioning
- Add comments to issues with validation
- Assign and replace labels atomically
- Transactional bulk status updates
- CSV-based bulk issue import with row-level validation
- Analytical reports for issue handling

### Reliability & Safety
- PostgreSQL constraints and indexes
- Transactional operations to prevent partial updates
- Clear error handling and HTTP status codes
- Minimal but meaningful automated tests

---

## 🛠 Tech Stack

- **Backend Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy (minimal usage)
- **Migrations**: Alembic
- **Testing**: pytest

“PostgreSQL is hosted on Supabase for ease of development; all schema management, transactions, and business logic are implemented in the FastAPI backend.”


---

##  Key Design Decisions
Perfect. This format is **exactly what evaluators like** because it shows awareness + intent.

Here is a **clean, structured README-ready section** in the format you asked.
You can paste this directly.

---

## ⚙️ Key Engineering Challenges Addressed

---

### 1. Concurrency Handling

Concurrency issues arise when multiple clients attempt to update the same issue at the same time, which can lead to lost or overwritten updates if not handled properly.

**API endpoints / tasks where it appears:**

* `PATCH /issues/{id}` — Updating issue details

**My strategy to handle it:**
The project uses **optimistic concurrency control** by maintaining a version field on each issue. Clients must send the current version during updates. If the version does not match the database value, the update is rejected, preventing silent overwrites and ensuring safe concurrent updates.

---

### 2. Transaction Management

Transaction challenges occur when an operation involves multiple database changes that must either all succeed or all fail to avoid inconsistent or partial data states.

**API endpoints / tasks where it appears:**

* `POST /issues/bulk-status` — Bulk status updates
* `PUT /issues/{id}/labels` — Atomic label replacement
* `POST /issues/import` — Batch inserts during import

**My strategy to handle it:**
All multi-step operations are wrapped inside **database transactions**. If any step fails, the transaction is rolled back automatically, ensuring atomicity and preserving data consistency across all affected records.

---

### 3. CSV Import Handling

CSV imports introduce challenges related to data validation, partial failures, and large batch inserts, which can corrupt data if handled naively.

**API endpoints / tasks where it appears:**

* `POST /issues/import` — Importing issues from CSV files

**My strategy to handle it:**
The import process includes structured CSV parsing, row-level validation, and controlled batch inserts. Imports are executed within transactions to avoid partial data insertion, and invalid rows are reported without affecting valid data.

---

### 4. Schema Evolution & Migrations

As project requirements evolve, the database schema needs to change without breaking existing data or deployments.

**API endpoints / tasks where it appears:**

* Adding fields like `created_at`, `priority`, `assigned_to`
* Supporting filters, sorting, and reporting features

**My strategy to handle it:**
All schema changes are managed using **Alembic migrations**, enabling versioned, incremental, and reversible updates. This allows the database structure to evolve safely while maintaining compatibility across environments.

---

## 📂 Project Structure
```
app/
├── main.py      # FastAPI application & routes
├── database.py  # Database connection & session
├── models.py    # SQLAlchemy models
├── schemas.py   # Request/response schemas
├── crud.py      # Database operations
└── tests/       # Minimal automated tests
```

---

## 🔌 API Endpoints (Overview)

### Issues
- `POST /issues` — Create issue
- `GET /issues` — List issues (filters + pagination)
- `GET /issues/{id}` — Get issue with comments & labels
- `PATCH /issues/{id}` — Update issue with version check
- `POST /issues/bulk-status` — Transactional bulk update
- `POST /issues/import` — CSV issue import

### Comments
- `POST /issues/{id}/comments` — Add comment

### Labels
- `PUT /issues/{id}/labels` — Replace labels atomically

### Reports
- `GET /reports/top-assignees`
- `GET /reports/latency`

---

## 🧪 Testing

Automated tests are written using pytest and focus on:
- optimistic concurrency conflicts
- transactional rollback behavior
- CSV validation correctness

The test suite prioritizes correctness over coverage.

---

## 🏁 Setup Instructions

1. Clone the repository
2. Create a virtual environment and install dependencies
3. Configure PostgreSQL connection
4. Run database migrations using Alembic
5. Start the FastAPI server

Detailed setup steps are provided in comments and configuration files.

---

## 📌 Notes

- This project is intentionally backend-only.
- Authentication is simplified to focus on data correctness.
- Code emphasizes readability and explainability over advanced abstractions.

---

## 👤 Author

**Pratik**  
Backend Intern Assignment
