from datetime import datetime
from typing import List
from .users import User
from pydantic import BaseModel, Field
from .comments import Comment

class PostPayload(BaseModel):
    content: str = Field(default=None, title="Thie is a TweetContent", max_length=120)

class Post(BaseModel):
    post_id: str
    user_id: str
    content: str
    created_at: datetime = None
    user: User
    favorites: List[User]
    comments: List[Comment]

    class Config:
        orm_mode = True
