from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str
    status: int

class TaskUpdate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int
    # kế thừa các trường từ TaskBase nên khong cần định nghĩa lại

    class Config:
        from_attributes = True