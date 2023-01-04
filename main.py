from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def index():
    return {"data": {"name": "srijan"}}

@app.get('/about')
def about():
    return {"data":  "This is a about page"}


