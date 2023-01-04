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
        ```
        from pydantic import BaseModel

        class Blog(BaseModel):
            title: str
            description: str
        ```
    b. Then inside `main.py` file create a path for creating a blog.
        ```
        from fastapi import FastApi
        from .schemas import Blog

        app = FastApi()

        app.get(/blog)
        def get_blog_list(request: Blog):
            return request
        ```