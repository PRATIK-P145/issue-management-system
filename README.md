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

The project intentionally avoids overengineering and advanced patterns in favor of clarity and correctness.

---

## 🧠 Key Design Decisions

### Optimistic Concurrency Control
Each issue includes a `version` field.  
Updates succeed only if the client-provided version matches the current database version.  
This prevents silent overwrites when multiple users update the same issue concurrently.

### Transactions
Multi-step operations (bulk updates, label replacement) are wrapped in database transactions to ensure:
- all changes succeed together, or
- all changes are rolled back on failure

### CSV Import Strategy
- Each row is validated independently
- Invalid rows do not stop the entire import
- A summary response reports success and failure counts with reasons

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
