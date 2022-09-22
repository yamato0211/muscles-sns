from pydantic import BaseModel

class Favorites(BaseModel):
    user_id: str
    post_id: str

    class Config:
        orm_mode = True

class CommentFavorites(BaseModel):
    user_id: str
    comment_id: str

    class Config:
        orm_mode = True