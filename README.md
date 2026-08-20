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

This repository documents my **8-week Python Backend Development Internship**, where I learned backend development by building a complete backend management system using **FastAPI**.

What started as small isolated endpoints in Week 1 grew into a fully authenticated, database-backed REST API with proper validation, ownership-based access control, and a clean layered architecture — the project below reflects that final state.

---

# ✨ Features

- 📦 REST API built with FastAPI, covering products, features, and users
- ✅ Full CRUD (Create, Read, Update, Delete) on every resource
- 🗂️ Layered architecture — routers, a dedicated CRUD/data-access layer, and Pydantic schemas
- 🗄️ MySQL database integration via SQLAlchemy
- 🔑 User registration and login
- 🔒 Password hashing with Passlib + Bcrypt
- 🎫 JWT-based authentication with OAuth2PasswordBearer
- 🛡️ Protected routes via reusable dependency injection
- 👤 Ownership-based authorization — users can only update or delete records they created
- 🧪 Request validation on every input (length limits, positive prices, non-negative stock, password strength, etc.)
- 📤 Typed response models — API responses are documented and filtered, never leaking unintended fields
- ⚙️ Environment-based configuration via `.env` — no secrets committed to the repo
- 🧭 Auto-generated interactive API docs at `/docs`

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
| Configuration | python-dotenv |
| ASGI Server | Uvicorn |
| Package Manager | uv |
| Version Control | Git |
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
├── .env                 # not committed — see setup below
├── .gitignore
├── .python-version
├── LICENSE
├── pyproject.toml
├── README.md
└── uv.lock
```

---

# ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/saboor-h5/devsphere-python-backend-internship.git

cd devsphere-python-backend-internship
```

### 2. Create a virtual environment

```bash
uv venv
```

Activate it:

**Windows**
```bash
source .venv/Scripts/activate
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
uv sync
```

### 4. Set up your database

Create a MySQL database (any name works, just match it in `.env` below):

```sql
CREATE DATABASE devsphere;
```

### 5. Configure environment variables

Create a `.env` file in the project root with the following keys:

```env
DB_USERNAME=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_NAME=devsphere

SECRET_KEY=your_random_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Generate a secure `SECRET_KEY` rather than typing one by hand:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### 6. Run the server

```bash
uv run uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive, browsable API docs (recommended starting point):

```text
http://127.0.0.1:8000/docs
```

---

# 🏗️ Architecture

The codebase follows a simple, MVC-inspired layered structure:

- **`routers/`** — the HTTP layer. Handles requests, status codes, and authentication checks — no raw SQL lives here.
- **`crud/`** — the data-access layer. Contains all database queries for each resource, with no knowledge of HTTP.
- **`schemas.py`** — Pydantic models defining both incoming request validation and outgoing response shapes.

Each layer has one job, which keeps the routers short and easy to follow even as the project grows.

---

# 🔐 Authentication & Authorization

- Passwords are hashed with **Passlib + Bcrypt** before storage — plain-text passwords are never saved or returned.
- Logging in returns a **JWT access token**, which encodes the user's id and username.
- Protected endpoints require this token in the `Authorization: Bearer <token>` header.
- Beyond authentication, most write operations use **ownership-based authorization**: a user can only update or delete the products/features *they* created. Attempting to modify someone else's record returns `403 Forbidden`; a record that doesn't exist at all returns `404 Not Found`.

---

# 🔗 API Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|:---------------:|
| GET | `/` | Server health check | No |
| GET | `/about` | Information about the backend | No |
| GET | `/profile` | Retrieve the authenticated user's profile | Yes |
| GET | `/features` | Retrieve all features | No |
| GET | `/features/{id}` | Retrieve a single feature by ID | No |
| POST | `/features` | Add a new feature | Yes |
| PUT | `/features/{id}` | Update a feature (creator only) | Yes |
| DELETE | `/features/{id}` | Delete a feature (creator only) | Yes |
| GET | `/products` | Retrieve all products | No |
| GET | `/products/{id}` | Retrieve a single product by ID | No |
| POST | `/products` | Add a new product | Yes |
| PUT | `/products/{id}` | Update a product (creator only) | Yes |
| DELETE | `/products/{id}` | Delete a product (creator only) | Yes |
| POST | `/users/register` | Register a new user | No |
| POST | `/users/login` | Authenticate and receive a JWT access token | No |
| GET | `/users/{id}` | Retrieve a user's profile by ID | Yes |
| PUT | `/users/{id}` | Update a user's name details | Yes |
| DELETE | `/users/{id}` | Delete a user | Yes |

For exact request/response bodies, use the interactive docs at `/docs` — they're generated directly from the schemas and always match the running code.

---

# 📦 Sample Responses

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
    "quantity": 25,
    "created_by": 2
}
```

### PUT /products/{id} — by a non-owner

```json
{
    "detail": "You do not have permission to update this product."
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

### Validation error (e.g. negative price)

```json
{
    "detail": [
        {
            "type": "greater_than",
            "loc": ["body", "price"],
            "msg": "Input should be greater than 0"
        }
    ]
}
```

---

# 📅 Internship Progress

- ✅ Week 1 — FastAPI setup, GET endpoints, middleware, browser & Postman testing
- ✅ Week 2 — REST APIs, JSON handling, Pydantic models, modular routing, GET & POST endpoints
- ✅ Week 3 — MySQL setup, SQLAlchemy integration, database connectivity, Insert & Read operations
- ✅ Week 4 — User registration & login, password hashing, JWT authentication, protected routes, dependency injection
- ✅ Week 5 — Full CRUD across all resources, MVC-style restructure with a `crud/` layer and consolidated `schemas.py`
- ✅ Week 6 — Final backend management system: environment-based configuration, full input validation, ownership-based authorization linking products/features to their creator, and typed response models across the API

---

# 🚀 Possible Next Steps

Ideas for extending this project further:

- SQLAlchemy ORM instead of raw SQL
- Pagination on list endpoints
- Centralized/global exception handling
- Automated tests with pytest
- Dockerized setup
- Deployment to a live host

---

# 👨‍💻 Author

**Saboor Hussain**

- GitHub: https://github.com/saboor-h5
- LinkedIn: https://www.linkedin.com/in/saboor-h5

---

> Built as part of my DevSphere Python Backend Development Internship — an 8-week journey from a single FastAPI endpoint to a fully authenticated, validated, and access-controlled backend system.