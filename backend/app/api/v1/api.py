from fastapi import APIRouter
from app.api.v1.endpoints import users , diets

api_router = APIRouter()
# /users 경로로 들어오는 요청은 users.py가 처리하도록 위임
api_router.include_router(users.router, prefix="/users", tags=["users"])
# 아래 줄 추가: /diets 경로로 들어오면 diets.py가 처리함
api_router.include_router(diets.router, prefix="/diets", tags=["diets"])