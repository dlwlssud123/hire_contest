from fastapi import APIRouter
from app.schemas.roadmap import CareerRoadmapResponse, CareerRoadmapCreate
from app.services.path_optimizer_service import path_optimizer_service
from app.models.profile import UserProfile

router = APIRouter()


@router.post("/optimize", response_model=CareerRoadmapResponse)
async def optimize_path(req: CareerRoadmapCreate):
    mock_profile = UserProfile(
        user_id=1,
        skills=["Java", "SQL", "Git", "Python"],
        target_job=req.target_job,
        prep_period_months=req.available_months
    )
    roadmap_data = await path_optimizer_service.generate_optimized_roadmap(
        mock_profile, req.target_job, req.available_months
    )
    return CareerRoadmapResponse(
        id=1,
        user_id=1,
        target_job=req.target_job,
        total_weeks=roadmap_data["total_weeks"],
        action_plans=roadmap_data["action_plans"],
        skill_gap_summary=roadmap_data["skill_gap_summary"]
    )
