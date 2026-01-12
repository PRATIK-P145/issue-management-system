

# Issue Tracker API

A backend service for managing issues with a strong focus on **data consistency, concurrency safety, and clean API design**.

---

## 🌐 Live Deployment

**IssueOps** — a concurrency-safe issue management API focused on **correctness**, **versioned updates**, and **clean backend architecture**.

🔗 **Live API Base URL:** `https://issueops.onrender.com`

 **Interactive API Docs (Swagger UI):** 
 ```
 https://issueops.onrender.com/docs
 ```

> The deployed API mirrors the local setup, including optimistic concurrency control, audit fields, and strict validation. Designed for reliability under concurrent usage.

---
## Contents

- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Implemented Features](#implemented-features)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Project Setup](#project-setup)
- [Pending / Future Work](#pending--future-work)
- [Evaluation Alignment](#evaluation-alignment)
- [Author](#author)

---


## Key  Features

### 1. Optimistic Concurrency Control

Used a `version` field on the Issue model.

* Clients must send the latest version when updating
* If the version does not match the database value:

  * Update is rejected with **409 Conflict**
* Prevents silent overwrites during concurrent edits

---

### 2. Clean API Design

* PATCH supports **partial updates only**
* No accidental overwrites
* Clear separation between request models and DB models


---

### 3. Auditability

* `created_at` and `updated_at` tracked automatically
* `updated_at` changes only when meaningful updates occur

---

### 4.Schema Evolution & Migrations

As project requirements evolve, the database schema needs to change without breaking existing data or deployments.

**API endpoints / tasks where it appears:**

* Adding fields like `created_at`, `priority`, `assigned_to`
* Supporting filters, sorting, and reporting features

**My strategy to handle it:**
All schema changes are managed using **Alembic migrations**, enabling versioned, incremental, and reversible updates. This allows the database structure to evolve safely while maintaining compatibility across environments.

---
##  Tech Stack

- **Backend Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy (minimal usage)
- **Migrations**: Alembic
- **Testing**: pytest

“PostgreSQL is hosted on Supabase for ease of development; all schema management, transactions, and business logic are implemented in the FastAPI backend.”


---

##  Implemented Features (Completed)

### Issue Management

* Create, retrieve, list, and **hard delete** issues
* List issues with **pagination** and **status/priority filters**
* Audit fields: `created_at`, `updated_at` (auto-updated on PATCH)

### Safe Updates (Concurrency Control)

* `PATCH /issues/{id}` supports **partial updates**
* **Optimistic locking** via `version` field
* Returns **409 Conflict** on version mismatch
* Prevents lost updates in concurrent requests

### Data Integrity & Validation

* Validates `assigned_to` user existence
* Clear error handling (`400`, `404`, `409`)
* Strong request/response validation using Pydantic

### Code Structure & Quality

* Clean separation of concerns:

  * `main.py` → routing
  * `crud.py` → database logic
  * `schemas.py` → validation
* Minimal, readable SQLAlchemy usage

---

## Project Structure

```
app/
├── main.py       # FastAPI routes
├── database.py   # DB session & engine
├── models.py     # SQLAlchemy models
├── schemas.py    # Pydantic schemas
├── crud.py       # Database operations
└── tests/        # (minimal tests)
```

---

##  API Endpoints (Current)

### Issues

* `POST /issues` — Create issue
* `GET /issues` — List issues (pagination + filters)
* `GET /issues/{id}` — Get issue by ID
* `PATCH /issues/{id}` — Partial update with version check
* `DELETE /issues/{id}` — Hard delete issue

---



## Project Setup

### Prerequisites

* Python **3.10+**
* PostgreSQL
* Git
* Virtual environment tool (`venv`)

---

### 1️⃣ Clone the Repository

```bash
git clone <repo-url>
cd issue-management-system
```

---

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv
```

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql+psycopg2://username:password@localhost:5432/issue_db
```

> PostgreSQL can be local or hosted (e.g., Supabase).

---

### 5️⃣ Run Database Migrations

```bash
alembic upgrade head
```

This creates all required tables and schema.

---

### 6️⃣ Start the Server

```bash
uvicorn app.main:app --reload
```

API will be available at:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

### 7️⃣ Run Tests (Optional but Recommended)

```bash
pytest
```

---

### Notes 

* All schema changes are managed via **Alembic**
* No manual DB setup required beyond configuring `DATABASE_URL`
* API is intentionally backend-only to focus on correctness and concurrency

---

##  Pending / Future Work

The following endpoints were **intentionally left out due to time constraints**, but the project structure fully supports adding them cleanly:

### Planned Endpoints

* `GET /issues/{id}` — Include comments & labels
* `POST /issues/{id}/comments` — Add comments
* `PUT /issues/{id}/labels` — Atomic label replacement
* `POST /issues/bulk-status` — Transactional bulk updates
* `POST /issues/import` — CSV issue import
* `GET /reports/top-assignees` — Aggregated report
* `GET /reports/latency` — Average resolution time

### Why These Are Deferred

* Priority was given to:

  * Correct PATCH semantics
  * Concurrency handling
  * Code structure & correctness
* All deferred features require **transactions and aggregation**, which can be added incrementally without refactoring core logic



---


##  Notes 

* Authentication is intentionally omitted to focus on **data correctness**
* The project emphasizes:

  * Concurrency safety
  * Clean update semantics
  * Real-world backend patterns
---


###  Evaluation Alignment

**API Correctness**

* Full CRUD for issues
* Filtering + pagination on list endpoint
* Proper HTTP methods and status codes

**Concurrency & Transactions**

* Optimistic locking using `version` field
* PATCH rejects stale updates with `409 Conflict`
* Prevents lost updates under concurrent clients

**Code Structure & Clarity**

* Clear separation: routing, schemas, DB logic
* Minimal ORM usage for readability
* Predictable project layout

**Error Handling & Validation**

* Validation of foreign keys (`assigned_to`)
* Consistent `400 / 404 / 409` responses
* No silent failures

**Tests & Documentation**

* Focused pytest cases for concurrency & integrity
* Clear setup and API documentation in README


---

##  Author

**PRATIK PATIL**

Backend Intern Assignment

---
