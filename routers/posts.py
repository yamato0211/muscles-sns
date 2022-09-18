from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm.session import Session
from schemas.posts import PostPayload, Post as PostSchema
from cruds.posts import create_post_by_user_id, get_timeline, get_posts_by_user_id
from cruds.posts import delete_post_by_post_id, get_post_detail_by_post_id
from db.database import get_db
from utils.jwt import get_current_user

post_router = APIRouter()

@post_router.get("/",response_model=List[PostSchema])
async def get_posts(db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    if user_id is None:
        raise HTTPException(status_code=403, detail="jwt_token is invalid!!")
    posts = get_timeline(db)
    return posts

@post_router.post("/",response_model=PostSchema)
async def create_post(payload: PostPayload, db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    if user_id is None:
        raise HTTPException(status_code=403, detail="jwt_token is invalid!")
    post = create_post_by_user_id(db, payload.content, user_id)
    return post

@post_router.get("/details/{post_id}",response_model=PostSchema)
async def get_post_detail(post_id: str, db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    if user_id is None:
        raise HTTPException(status_code=403, detail="jwt_token is invalid")
    post = get_post_detail_by_post_id(db, post_id)
    return post

@post_router.get("/me",response_model=List[PostSchema])
async def get_my_posts(db:Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    if user_id is None:
        raise HTTPException(status_code=403, detail="jwt_token is invalid!")
    posts = get_posts_by_user_id(db, user_id)
    return posts

@post_router.delete("/{post_id}")
async def delete_post(post_id: str, db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    if user_id is None:
        raise HTTPException(status_code=403, detail="jwt_token si invalid!")
    delete_post_by_post_id(db, post_id, user_id)
    return {"detail" : "OK!!"}

@post_router.get("/{uid}", response_model=List[PostSchema])
async def get_user_posts(uid: str, db:Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    if user_id is None:
        raise HTTPException(status_code=403, detail="jwt_token si invalid!")
    posts = get_posts_by_user_id(db, uid)
    return posts