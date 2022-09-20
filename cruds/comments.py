from sqlalchemy.orm.session import Session
from schemas.comments import Comment as CommentSchema
from db.models import Post, Comment
from fastapi import HTTPException


def create_comments_by_ids(db: Session, post_id: str, user_id: str, content: str) -> CommentSchema:
    post = db.query(Post).filter(Post.post_id == post_id).first()
    if post is None:
        raise HTTPException(status_code=404, detail="Post not Found")
    comment_orm = Comment(
        user_id=user_id,
        post_id=post_id,
        content=content,
    )

    db.add(comment_orm)
    db.commit()
    db.refresh(comment_orm)
    comment = CommentSchema.from_orm(comment_orm)
    return comment

def delete_comments_by_ids(db: Session, comment_id: str) -> None:
    comment = db.query(Comment).filter(Comment.comment_id == comment_id).first()
    if comment is None:
        raise HTTPException(status_code=404, detail="Comment not Found")
    db.delete(comment)
    db.commit()
    return
