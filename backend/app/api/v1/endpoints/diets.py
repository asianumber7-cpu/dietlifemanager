from fastapi import APIRouter
from app.schemas.diet import DietInput, DietOutput
from app.services.diet_advisor import diet_advisor

router = APIRouter()

@router.post("/calculate", response_model=DietOutput)
def calculate_diet(diet_in: DietInput):
    """
    사용자의 신체 정보를 받아 다이어트 가이드를 계산합니다.
    """
    # 서비스 로직에 데이터 전달 후 결과 반환
    result = diet_advisor.calculate(diet_in)
    return result