# 📝 Task Manager API (FastAPI + MySQL)

A simple and fully functional CRUD API for managing users and their tasks using **FastAPI**, **SQLAlchemy**, and **MySQL**.

---

## 🚀 Features

- Create, Read, Update, and Delete (CRUD) users and tasks
- MySQL backend for data persistence
- RESTful endpoints with automatic documentation via Swagger UI
- Relational database with 1-to-many relationship (User → Tasks)

---

## 📁 Project Structure

DATABASE/
│
├── main.py # FastAPI application (API logic)
├── models.py # SQLAlchemy ORM models (User, Task)
├── database.py # DB connection and session setup
├── schemas.py # Pydantic schemas for request/response
├── requirements.txt # Dependencies (optional)
└── README.md # You're here!


---

## 🧠 Database Schema (ERD)

Each Task belongs to a User. A User can have many Tasks.

---

## ⚙️ How to Set Up and Run Locally

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/task-manager-api.git
cd task-manager-api

python -m venv venv
.\venv\Scripts\activate    # On Windows
# source venv/bin/activate # On Mac/Linux

pip install fastapi uvicorn pymysql sqlalchemy
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:123456789@localhost/taskdb"
uvicorn main:app --reload


---

