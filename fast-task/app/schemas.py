from pydantic import BaseModel
from typing import Optional

# Shared properties
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: Optional[bool] = False

# Properties required when creating a new task
class TaskCreate(TaskBase):
    pass

# Properties for updating an existing task
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

# Properties returned in responses
class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True
