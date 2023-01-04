from pydantic import BaseModel

class BlogSchemas(BaseModel):
    title: str
    body: str


