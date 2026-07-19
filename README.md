# IssueForge API

A production-style Issue Tracking REST API built with **FastAPI**, following Clean Architecture principles and modern backend development practices.

This project demonstrates how to build a scalable backend using dependency injection, layered architecture, SQLAlchemy, Alembic, middleware, structured logging, and production-ready exception handling.

---

## Features

- RESTful CRUD APIs
- FastAPI Dependency Injection
- Layered (Clean) Architecture
- SQLAlchemy ORM
- Alembic Database Migrations
- Custom Exception Handling
- Structured Logging Middleware
- Request Validation with Pydantic
- Application Lifespan Events
- Environment-based Configuration
- API Versioning
- Interactive API Documentation (Swagger & ReDoc)

---

## Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.12+ |
| Framework | FastAPI |
| ORM | SQLAlchemy |
| Database | PostgreSQL / SQLite |
| Migrations | Alembic |
| Validation | Pydantic v2 |
| ASGI Server | Uvicorn |
| Configuration | python-dotenv |
| Testing | Pytest |

---

# Project Structure

```text
issueforge-api/
│
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── routers/
│   │       └── __init__.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   └── logging.py
│   │
│   ├── db/
│   │   ├── database.py
│   │   ├── session.py
│   │   └── base.py
│   │
│   ├── dependencies/
│   │
│   ├── middleware/
│   │
│   ├── models/
│   │
│   ├── repositories/
│   │
│   ├── schemas/
│   │
│   ├── services/
│   │
│   ├── exceptions/
│   │
│   ├── context/
│   │
│   └── main.py
│
├── alembic/
├── tests/
├── .env.example
├── alembic.ini
├── requirements.txt
└── README.md
```

---

# Architecture

```text
                HTTP Request
                     │
                     ▼
              FastAPI Router
                     │
                     ▼
             Dependency Injection
                     │
                     ▼
              Service Layer
                     │
                     ▼
            Repository Layer
                     │
                     ▼
               SQLAlchemy ORM
                     │
                     ▼
                 Database
```

---

# Implemented Features

## API

- Create Project
- Get Project
- Update Project
- Delete Project
- List Projects
- Health Check Endpoint

## Backend

- Dependency Injection
- Repository Pattern
- Service Layer
- Configuration Management
- Environment Variables
- Exception Handlers
- Logging Middleware
- Application Lifespan
- Database Session Management

---

# Getting Started

## Clone Repository

```bash
git clone https://github.com/ajinkyad015/issueforge-api.git

cd issueforge-api
```

---

## Create Virtual Environment

### Linux / macOS

```bash
python -m venv .venv

source .venv/bin/activate
```

### Windows

```powershell
python -m venv .venv

.venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file.

Example:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/issueforge

APP_NAME=IssueForge API

DEBUG=True
```

---

## Run Database Migrations

```bash
alembic upgrade head
```

---

## Start the Application

```bash
uvicorn app.main:app --reload
```

Server runs at

```
http://localhost:8000
```

---

# API Documentation

Swagger UI

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

# Engineering Concepts Demonstrated

- Clean Architecture
- REST API Design
- Dependency Injection
- Repository Pattern
- Service Layer
- SQLAlchemy ORM
- Database Migrations
- Middleware
- Structured Logging
- Pydantic Validation
- Custom Exception Handling
- Environment Configuration
- Application Lifespan Management

---

# Future Improvements

- JWT Authentication
- Role-based Authorization
- Docker Support
- Redis Caching
- Async SQLAlchemy
- Background Tasks
- Rate Limiting
- Pagination & Filtering
- CI/CD Pipeline
- Unit & Integration Tests

---

# Example API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/health` | Health Check |
| GET | `/api/v1/projects` | List Projects |
| POST | `/api/v1/projects` | Create Project |
| GET | `/api/v1/projects/{id}` | Get Project |
| PUT | `/api/v1/projects/{id}` | Update Project |
| DELETE | `/api/v1/projects/{id}` | Delete Project |

---

# Why This Project?

This project was built to demonstrate production-ready backend development practices using FastAPI. It focuses on writing maintainable, scalable, and testable code by separating concerns into routers, services, repositories, and database layers while following modern Python best practices.

---

# License

This project is licensed under the MIT License.
