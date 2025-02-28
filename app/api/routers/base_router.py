from fastapi import APIRouter

from .user.user_router import user_router
from .auth.auth import auth_router

base_router = APIRouter()

routers = [
    # user_router,
    auth_router
]

for router in routers:
    base_router.include_router(router)
