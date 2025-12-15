from fastapi import APIRouter,HTTPException
from sqlalchemy.orm import Session
from app.db.base import get_db
from fastapi import Depends
from app.models.task_model import Task
from typing import List
from app.schemas.schemas import TaskBase, TaskResponse,TaskUpdate
from sqlalchemy import update,delete
from datetime import datetime
router = APIRouter()

@router.get("/tasks",)
async def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return tasks

@router.post("/tasks")
async def create_task():
    return {"message": "Task created"}

@router.put("/tasks/{task_id}",response_model=TaskResponse)
async def update_task(task_id:int,task:TaskUpdate,db:Session=Depends(get_db)):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    stml = update(Task).where(Task.id == task_id).values(
        title = task.title,
        description = task.description,
        status = task.status
    )
    db.execute(stml)
    db.commit()

    return db_task


@router.delete("/task/softdelete/{task_id}")
def delete_soft_task(task_id:int, db:Session=Depends(get_db)):

    db_task = db.query(Task).filter(Task.id == task_id,Task.is_deleted== 0).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    stmt = delete(Task).where(Task.id == task_id).values(
        is_deleted = 1,
        deleted_at = datetime.now()
    )
    db.execute(stmt)
    db.commit()
    
    return {"message": "Task soft deleted sussessfully"}


   

@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    return {"message": "Task deleted"}






