# HMCTS Task Management System

A simple task management system for HMCTS caseworkers.
This project includes a **backend API** for task creation and a **frontend application** to interact with the API.

---

## Table of Contents

* [Project Overview](#project-overview)
* [Features](#features)
* [Tech Stack](#tech-stack)
* [Setup and Installation](#setup-and-installation)
* [Running the Backend API](#running-the-backend-api)
* [API Endpoints](#api-endpoints)
* [Validation](#validation)
* [Testing](#testing)
* [Folder Structure](#folder-structure)
* [Frontend Integration](#frontend-integration)
* [Contributing](#contributing)
* [Future Enhancements](#future-enhancements)

---

## Project Overview

This project is a simple task management system where caseworkers can:

* Create tasks
* Validate task data before storing it
* Store tasks in a database for later retrieval

Currently, **only task creation** is implemented as per the technical test requirements.

Original task details can be found [here](https://github.com/hmcts/dts-developer-challenge-junior).

# HMCTS Task Management System

A simple task management system for HMCTS caseworkers.
This project includes a **backend API** for task creation and a **frontend application** to interact with the API.

---

## Table of Contents

* [Project Overview](#project-overview)
* [Features](#features)
* [Tech Stack](#tech-stack)
* [Setup and Installation](#setup-and-installation)
* [Running the Backend API](#running-the-backend-api)
* [API Endpoints](#api-endpoints)
* [Validation](#validation)
* [Testing](#testing)
* [Folder Structure](#folder-structure)

---

## Project Overview

This project is a simple task management system where caseworkers can:

* Create tasks
* Validate task data before storing it
* Store tasks in a database for later retrieval

Currently, **only task creation** is implemented as per the technical test requirements.

---

## Features

* Create tasks with fields:

  * `title` (required)
  * `description` (optional)
  * `status` (`pending`, `inprogress`, `completed`, default: `pending`)
  * `due_datetime` (must be in the future)
* Input validation using **Pydantic**
* Database interactions with **SQLAlchemy**
* Proper error handling for invalid inputs and database errors
* Unit tests with **pytest**
* Documentation via **Swagger UI**

---

## Tech Stack

* **Python 3.13** – Backend language
* **FastAPI** – Web framework
* **SQLAlchemy** – ORM for database operations
* **SQLite** – Database (local development)
* **Pydantic** – Data validation
* **Uvicorn** – ASGI server

---

## Setup and Installation

1. **Clone the repository:**

```bash
git clone <your-repo-url>
cd hmcts-task-app
```

2. **Create a virtual environment:**

```bash
python -m venv myenv
```

3. **Activate the virtual environment:**

```bash
# Windows
myenv\Scripts\activate
# Mac/Linux
source myenv/bin/activate
```

4. **Install dependencies:**

```bash
pip install -r backend/requirements.txt
```

---

## Running the Backend API

1. Navigate to the `backend/` folder:

```bash
cd backend
```

2. Run the FastAPI server:

```bash
uvicorn app.main:app --reload
```

3. Open the API documentation:

* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## API Endpoints

### **Create Task**

**URL:** `/tasks/`
**Method:** `POST`
**Request Body:**

```json
{
  "title": "Review case documents",
  "description": "Check for missing attachments",
  "status": "pending",
  "due_datetime": "2025-12-08T14:00:00Z"
}
```

**Response:**

```json
{
  "id": 1,
  "title": "Review case documents",
  "description": "Check for missing attachments",
  "status": "pending",
  "due_datetime": "2025-12-08T14:00:00Z"
}
```

---

## Validation

* `due_datetime` must be a future datetime
* `status` defaults to `pending` if not provided
* Title is required
* All datetime comparisons are **timezone-aware** to prevent errors

Validation logic is implemented in `backend/app/utils.py`.

---

## Testing

Unit tests are implemented with **pytest**.

To run tests:

```bash
cd backend
pytest -v tests
```

Tests include:

* Successful task creation
* Validation of future `due_datetime`
* Response schema verification

---

## Folder Structure

```
hmcts-task-app/
│
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── routes.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── crud.py
│   │   ├── utils.py
│   │   └── database.py
│   ├── tests/
│   │   └── test_tasks.py
│   └── requirements.txt
│
├── frontend/                # Frontend app (optional)
├── myenv/                   # Virtual environment
└── README.md                # This file
```
