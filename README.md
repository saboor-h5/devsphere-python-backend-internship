<div align="center">

# 🐍 DevSphere Python Backend Internship

### Documenting my 8-week Python Backend Development internship using FastAPI.

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI_Server-4051B5?style=for-the-badge)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)

</div>

---

# 📖 About

This repository documents my **8-week Python Backend Development Internship**, where I am learning backend development by building practical applications using **FastAPI**.

The purpose of this repository is to track my progress, apply software engineering best practices, and build a portfolio of backend development projects throughout the internship.

---

# 🎯 Learning Objectives

Throughout this internship, I aim to:

- Learn Python backend development
- Build RESTful APIs using FastAPI
- Understand backend architecture and request handling
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
│   └── main.py
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

# 🔗 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Returns server status |
| GET | `/about` | Returns information about the backend application |

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

---

# 📅 Internship Progress

## ✅ Week 1 Completed

Implemented:

- FastAPI project setup using `uv`
- Virtual environment configuration
- Root (`/`) endpoint
- About (`/about`) endpoint
- HTTP middleware for request logging
- Browser testing
- Postman API testing
- GitHub repository setup and version control

Future weeks will introduce additional backend concepts and features as the internship progresses.

---

# 🚀 Planned Learning

As the internship continues, I plan to explore:

- Request and response models with Pydantic
- CRUD APIs
- Database integration (SQLite/PostgreSQL)
- Authentication and Authorization
- JWT Authentication
- SQLAlchemy ORM
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

> This repository is maintained as part of my DevSphere Python Backend Development Internship and will be updated weekly as I progress through the program.