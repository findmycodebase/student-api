# Student Management API

A RESTful Student Management API built with FastAPI as part of my backend development journey. This project is being developed incrementally to learn modern backend development concepts and best practices.

## Project Goals

This project is designed to demonstrate practical backend development skills including:

- REST API development with FastAPI
- Request validation
- Database integration
- Authentication and authorization
- Testing
- Deployment
- Software engineering best practices

## Tech Stack

- Python
- FastAPI
- Uvicorn

## Current Features

### General Endpoints

- GET `/`
- GET `/about`

### Student Endpoints

- GET `/student/{name}`
- GET `/student/{name}/{age}`

## Features Planned

- Query Parameters
- POST Endpoints
- Request Validation with Pydantic
- SQLite Database
- SQLAlchemy ORM
- CRUD Operations
- Authentication with JWT
- Password Hashing
- Protected Routes
- Testing with Pytest
- Deployment

## Installation

```bash
git clone https://github.com/findmycodebase/student-api.git

cd student-api

python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m uvicorn app:app --reload
```

Open the API documentation:

```
http://127.0.0.1:8000/docs
```

## Project Structure

```
student-api/
│── app.py
│── requirements.txt
│── database.py
│── models.py
│── schemas.py
│── crud.py
│── .gitignore
└── README.md
```

## Learning Journey

This repository is being built progressively while learning backend development. New features and improvements will be added as more backend concepts are covered.

## Author

**Rejoice Oyebode**

GitHub: https://github.com/findmycodebase
