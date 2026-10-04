from fastapi import APIRouter
from app.schemas.skill_gap import SkillGapAnalysisResponse
from app.services.skill_gap_service import skill_gap_service
from app.models.profile import UserProfile

router = APIRouter()


@router.get("/analyze", response_model=SkillGapAnalysisResponse)
async def analyze_skill_gap(target_job: str = "백엔드 개발자"):
    mock_profile = UserProfile(
        user_id=1,
        skills=["Java", "SQL", "Git", "Python"],
        target_job=target_job
    )
    return await skill_gap_service.analyze_gap(mock_profile, target_job)
