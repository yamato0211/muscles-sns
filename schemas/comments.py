from pydantic import BaseModel
from .users import User

class Comment(BaseModel):
    comment_id: str
    user_id: str
    post_id: str
    content: str
    user: User

    class Config:
        orm_mode = True    
