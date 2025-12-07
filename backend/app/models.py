from enum import Enum
from backend.app.database import Base
from sqlalchemy import Column, DateTime, Integer, String, Enum 


class StatusOptions(Enum):
    pending = "pending"
    inprogress = "inprogress"
    completed = "completed"


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False, index=True)
    description = Column(String)
    status = Column(Enum(StatusOptions), default=StatusOptions.pending, nullable=False, index=True)
    due_datetime = Column(DateTime, index=True, nullable=False)
