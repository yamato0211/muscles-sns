from sqlalchemy.orm.session import Session
from schemas.favorites import CommentFavorites as CommentSchema
from schemas.favorites import Favorites as FavoriteSchema
from db.models import Post, PostFavorites, CommentFavorites, Comment
from fastapi import HTTPException


def create_post_favorites_by_ids(db: Session, post_id: str, user_id: str) -> FavoriteSchema:
    post = db.query(Post).filter(Post.post_id == post_id).first()
    if post is None:
        raise HTTPException(status_code=404, detail="post not found")
    favorite_orm = db.query(PostFavorites).filter(PostFavorites.post_id == post_id, PostFavorites.user_id == user_id).first()
    if favorite_orm is not None:
        raise HTTPException(status_code=400, detail="you already favorite")
    favorite_orm = PostFavorites(
        post_id=post_id,
        user_id=user_id,
    )
    db.add(favorite_orm)
    db.commit()
    db.refresh(favorite_orm)

    favorite = FavoriteSchema.from_orm(favorite_orm)
    return favorite

def delete_post_favorites_by_ids(db: Session, post_id: str, user_id: str) -> None:
    post = db.query(Post).filter(Post.post_id == post_id).first()
    if post is None:
        raise HTTPException(status_code=404, detail="post not found")
    favorite = db.query(PostFavorites).filter(PostFavorites.post_id == post_id, PostFavorites.user_id == user_id).first()
    if favorite is None:
        raise HTTPException(status_code=400, detail="Post not Found or you have never favorite")
    db.delete(favorite)
    db.commit()
    return


def create_comment_favorites_by_ids(db: Session, comment_id: str, user_id: str) -> CommentSchema:
    comment = db.query(Comment).filter(Comment.comment_id == comment_id).first()
    if comment is None:
        raise HTTPException(status_code=404, detail="comment not found!!")
    comment_favorite = db.query(CommentFavorites).filter(
        CommentFavorites.comment_id == comment_id,
        CommentFavorites.user_id == user_id
    ).first()
    if comment_favorite is not None:
        raise HTTPException(status_code=400, detail="you already favorite")
    comment_favorite_orm = CommentFavorites(
        user_id=user_id,
        comment_id= comment_id,
    )
    db.add(comment_favorite_orm)
    db.commit()
    db.refresh(comment_favorite_orm)
    comment_favorite = CommentSchema.from_orm(comment_favorite_orm)
    return comment_favorite

def delete_comment_favorites_by_ids(db: Session, comment_id: str, user_id: str) -> None:
    comment = db.query(Comment).filter(Comment.comment_id == comment_id).first()
    if comment is None:
        raise HTTPException(status_code=404, detail="comment not found!!")
    favorite = db.query(CommentFavorites).filter(
        CommentFavorites.user_id == user_id,
        CommentFavorites.comment_id == comment_id
    ).first()
    if favorite is None:
        raise HTTPException(status_code=404, detail="comment not found")

    db.delete(favorite)
    db.commit()
    return