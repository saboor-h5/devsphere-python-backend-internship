<div align="center">

# 🐍 DevSphere Python Backend Internship

### Documenting my 8-week Python Backend Development internship using FastAPI.

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI_Server-4051B5?style=for-the-badge)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
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
- ✅ Request validation using Pydantic models
- 🗂️ Modular project structure using routers and models
- 🗄️ MySQL database integration
- ⚙️ Database operations using SQLAlchemy
- 🧪 API testing with Postman

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
│   ├── models.py
│   └── routers/
│       ├── __init__.py
│       └── features.py
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
- Retrieve stored records

---

# 🔗 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Server health check |
| GET | `/about` | Information about the backend |
| GET | `/features` | Retrieve all features from the database |
| POST | `/features` | Add a new feature to the database |

---

# 📦 Sample Responses

### GET /

```json
{
    "message": "Server Running"
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
    "feature": {
        "title": "Database Connected",
        "description": "Week 3 completed."
    }
}
```

---

# 📅 Internship Progress

- ✅ Week 1 — FastAPI setup, GET endpoints, middleware, browser & Postman testing
- ✅ Week 2 — REST APIs, JSON handling, Pydantic models, modular routing, GET & POST endpoints
- ✅ Week 3 — MySQL setup, SQLAlchemy integration, database connectivity, Insert & Read operations
- ⬜ Week 4
- ⬜ Week 5
- ⬜ Week 6
- ⬜ Week 7
- ⬜ Week 8

---

# 🚀 Planned Learning

As the internship continues, I plan to explore:

- PUT, PATCH and DELETE operations
- CRUD APIs
- SQLAlchemy ORM
- Authentication and Authorization
- JWT Authentication
- Environment variables
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