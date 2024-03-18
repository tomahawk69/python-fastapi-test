from enum import Enum
from pydantic import BaseModel, Field
from datetime import datetime


class Item(BaseModel):
    name: str = Field(min_length=3, max_length=60)
    price: float = Field(ge=0)
    is_offer: bool | None = None
    created: datetime | None = None


class Post(BaseModel):
    userId: str
    postId: str
    title: str
    body: str


class Version(str, Enum):
    v1 = "v1"
