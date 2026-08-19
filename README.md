<div align="center">

# 🐍 DevSphere Python Backend Internship

### Documenting my 8-week Python Backend Development internship using FastAPI.

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI_Server-4051B5?style=for-the-badge)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-Auth-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)

</div>

---

# 📖 About

This repository documents my **8-week Python Backend Development Internship**, where I am learning backend development by building practical applications using **FastAPI**.

The purpose of this repository is to track my progress, apply software engineering best practices, and build a portfolio of backend development projects throughout the internship.

---

# ✨ Features

- 📦 REST API development using FastAPI
- 📥 GET endpoints for retrieving data
- 📤 POST endpoints for accepting JSON requests
- ✏️ PUT endpoints for updating existing records
- 🗑️ DELETE endpoints for removing records
- ✅ Request validation using Pydantic models
- 🗂️ Modular project structure using routers, schemas, and a CRUD (data-access) layer
- 🗄️ MySQL database integration
- ⚙️ Database operations using SQLAlchemy
- 🧪 API testing with Postman
- 👤 User registration
- 🔑 User login
- 🔒 Password hashing using Passlib + Bcrypt
- 🎫 JWT access token generation and verification
- 🛡️ Protected routes using OAuth2PasswordBearer
- 🧩 Dependency injection for reusable authentication logic
- 🏗️ MVC-style architecture separating routing, business logic, and data validation

---

# 🎯 Learning Objectives

Throughout this internship, I aim to:

- Learn Python backend development
- Build RESTful APIs using FastAPI
- Understand backend architecture and request handling
- Integrate relational databases with backend applications
- Write clean, maintainable Python code
- Practice Git and GitHub workflows
- Learn API testing with Postman
- Develop portfolio-quality backend projects

---

# 🛠️ Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python 3.12 |
| Framework | FastAPI |
| Validation | Pydantic |
| Database | MySQL |
| Database Toolkit | SQLAlchemy |
| Database Driver | PyMySQL |
| Password Hashing | Passlib + Bcrypt |
| Token Handling | Python-Jose |
| Authentication Scheme | OAuth2PasswordBearer |
| ASGI Server | Uvicorn |
| Package Manager | uv |
| Version Control | Git |
| Repository Hosting | GitHub |
| API Testing | Postman |

---

# 📂 Project Structure

```text
devsphere-python-backend-internship/
│
├── .venv/
├── app/
│   ├── __init__.py
│   ├── database.py
│   ├── main.py
│   ├── schemas.py
│   ├── security.py
│   ├── jwt_handler.py
│   ├── dependencies.py
│   ├── crud/
│   │   ├── __init__.py
│   │   ├── products.py
│   │   ├── features.py
│   │   └── users.py
│   └── routers/
│       ├── __init__.py
│       ├── features.py
│       ├── products.py
│       └── users.py
│
├── .gitignore
├── .python-version
├── LICENSE
├── pyproject.toml
├── README.md
└── uv.lock
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/saboor-h5/devsphere-python-backend-internship.git

cd devsphere-python-backend-internship
```

Create a virtual environment:

```bash
uv venv
```

Activate it:

### Windows

```bash
source .venv/Scripts/activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

Install project dependencies:

```bash
uv sync
```

---

# ▶️ Running the Project

Start the FastAPI development server:

```bash
uv run uvicorn app.main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 🗄️ Database

This project uses **MySQL** as the relational database.

Database connectivity is implemented using **SQLAlchemy** with the **PyMySQL** driver.

Current database operations include:

- Insert new records
- Retrieve stored records (single and multiple)
- Update existing records
- Delete records
- Store registered users with hashed passwords

---

# 🏗️ Architecture

As the project grew past simple GET/POST endpoints, the codebase was restructured into a clearer, MVC-inspired layout:

- **`routers/`** — the controller layer. Handles HTTP concerns only: request/response shapes, status codes, and raising the right exceptions.
- **`crud/`** — the model/data-access layer. Contains the actual SQL and database logic for each resource, with no knowledge of HTTP.
- **`schemas.py`** — Pydantic models defining the shape of request and response data, used for validation.

This keeps each layer focused on one responsibility and makes the routers easy to read at a glance.

---

# 🔐 Authentication

User authentication is implemented using **OAuth2** with **JWT (JSON Web Tokens)**.

