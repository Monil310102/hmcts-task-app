from fastapi import APIRouter, Depends   
from sqlalchemy.orm import Session
from backend.app import crud, schemas
from backend.app.database import get_db
from backend.app.utils import validate_due_datetime

router = APIRouter()

@router.post("/tasks/")
def create_task(task: schemas.CreateTask, db: Session = Depends(get_db)):
    
    validate_due_datetime(task.due_datetime)

    return crud.create_task(db=db, task=task)