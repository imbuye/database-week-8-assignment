from pydantic import BaseModel
from typing import Optional, List
from datetime import date

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[date] = None
    completed: Optional[bool] = False

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    task_id: int
    user_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    user_id: int
    tasks: List[Task] = []

    class Config:
        orm_mode = True
