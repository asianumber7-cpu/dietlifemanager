from sqlalchemy.ext.declarative import declarative_base

# 모든 모델이 상속받을 부모 클래스
Base = declarative_base()

# 여기에 우리가 만든 모델들을 import 해야 DB가 인식합니다.
# (나중에 User 모델도 여기에 추가하면 됩니다)
# from app.models.user import User  <-- 나중에 주석 해제
# from app.models.diet import Diet  <-- 여기서는 순환 참조 방지를 위해 main.py에서 처리