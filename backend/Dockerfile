# 1. 베이스 이미지: 파이썬 3.11 (슬림 버전으로 용량 최소화)
FROM python:3.11.14-slim

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 환경 변수 설정 (파이썬 버퍼링 끄기 - 로그 즉시 출력)
ENV PYTHONUNBUFFERED=1

# 4. 의존성 파일 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. 전체 소스 코드 복사
COPY . .

# 6. 서버 실행 명령어 (Uvicorn)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]