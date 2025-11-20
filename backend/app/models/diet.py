from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from app.db.base import Base  # 아래 3단계에서 만들 Base를 가져옵니다.

class Diet(Base):
    __tablename__ = "diets"  # DB에 저장될 테이블 이름

    id = Column(Integer, primary_key=True, index=True) # 고유 번호
    height = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    activity_level = Column(String, nullable=False)
    
    bmi = Column(Float)         
    bmi_status = Column(String) 
    tdee = Column(Float)         

    # 결과값 저장
    bmr = Column(Float)
    recommend_calories = Column(Float)
    advice = Column(String)
    
    # 생성 시간 (자동 입력)
    created_at = Column(DateTime(timezone=True), server_default=func.now())