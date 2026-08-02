from pydantic import BaseModel, Field


class Book(BaseModel):
    title: str
    author: str
    rating: int = Field(default = None, ge = 0, le = 5)
    year: int = Field(default = None, gt = 0)
    pages: int | None = Field(default = None, gt = 0)

