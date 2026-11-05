from fastapi import FastAPI
from schemas import AuthorCreate

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to the personal library API project"}


# POST /authors → validate request → create SQLAlchemy object → save → return response.
@app.post("/authors")
def create_author(author: AuthorCreate):
    return author
