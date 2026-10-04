from fastapi import APIRouter
from app.schemas.report import CareerReportResponse
from app.services.report_service import report_service
from app.models.profile import UserProfile
from datetime import datetime

router = APIRouter()


@router.get("/generate", response_model=CareerReportResponse)
async def generate_report(user_id: int = 1, target_job: str = "백엔드 개발자"):
    mock_profile = UserProfile(
        user_id=user_id,
        major="컴퓨터공학과",
        education_level="대졸(4년)",
        skills=["Java", "SQL", "Git", "Python"],
        target_job=target_job,
        target_location="서울",
        prep_period_months=3
    )
    report_data = await report_service.generate_full_report(mock_profile, target_job)
    
    return CareerReportResponse(
        id=1,
        user_id=user_id,
        title=report_data["title"],
        version=1,
        created_at=datetime.utcnow(),
        profile_summary=report_data["profile_summary"],
        recommended_jobs=report_data["recommended_jobs"],
        recommended_recruitments=report_data["recommended_recruitments"],
        skill_gap_analysis=report_data["skill_gap_analysis"],
        market_insights=report_data["market_insights"],
        recommended_education=report_data["recommended_education"],
        career_path=report_data["career_path"],
        action_plans=report_data["action_plans"]
    )
