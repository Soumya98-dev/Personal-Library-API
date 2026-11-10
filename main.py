from fastapi import FastAPI, HTTPException, status
from schemas import AuthorCreate
from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Author
from database import Base, engine
from schemas import AuthorResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to the personal library API project"}


@app.get("/authors", response_model=list[AuthorResponse])
def list_authors(db: Session = Depends(get_db)):
    return db.query(Author).all()


@app.get("/authors/{author_id}", response_model=AuthorResponse)
def get_author_by_id(author_id: int, db: Session = Depends(get_db)):
    author = db.get(Author, author_id)
    if author is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Author not found"
        )
    return author


# POST /authors → validate request → create SQLAlchemy object → save → return response.
@app.post(
    "/authors", response_model=AuthorResponse, status_code=status.HTTP_201_CREATED
)
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    new_author = Author(name=author.name, country=author.country)
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author
