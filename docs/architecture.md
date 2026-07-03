# Home Network Monitor – Architecture

## Overview

The Home Network Monitor is a production-oriented application designed to monitor devices and services on a home network.

The project is intentionally built using enterprise software engineering practices, emphasizing maintainability, security, scalability, and testability over rapid development.

---

# Technology Stack

## Backend

* Python 3.14
* FastAPI
* PyMongo
* Pydantic Settings
* psutil
* Docker SDK
* WebSockets

## Frontend

* React
* TypeScript
* Tailwind CSS

## Database

* MongoDB

## Infrastructure

* Docker Compose
* Jenkins (planned)
* GitHub Flow
* Conventional Commits

---

# Project Structure

```text
backend/
    app/
        api/
        core/
        db/
        middleware/
        models/
        repositories/
        schemas/
        security/
        services/
        utils/
        websocket/
        workers/
        main.py

frontend/

infrastructure/

docs/

scripts/
```

---

# Current Backend Architecture

```text
FastAPI
    │
    ▼
Dependencies
    │
    ▼
Repositories
    │
    ▼
MongoDB Manager
    │
    ▼
MongoDB
```

---

# Database Layer

The application uses a single MongoDB client for the lifetime of the application.

Responsibilities of the database layer:

* Create the MongoDB client during application startup.
* Verify database connectivity.
* Expose a single configured database instance.
* Close the client gracefully during application shutdown.

Repositories never create MongoDB clients directly.

---

# Dependency Injection

Database access is exposed through a dependency function.

This prevents repositories from depending directly on the MongoDB manager and improves testability.

---

# Repository Layer

Repositories encapsulate all database operations.

The goal is to keep MongoDB-specific code isolated from business logic.

A shared `BaseRepository` provides common functionality, while domain repositories implement application-specific queries.

---

# Quality Gates

Every milestone must successfully pass:

* Ruff
* MyPy
* Pytest

before committing.

---

# Git Workflow

Development follows GitHub Flow.

* `develop`
* feature branches
* Pull Requests
* Conventional Commits

---

# Future Architecture

Planned components include:

* Service layer
* Authentication
* WebSocket event streaming
* Background workers
* Device discovery
* Docker monitoring
* Security hardening
* CI/CD pipeline
* Nginx reverse proxy
* Monitoring and observability
