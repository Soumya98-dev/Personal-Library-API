from pydantic import BaseModel, Field, ConfigDict, field_validator


# ---------------Author Schema-------------------------
class AuthorBase(BaseModel):
    name: str = Field(min_length=2, max_length=250)
    country: str = Field(min_length=2, max_length=250)


class AuthorCreate(AuthorBase):
    pass


class AuthorResponse(AuthorBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


# ------------------Book Schema--------------------------
class BookBase(BaseModel):
    title: str = Field(min_length=2, max_length=500)
    pages: int = Field(gt=0, description="Pages must be a positive integer")
    published_year: int

    @field_validator("published_year")
    @classmethod
    def validate_four_digit_year(cls, v: int):
        if not (1000 <= v <= 9999):
            raise ValueError("published_year must be a 4-digits integer (1000 - 9999)")
        return v


class BookCreate(BookBase):
    author_id: int


class BookResponse(BookBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    author_id: int
