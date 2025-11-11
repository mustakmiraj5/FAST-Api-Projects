from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app import crud, schemas
from app.database import SessionLocal

# Create router
router = APIRouter()

# Dependency to get DB session
async def get_db():
    async with SessionLocal() as session:
        yield session

# -------------------------
# CREATE Task
# -------------------------
@router.post("/", response_model=schemas.Task)
async def create_task(task: schemas.TaskCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_task(db, task)

# -------------------------
# READ all tasks
# -------------------------
@router.get("/", response_model=List[schemas.Task])
async def read_tasks(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    return await crud.get_tasks(db, skip=skip, limit=limit)

# -------------------------
# READ single task
# -------------------------
@router.get("/{task_id}", response_model=schemas.Task)
async def read_task(task_id: int, db: AsyncSession = Depends(get_db)):
    db_task = await crud.get_task(db, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

# -------------------------
# UPDATE task
# -------------------------
@router.put("/{task_id}", response_model=schemas.Task)
async def update_task(task_id: int, task: schemas.TaskUpdate, db: AsyncSession = Depends(get_db)):
    db_task = await crud.update_task(db, task_id, task)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

# -------------------------
# DELETE task
# -------------------------
@router.delete("/{task_id}", response_model=schemas.Task)
async def delete_task(task_id: int, db: AsyncSession = Depends(get_db)):
    db_task = await crud.delete_task(db, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task
