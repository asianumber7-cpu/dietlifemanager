from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.diet import DietInput, DietOutput
from app.services.diet_advisor import diet_advisor
from app.services.watson_service import get_diet_advice_from_watson # <--- 추가
from app.api.deps import get_db
from app.models.diet import Diet

router = APIRouter()

@router.post("/calculate", response_model=DietOutput)
def calculate_diet(
    diet_in: DietInput,
    db: Session = Depends(get_db)
):
    # 1. 기본 수학 계산 (BMI, BMR 등)
    result = diet_advisor.calculate(diet_in)
    
    # 2. IBM Watson에게 조언 요청 (AI)
    # 계산된 결과를 딕셔너리로 만들어서 넘겨줍니다.
    user_data_for_ai = {
        "height": diet_in.height,
        "weight": diet_in.weight,
        "age": diet_in.age,
        "gender": diet_in.gender,
        "activity_level": diet_in.activity_level,
        "bmi": result.bmi,
        "bmi_status": result.bmi_status,
        "bmr": result.bmr
    }
    
    ai_advice = get_diet_advice_from_watson(user_data_for_ai)
    
    # 3. 결과에 AI 조언 덮어쓰기
    result.advice = ai_advice 
    
    # 4. DB 저장
    diet_record = Diet(
        height=diet_in.height,
        weight=diet_in.weight,
        age=diet_in.age,
        gender=diet_in.gender,
        activity_level=diet_in.activity_level,
        bmi=result.bmi,
        bmi_status=result.bmi_status,
        tdee=result.tdee,
        bmr=result.bmr,
        recommend_calories=result.recommend_calories,
        advice=result.advice # 여기에 왓슨의 말이 저장됩니다.
    )
    
    db.add(diet_record)
    db.commit()
    db.refresh(diet_record)
    
    return result