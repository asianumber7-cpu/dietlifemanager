from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware # <--- [추가 1]
from app.api.v1.api import api_router
from app.core.config import settings
from app.db.base import Base
from app.db.session import engine
from app.models import diet

# DB 테이블 자동 생성
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# --- [추가 2] CORS 미들웨어 설정 (보안 허용) ---
# 리액트가 실행될 주소(http://localhost:5173)를 허용해줍니다.
origins = [
    "http://localhost:5173", # Vite 기본 포트
    "http://localhost:3000", # React 기본 포트
    "http://127.0.0.1:5173",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      # 허용할 출처 목록
    allow_credentials=True,     # 쿠키/인증 정보 허용
    allow_methods=["*"],        # 모든 HTTP 메서드(GET, POST 등) 허용
    allow_headers=["*"],        # 모든 헤더 허용
)
# ----------------------------------------------

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
def root():
    return {"message": "Diet Service is Ready!"}