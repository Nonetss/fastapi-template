from fastapi import APIRouter
from .user import router as user_router
from .jwt import router as jwt_router


router = APIRouter()

router.include_router(user_router, prefix="/user", tags=["user"])
router.include_router(jwt_router, prefix="/jwt", tags=["jwt"])
