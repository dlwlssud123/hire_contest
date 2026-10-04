from typing import List, Optional, Dict, Any
from pydantic import BaseModel


class ActionPlanStep(BaseModel):
    week_range: str       # e.g., "1~4주차"
    title: str            # e.g., "Spring Boot 학습 및 프로젝트 개발"
    goal: str
    recommended_activities: List[str]
    linked_trainings: List[Dict[str, Any]] = []
    linked_certifications: List[Dict[str, Any]] = []


class CareerRoadmapCreate(BaseModel):
    target_job: str
    available_months: int = 6


class CareerRoadmapResponse(BaseModel):
    id: int
    user_id: int
    target_job: str
    total_weeks: int
    action_plans: List[ActionPlanStep]
    skill_gap_summary: Dict[str, Any]

    class Config:
        from_attributes = True
