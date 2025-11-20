from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# 1. 엔진 생성 (DB와 연결되는 심장)
engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)

# 2. 세션 생성기 (요청이 올 때마다 전용 전화선을 하나씩 놔주는 역할)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)