from typing import List
from pydantic import BaseModel
from .users import User


class CommentPayload(BaseModel):
    content: str

class Comment(BaseModel):
    comment_id: str
    user_id: str
    post_id: str
    content: str
    user: User
    favorites: List[User]

    class Config:
        orm_mode = True    
