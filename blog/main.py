from fastapi import FastAPI

from . import schemas

app = FastAPI()

@app.get('/blog')
def create(request : schemas.Blog):
    return request
