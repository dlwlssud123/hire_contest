from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.schemas.profile import ProfileCreate, ProfileResponse
from app.services.profile_service import profile_service

router = APIRouter()


@router.get("/{user_id}", response_model=ProfileResponse)
async def get_profile(user_id: int, db: AsyncSession = Depends(get_db)):
    profile = await profile_service.get_by_user_id(db, user_id)
    if not profile:
        # Return default template profile
        return ProfileResponse(
            id=1,
            user_id=user_id,
            major="컴퓨터공학과",
            education_level="대졸(4년)",
            career_years=0,
            skills=["Java", "SQL", "Git", "Python"],
            certifications=["SQLD"],
            projects=[{"title": "쇼핑몰 백엔드 프로젝트", "description": "Spring REST API 기반", "skills": ["Java", "MySQL"]}],
            target_job="백엔드 개발자",
            target_location="서울",
            prep_period_months=3
        )
    return profile


@router.post("/{user_id}", response_model=ProfileResponse)
async def update_profile(user_id: int, profile_in: ProfileCreate, db: AsyncSession = Depends(get_db)):
    return await profile_service.create_or_update(db, user_id, profile_in)
