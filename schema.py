# schema.py

from pydantic import BaseModel, Field, ValidationError, validator
from typing import List, Tuple


class Article(BaseModel):
    id: str
    source: str
    content: str = Field(min_length=50)
    length: int

    @validator("content")
    def validate_content(cls, v):
        if not v.strip():
            raise ValueError("Content cannot be empty")
        return v


def validate_data(raw_data: List[dict]) -> Tuple[List[dict], List[str]]:
    """
    Validates scraped data against schema.
    Returns valid data and error messages.
    """

    valid_data = []
    errors = []

    for item in raw_data:
        try:
            article = Article(**item)
            valid_data.append(article.dict())
        except ValidationError as e:
            errors.append(str(e))

    return valid_data, errors
