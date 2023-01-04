from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from . import schemas, models, database


app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/blog')
def create(request: schemas.BlogSchemas, db: Session = Depends(get_db)):
    new_blog = models.BlogModel(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


