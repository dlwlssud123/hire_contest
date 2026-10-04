from typing import List
from pydantic import BaseModel


class SimulationActivity(BaseModel):
    activity_name: str          # e.g., "Spring 프로젝트 추가", "정보처리기사 취득"
    duration_weeks: int
    readiness_before: float
    readiness_after: float
    score_delta: float
    description: str


class SimulationRequest(BaseModel):
    user_id: int
    target_job: str
    selected_activities: List[str]


class SimulationResponse(BaseModel):
    current_readiness: float
    projected_readiness: float
    total_duration_weeks: int
    simulation_results: List[SimulationActivity]
