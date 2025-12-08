# HMCTS Task Management System

A simple task management system for HMCTS caseworkers.
This project includes a **backend API** for task creation and a **frontend React application** to interact with the API.

---

## Table of Contents

* [Project Overview](#project-overview)
* [Features](#features)
* [Tech Stack](#tech-stack)
* [Setup and Installation](#setup-and-installation)
* [Running the Backend API](#running-the-backend-api)
* [Frontend Integration](#frontend-integration)
* [API Endpoints](#api-endpoints)
* [Validation](#validation)
* [Testing](#testing)
* [Folder Structure](#folder-structure)
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

---

## Features

* Create tasks via a backend API
* Input validation using **Pydantic**
* Database interactions with **SQLAlchemy**
* Proper error handling for invalid inputs and database errors
* Frontend **Task Form** with user input for task creation and success/error messages
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
* **React** – Frontend
* **JavaScript** – Frontend scripting
* **CSS** – Frontend styling

---

## Setup and Installation

1. **Clone the repository:**

```bash
git clone <your-repo-url>
cd hmcts-task-app
```

2. **Backend setup:**

```bash
cd backend
python -m venv myenv
# Activate virtual environment
# Windows:
myenv\Scripts\activate
# Mac/Linux:
source myenv/bin/activate
pip install -r requirements.txt
```

3. **Frontend setup:**

```bash
cd ../frontend
npm install
```

---

## Running the Backend API

1. Navigate to the backend folder and activate virtual environment (if not already):

```bash
cd backend
# activate virtual environment again if needed
```

2. Run the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The backend will run at: `http://127.0.0.1:8000`

---

## Frontend Integration

1. Navigate to the frontend folder:

```bash
cd frontend
```

2. Start the React app:

```bash
npm start
```

The frontend will run at: `http://localhost:3000`

3. Open your browser, access the frontend, and create a task using the form. You should see success/error messages with task details.

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

### Backend

Run pytest to test backend functionality:

```bash
cd backend
pytest -v tests
```

Tests include:

* Successful task creation
* Validation of future `due_datetime`
* Response schema verification

### Frontend

* Fill out the form and verify tasks are created.
* Ensure success/error messages display correctly.
* Check browser console for any runtime errors.

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
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   └─ TaskForm.jsx
│   │   │   └─ TaskForm.css
│   │   ├─ api.js
│   │   ├─ App.jsx
│   │   ├─ index.js
│
└── README.md                # This file
```