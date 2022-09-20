from fastapi import APIRouter
from .users import user_router
from .posts import post_router
from .favorites import favorite_router
from .comments import comment_router

router = APIRouter()

router.include_router(user_router, prefix="/users", tags=["users"])
router.include_router(post_router, prefix="/posts", tags=["posts"])
router.include_router(favorite_router, prefix="/favorites", tags=["favorites"])
router.include_router(comment_router, prefix="/comments", tags=["comments"])