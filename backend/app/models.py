from enum import Enum
from app.database import Base
from sqlalchemy import Column, DateTime, Integer, String, Enum 

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False, index=True)
    description = Column(String)
    status = Column(String, default="pending", nullable=False, index=True)
    due_datetime = Column(DateTime, index=True, nullable=False)
