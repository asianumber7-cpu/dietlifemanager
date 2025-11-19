from fastapi import FastAPI
from app.api.v1.api import api_router
from app.core.config import settings

# 앱 인스턴스 생성 (유연한 설정 적용)
app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# 라우터 등록 (기능별로 나뉜 파일들을 하나로 합침)
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
def root():
    """
    헬스 체크용 기본 경로
    """
    return {"message": "Diet & Life Manager API is running", "version": "1.0.0"}