- Passwords are hashed using **Passlib + Bcrypt** before being stored — plain-text passwords are never saved or returned in API responses.
- On successful login, the server issues a JWT access token.
- On failed login, the server returns a proper `401 Unauthorized` error.
- Protected routes require this token to be sent in the `Authorization` header and are validated using a reusable dependency before the request is processed.
- User profile routes (`GET`, `PUT`, `DELETE` on `/users/{id}`) are protected; product and feature reads remain public, with writes open for now and planned to be protected further in a later week.

---

# 🔗 API Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|:---------------:|
| GET | `/` | Server health check | No |
| GET | `/about` | Information about the backend | No |
| GET | `/profile` | Retrieve the authenticated user's profile | Yes |
| GET | `/features` | Retrieve all features | No |
| GET | `/features/{id}` | Retrieve a single feature by ID | No |
| POST | `/features` | Add a new feature | No |
| PUT | `/features/{id}` | Update an existing feature | No |
| DELETE | `/features/{id}` | Delete a feature | No |
| GET | `/products` | Retrieve all products | No |
| GET | `/products/{id}` | Retrieve a single product by ID | No |
| POST | `/products` | Add a new product | No |
| PUT | `/products/{id}` | Update an existing product | No |
| DELETE | `/products/{id}` | Delete a product | No |
| POST | `/users/register` | Register a new user with a hashed password | No |
| POST | `/users/login` | Authenticate a user and return a JWT access token | No |
| GET | `/users/{id}` | Retrieve a user's profile by ID | Yes |
| PUT | `/users/{id}` | Update a user's name details | Yes |
| DELETE | `/users/{id}` | Delete a user | Yes |

---

# 📦 Sample Responses

### GET /

```json
{
    "message": "Server Running!"
}
```

### GET /about

```json
{
    "message": "This backend server is built using FastAPI."
}
```

### POST /features

```json
{
    "message": "Feature added successfully.",
    "id": 4
}
```

### PUT /features/{id}

```json
{
    "message": "Feature updated successfully.",
    "id": 4
}
```

### DELETE /features/{id}

```json
{
    "message": "Feature deleted successfully.",
    "id": 4
}
```

### POST /products

```json
{
    "message": "Product created successfully!",
    "id": 7
}
```

### GET /products/{id}

```json
{
    "id": 7,
    "name": "Wireless Mouse",
    "description": "Ergonomic wireless mouse.",
    "price": 1500.0,
    "quantity": 25
}
```

### POST /users/register

```json
{
    "message": "User registered successfully",
    "id": 1,
    "username": "saboor"
}
```

### POST /users/login

```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "bearer"
}
```

### GET /users/{id}

```json
{
    "id": 1,
    "username": "saboor",
    "first_name": "Saboor",
    "last_name": "Hussain"
}
```

---

# 📅 Internship Progress

- ✅ Week 1 — FastAPI setup, GET endpoints, middleware, browser & Postman testing
- ✅ Week 2 — REST APIs, JSON handling, Pydantic models, modular routing, GET & POST endpoints
- ✅ Week 3 — MySQL setup, SQLAlchemy integration, database connectivity, Insert & Read operations
- ✅ Week 4 — User registration & login, password hashing with Passlib + Bcrypt, JWT authentication, protected routes, OAuth2PasswordBearer, dependency injection
- ✅ Week 5 — Full CRUD operations (GET, POST, PUT, DELETE) across products, features, and users; restructured project into an MVC-style layout with a dedicated `crud/` data-access layer and consolidated `schemas.py`; fixed login to return proper `401` on invalid credentials; secured user profile endpoints with JWT authentication
- ⬜ Week 6
- ⬜ Week 7
- ⬜ Week 8

---

# 🚀 Planned Learning

As the internship continues, I plan to explore:

- SQLAlchemy ORM
- Finer-grained authorization (e.g. users only editing their own resources)
- Environment variables for secrets and config
- Automated testing with pytest
- Docker
- Deployment

---

# 👨‍💻 Author

**Saboor Hussain**

- GitHub: https://github.com/saboor-h5
- LinkedIn: https://www.linkedin.com/in/saboor-h5

---

> This repository is maintained as part of my DevSphere Python Backend Development Internship and is updated weekly to document my learning journey and backend development progress.