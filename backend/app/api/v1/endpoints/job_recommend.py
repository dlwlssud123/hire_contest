from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.schemas.job import JobRecommendationResponse
from app.services.job_match_service import job_match_service
from app.models.profile import UserProfile

router = APIRouter()


@router.get("/recommendations/{user_id}", response_model=JobRecommendationResponse)
async def get_job_recommendations(user_id: int, db: AsyncSession = Depends(get_db)):
    mock_profile = UserProfile(
        user_id=user_id,
        major="컴퓨터공학",
        skills=["Java", "SQL", "Git", "Python"],
        prep_period_months=3
    )
    return await job_match_service.recommend_jobs(db, mock_profile)
