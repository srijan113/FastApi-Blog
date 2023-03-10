### Fast Api

Learning Fast and creating Blogging web application with JWT Authentication.

Steps:

1. Project Setup
    
    a. Create all the files like main.py, gitignore, and ofcourse venv in you project root folder

2. Create a seperate app, in this case a folder and name it according to its function or application

Now your folder structure should be something like this:
```
FastApiBlog
    .venv/
    blog/
        __init__.py
        main.py
    .gitignore
    main.py
    Pipfile
    Pipfile.lock
    README.md
```

3. Then create a path/router and schemas for the blog application
    
    a. Create a file inside blog/ with name `schemas.py` and inside create a schema

        from pydantic import BaseModel

        class Blog(BaseModel):
            title: str
            description: str
    b. Then inside `main.py` file create a path for creating a blog.


        from fastapi import FastApi
        from .schemas import Blog

        app = FastApi()

        app.get(/blog)
        def get_blog_list(request: Blog):
            return request

4. Connecting to a Database using SQLAlchemy
    First install SQLAlchemy using 

    `pip install sqlalchemy`

    a. create a file called database.py where we will create a engine for our database.([learn more.](https://docs.sqlalchemy.org/en/14/orm/quickstart.html#create-an-engine))

        from sqlalchemy import create_engine
        from sqlalchemy.ext.declarative import declarative_base
        from sqlalchemy.orm import sessionmaker

        SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"


        engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

        SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

        Base = declarative_base()

    b. Now, we have create models that will be Used to map a table in SQL database. So, create a file called `models.py` inside you app folder called `blog/` .

        from sqlalchemy import Column, Integer, String
        from .database import Base

        class BlogModel(Base):
            __tablename__ = "Blog"

            id = Column(Integer, primary_key=True, index=True)
            title = Column(String)
            body = Column(String)

    c. Then, we have now migrate all the models to a database so inside our `main.py` file we have bind our models to our database


        from . import database, models

        models.Base.metadata.create_all(bind=database.engine)

5. Creating Blogs objects

    a. Inside of `main.py` file there is router for creating blogs of inside that router we have to define the db that we want to use writing payload. That functions takes request send by user and db info.

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
        
    b. We have take all the request data and pass it through a BlogModel which will be use for mapping to db and validating then the validated data is added to the db using `db.add(obj)` then it is commited to db using 
    `db.commit()` then we get the data from the database after commiting using refresh i.e. db.refresh(new_blog). Finally return the data as new_blog from the db table.

