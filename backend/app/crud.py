from sqlalchemy.orm import Session
from app import models, schemas


def create_task(db: Session, task: schemas.CreateTask) -> models.Task:
    db_task = models.Task(
        title=task.title,
        description=task.description,
        status=task.status.value,
        due_datetime=task.due_datetime
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task