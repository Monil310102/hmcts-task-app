from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class StatusOptions(str, Enum):
    pending = "pending"
    inprogress = "inprogress"
    completed = "completed"

#Create task request schema
class CreateTask(BaseModel):
    title: str
    description: str | None = None
    status: StatusOptions = StatusOptions.pending
    due_datetime: datetime

#Create task response schema
class CreateTaskResponse(CreateTask):
    id: int

    class Config:
        orm_mode = True