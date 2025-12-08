from datetime import datetime
from fastapi import HTTPException

def validate_due_datetime(due_datetime: datetime):
    if due_datetime < datetime.now():
        raise HTTPException(status_code=400, detail="due_datetime must be in the future")
    return due_datetime