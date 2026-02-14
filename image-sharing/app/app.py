from fastapi import FastAPI, HTTPException
from .schema import Post
from .db import init_db
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)

text_posts = {
    1: Post(title="First Post", content="Hello World!"),
    2: Post(title="Second Post", content="FastAPI is great!"),
    3: Post(title="Third Post", content="Python is awesome!"),
    4: Post(title="Fourth Post", content="I love programming!"),
    5: Post(title="Fifth Post", content="APIs are fun!"),
    6: Post(title="Sixth Post", content="This is a test post!"),
    7: Post(title="Seventh Post", content="FastAPI is fast!"),
    8: Post(title="Eighth Post", content="I enjoy learning new technologies!"),
    9: Post(title="Ninth Post", content="Programming is a valuable skill!"),
    10: Post(title="Tenth Post", content="This is the last post!")
}
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
async def get_posts(limit: int = None) -> list[Post]: # type: ignore
    if limit:
        return list(text_posts.values())[:limit]
    return list(text_posts.values())

@app.get("/posts/{post_id}")
async def get_post(post_id: int):
    if post_id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    post = text_posts.get(post_id)
    return post

@app.post("/posts")
async def create_post(post: Post) -> dict:
    new_id = max(text_posts.keys()) + 1
    text_posts[new_id] = post
    return {"id": new_id, "message": "Post created successfully"}

@app.delete("/posts/{post_id}")
async def delete_post(post_id: int):
    if post_id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    del text_posts[post_id]
    return {"message": "Post deleted successfully"}
