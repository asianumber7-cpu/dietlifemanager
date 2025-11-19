from fastapi import APIRouter, HTTPException
from typing import List, Optional
from pydantic import BaseModel

router = APIRouter()

# --- Schemas (데이터 구조 정의) ---
class UserBase(BaseModel):
    email: str
    name: str
    age: Optional[int] = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    class Config:
        from_attributes = True

# --- In-Memory DB (실제 DB 연결 전 테스트용 임시 저장소) ---
fake_users_db = []

# --- CRUD Operations ---

@router.post("/", response_model=User)
def create_user(user_in: UserCreate):
    """
    새로운 사용자 생성 (Create)
    """
    # 실제로는 여기서 DB에 저장하고 비밀번호를 해싱해야 합니다.
    new_user_id = len(fake_users_db) + 1
    new_user = {**user_in.model_dump(), "id": new_user_id}
    fake_users_db.append(new_user)
    return new_user

@router.get("/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 100):
    """
    모든 사용자 조회 (Read - List)
    """
    return fake_users_db[skip : skip + limit]

@router.get("/{user_id}", response_model=User)
def read_user(user_id: int):
    """
    특정 사용자 조회 (Read - Detail)
    """
    for user in fake_users_db:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")