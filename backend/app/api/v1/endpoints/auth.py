from fastapi import APIRouter, HTTPException, Depends
from app.schemas.user import UserCreate, UserResponse, Token

router = APIRouter()


@router.post("/register", response_model=UserResponse)
async def register(user_in: UserCreate):
    return {
        "id": 1,
        "email": user_in.email,
        "name": user_in.name,
        "is_active": True
    }


@router.post("/login", response_model=Token)
async def login():
    return {
        "access_token": "mock-jwt-token-for-careerpath-ai",
        "token_type": "bearer"
    }
