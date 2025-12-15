from app.models.base_model import BaseModel
from sqlalchemy import Column, String, Float, DateTime, Integer,Boolean
import datetime

class Task(BaseModel):
    __tablename__ = "tasks"
    id: int = Column(Integer, primary_key=True, index=True)
    title: str = Column(String, index=True)
    description: str = Column(String, index=True)
    status: float = Column(Integer, index=True)

    is_deleted = Column(Boolean, default=False, index=True)
    deleted_at = Column(DateTime, nullable=True)
