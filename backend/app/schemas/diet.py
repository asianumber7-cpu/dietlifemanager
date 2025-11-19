from pydantic import BaseModel, Field
from enum import Enum

# 활동량 레벨을 미리 정의 (오타 방지 및 명확성)
class ActivityLevel(str, Enum):
    SEDENTARY = "sedentary"       # 운동 안 함 (사무직)
    LIGHTLY_ACTIVE = "lightly"    # 주 1-3회 가벼운 운동
    MODERATELY_ACTIVE = "moderate" # 주 3-5회 적당한 운동
    VERY_ACTIVE = "active"        # 주 6-7회 심한 운동
    EXTRA_ACTIVE = "extra"        # 매우 심한 운동 (선수급)

# 사용자가 입력할 데이터 (Input)
class DietInput(BaseModel):
    height: float = Field(..., gt=0, description="키 (cm 단위)")
    weight: float = Field(..., gt=0, description="몸무게 (kg 단위)")
    age: int = Field(..., gt=0, description="나이")
    gender: str = Field(..., description="성별 ('male' 또는 'female')")
    activity_level: ActivityLevel = Field(..., description="활동량 레벨")

# 우리가 돌려줄 데이터 (Output)
class DietOutput(BaseModel):
    bmi: float
    bmi_status: str         # 저체중, 정상, 비만 등
    bmr: float              # 기초대사량
    tdee: float             # 하루 총 에너지 소비량 (유지 칼로리)
    recommend_calories: float # 다이어트 추천 칼로리
    advice: str             # AI의 조언 메시지