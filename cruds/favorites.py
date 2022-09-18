from typing import List
from sqlalchemy.orm.session import Session
from schemas.favorites import Favorites as FavoriteSchema
from db.models import Post, Favorites
from fastapi import HTTPException

def get_all_favorites(db: Session, post_id: str) -> List[FavoriteSchema]:
    favorites_orm = db.query(Favorites).filter(Favorites.post_id == post_id).all()
    favorites = list(map(FavoriteSchema.from_orm,favorites_orm))
    return favorites

def create_favorites_by_ids(db: Session, post_id: str, user_id: str) -> FavoriteSchema:
    post = db.query(Post).filter(Post.post_id == post_id).first()
    if post is None:
        raise HTTPException(status_code=404, detail="post not found")
    favorite_orm = db.query(Favorites).filter(Favorites.post_id == post_id, Favorites.user_id == user_id).first()
    if favorite_orm is not None:
        raise HTTPException(status_code=400, detail="you already favorite")
    favorite_orm = Favorites(
        post_id=post_id,
        user_id=user_id,
    )
    db.add(favorite_orm)
    db.commit()
    db.refresh(favorite_orm)

    favorite = FavoriteSchema.from_orm(favorite_orm)
    return favorite

def delete_favorites_by_ids(db: Session, post_id: str, user_id: str) -> None:
    favorite = db.query(Favorites).filter(Favorites.post_id == post_id, Favorites.user_id == user_id).first()
    if favorite is None:
        raise HTTPException(status_code=400, detail="Post not Found or you have never favorite")
    db.delete(favorite)
    db.commit()
    return