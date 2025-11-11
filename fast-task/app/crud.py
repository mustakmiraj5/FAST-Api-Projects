from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from app.models import Task
from app.schemas import TaskCreate, TaskUpdate

# -------------------------
# CREATE
# -------------------------
async def create_task(db: AsyncSession, task: TaskCreate) -> Task:
    db_task = Task(**task.dict())
    db.add(db_task)
    await db.commit()
    await db.refresh(db_task)
    return db_task

# -------------------------
# READ ALL
# -------------------------
async def get_tasks(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(Task).offset(skip).limit(limit))
    return result.scalars().all()

# -------------------------
# READ SINGLE
# -------------------------
async def get_task(db: AsyncSession, task_id: int):
    result = await db.execute(select(Task).where(Task.id == task_id))
    return result.scalars().first()

# -------------------------
# UPDATE
# -------------------------
async def update_task(db: AsyncSession, task_id: int, task: TaskUpdate):
    result = await db.execute(select(Task).where(Task.id == task_id))
    db_task = result.scalars().first()
    if not db_task:
        return None
    for key, value in task.dict(exclude_unset=True).items():
        setattr(db_task, key, value)
    db.add(db_task)
    await db.commit()
    await db.refresh(db_task)
    return db_task

# -------------------------
# DELETE
# -------------------------
async def delete_task(db: AsyncSession, task_id: int):
    result = await db.execute(select(Task).where(Task.id == task_id))
    db_task = result.scalars().first()
    if not db_task:
        return None
    await db.delete(db_task)
    await db.commit()
    return db_task
