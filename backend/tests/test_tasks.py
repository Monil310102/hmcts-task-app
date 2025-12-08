import pytest
from fastapi.testclient import TestClient
import datetime
from app.main import app
from app.database import engine, Base, SessionLocal

client = TestClient(app)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

def test_create_task_success():
    response = client.post(
        "/tasks/",
        json={
            "title": "Test Task",
            "description": "This is a test task",
            "status": "pending",
            "due_datetime": (datetime.datetime.now() + datetime.timedelta(days=1)).isoformat()
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["description"] == "This is a test task"
    assert data["status"] == "pending"

def test_create_task_past_due_datetime():
    response = client.post(
        "/tasks/",
        json={
            "title": "Past Task",
            "description": "This task has a past due date",
            "status": "pending",
            "due_datetime": (datetime.datetime.now() - datetime.timedelta(days=1)).isoformat()
        }
    )
    assert response.status_code == 400
    data = response.json()
    assert data["detail"] == "ERROR: due_datetime must be in the future"

def test_create_task_missing_title():
    response = client.post(
        "/tasks/",
        json={
            "description": "This task is missing a title",
            "status": "pending",
            "due_datetime": (datetime.datetime.now() + datetime.timedelta(days=1)).isoformat()
        }
    )
    assert response.status_code == 422  # Unprocessable Entity