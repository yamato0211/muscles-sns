from fastapi import APIRouter, Depends, HTTPException
from schemas.comments import Comment
from sqlalchemy.orm.session import Session
from db.database import get_db
from utils.jwt import get_current_user
from cruds import comments as c

comment_router = APIRouter()

@comment_router.post("/", response_model=Comment)
async def create_comment(post_id: str, content: str, db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    if user_id is None:
        raise HTTPException(status_code=403, detail="jwt_token is invalid!")
    comment = c.create_comments_by_ids(db,post_id,user_id,content)
    return comment

@comment_router.delete("/")
async def delete_comment(comment_id: str, db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    if user_id is None:
        raise HTTPException(status_code=403, detail="jwt_token is Invalid!")
    c.delete_comments_by_ids(db, comment_id)
    return {"detail" : "OK!!"}