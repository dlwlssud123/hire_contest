from typing import Dict, Any, List
from pydantic import BaseModel
from datetime import datetime


class CareerReportResponse(BaseModel):
    id: int
    user_id: int
    title: str
    version: int
    created_at: datetime
    
    # 8대 핵심 섹션 데이터 (plan.md 12)
    profile_summary: Dict[str, Any]
    recommended_jobs: List[Dict[str, Any]]
    recommended_recruitments: List[Dict[str, Any]]
    skill_gap_analysis: Dict[str, Any]
    market_insights: Dict[str, Any]
    recommended_education: List[Dict[str, Any]]
    career_path: Dict[str, Any]
    action_plans: List[Dict[str, Any]]

    class Config:
        from_attributes = True
