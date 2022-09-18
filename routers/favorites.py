from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm.session import Session
from schemas.favorites import Favorites as FavoriteSchema
from db.database import get_db
from utils.jwt import get_current_user
from cruds.favorites import create_favorites_by_ids, delete_favorites_by_ids

favorite_router = APIRouter()


@favorite_router.post("/{post_id}", response_model=FavoriteSchema)
async def create_favorite(post_id: str, db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    if user_id is None:
        raise HTTPException(status_code=403, detail="jwt_token is invalid")
    favorite = create_favorites_by_ids(db, post_id, user_id)
    return favorite

@favorite_router.delete("/{post_id}")
async def delete_favorite(post_id: str, db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    if user_id is None:
        raise HTTPException(status_code=403, detail="jwt_token is invalid")
    delete_favorites_by_ids(db, post_id, user_id)
    return {"detail" : "OK!!"}
