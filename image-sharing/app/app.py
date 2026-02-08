from fastapi import FastAPI, HTTPException

app = FastAPI()

text_posts = {
    1: {"id": 1, "title": "First Post", "content": "Hello World!"},
    2: {"id": 2, "title": "Second Post", "content": "FastAPI is great!"},
    3: {"id": 3, "title": "Third Post", "content": "Python is awesome!"},
    4: {"id": 4, "title": "Fourth Post", "content": "I love programming!"},
    5: {"id": 5, "title": "Fifth Post", "content": "APIs are fun!"},
    6: {"id": 6, "title": "Sixth Post", "content": "This is a test post!"},
    7: {"id": 7, "title": "Seventh Post", "content": "FastAPI is fast!"},
    8: {"id": 8, "title": "Eighth Post", "content": "I enjoy learning new technologies!"},
    9: {"id": 9, "title": "Ninth Post", "content": "Programming is a valuable skill!"},
    10: {"id": 10, "title": "Tenth Post", "content": "This is the last post!"}
}
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
async def get_posts(limit: int = None): # type: ignore
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{post_id}")
async def get_post(post_id: int):
    if post_id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    post = text_posts.get(post_id)
    return post
