<div align="center">

# 🐍 DevSphere Python Backend Internship Journey

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

Rather than serving as a finished project, this repository captures my learning journey week by week. Each task introduces new backend development concepts that are implemented, tested, documented, and version-controlled using professional development practices.

---

# ✨ Features

Current implementation includes:

- ⚡ FastAPI application setup
- 🌐 GET endpoints (`/`, `/about`, `/features`)
- 📤 POST endpoint for accepting JSON data
- ✅ Request validation using Pydantic models
- 📁 Modular project structure using routers and models
- 🔄 Custom HTTP middleware for request logging
- 🧪 API testing with Postman
- 📚 Interactive API documentation using Swagger UI (`/docs`)

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

# 🔗 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Server health check |
| GET | `/about` | Information about the backend |
| GET | `/features` | Retrieve all available features |
| POST | `/features` | Create a new feature |
| GET | `/docs` | Interactive Swagger API documentation |

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

### GET /features

```json
[
  {
    "id": 1,
    "title": "Fast Performance",
    "description": "High-speed backend APIs."
  },
  {
    "id": 2,
    "title": "Responsive Design",
    "description": "Works on all devices."
  },
  {
    "id": 3,
    "title": "Easy Integration",
    "description": "Simple REST API integration."
  }
]
```

### POST /features

Request

```json
{
  "title": "Secure",
  "description": "Built with security best practices."
}
```

Response

```json
{
  "message": "Feature added successfully.",
  "feature": {
    "title": "Secure",
    "description": "Built with security best practices."
  }
}
```

---

# 📅 Internship Progress

- [x] **Week 1** — FastAPI setup, GET endpoints, middleware, browser & Postman testing
- [x] **Week 2** — REST APIs, JSON handling, Pydantic models, modular routing, GET & POST endpoints
- [ ] Week 3
- [ ] Week 4
- [ ] Week 5
- [ ] Week 6
- [ ] Week 7
- [ ] Week 8

---

# 🗺️ Roadmap

Future topics planned during this internship include:

- CRUD operations
- Request and response models
- Database integration (SQLite/PostgreSQL)
- SQLAlchemy ORM
- Authentication & Authorization
- JWT Authentication
- Environment variables
- Automated testing with pytest
- Docker
- Deployment

---

# 👨‍💻 Author

**Saboor Hussain**

- GitHub: **https://github.com/saboor-h5**
- LinkedIn: **https://www.linkedin.com/in/saboor-h5**

---

> 📚 This repository is continuously updated throughout my DevSphere Python Backend Development Internship to document both my learning progress and practical backend development experience.