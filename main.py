from fastapi import FastAPI

import uvicorn

from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def index(limit=10, published: bool = False, sort: Optional[str] = None):
    if published:
        return {"data": f"{limit} published blogs from the db"}
    else:
        return {"data": f"{limit} blogs from db"}

@app.get('/about')
def about():
    return {"data":  "This is a about page"}


class Blog(BaseModel):
    id: Optional[int]
    title: str
    description: str
    published: Optional[bool] = True

@app.post('/create/')
def create_blog(request: Blog):
    return {"data": f"{request.title} is the title of the blog."}



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

