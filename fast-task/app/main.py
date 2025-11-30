from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.database import init_db
from app.routers import tasks
from app.routers import users


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context used by FastAPI to run startup/shutdown logic.

    This replaces the deprecated @app.on_event("startup").
    Initialize the database during startup by awaiting `init_db()`.
    Add any shutdown/cleanup after the `yield` if needed.
    """
    await init_db()
    yield


app = FastAPI(title="FastTask API", version="1.0.0", lifespan=lifespan)

app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])
app.include_router(users.router, prefix="/users", tags=["Users"])


@app.get("/")
def root():
    return {"message": "Welcome to FastTask API!"}
