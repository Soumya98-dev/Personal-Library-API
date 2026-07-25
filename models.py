from __future__ import annotations

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates

from database import Base

class Author(Base):
    __tablename__ = "authors"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    country: Mapped[str] = mapped_column(String(120), nullable=False)
    
    books: Mapped[list[Book]] = relationship(back_populates="author")

class Book(Base):
    __tablename__ = "books"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    pages: Mapped[int] = mapped_column(Integer, nullable=False)
    published_year: Mapped[int] = mapped_column(nullable=False)
    author_id: Mapped[int] = mapped_column(
        ForeignKey("authors.id"), nullable=False, index=True
    )
    
    @validates("pages")
    def validate_pages(self, key: str, page: int) -> int:
        if not (page > 0):
            raise ValueError(f"Invalid page count: {page}. Must be greater than 0.")
        return page
    
    author: Mapped[Author] = relationship(back_populates="books")