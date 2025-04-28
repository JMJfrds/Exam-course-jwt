from fastapi import APIRouter
from routers.user import router as user_router
from routers.courses import router as courses_router

router = APIRouter()

router.include_router(user_router)
router.include_router(courses_router)