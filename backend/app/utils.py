from datetime import datetime, timezone
from fastapi import HTTPException

def validate_due_datetime(due_datetime: datetime):
    now = datetime.now(timezone.utc)
    if due_datetime.astimezone(timezone.utc) < now:
        raise HTTPException(status_code=400, detail="ERROR: due_datetime must be in the future")
    return due_datetime