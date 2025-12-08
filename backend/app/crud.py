from sqlalchemy.orm import Session
from backend.app import models, schemas


def create_task(db: Session, task: schemas.CreateTask) -> models.Task:
    db_task = models.Task(**task.dimodelct())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task