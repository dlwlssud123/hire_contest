from typing import List, Optional
from pydantic import BaseModel


class SkillGapItem(BaseModel):
    skill_name: str
    demand_frequency: float     # 채용공고 출현 빈도 (%)
    is_possessed: bool          # 사용자 보유 여부
    priority_level: str         # High, Medium, Low
    learning_weeks: int         # 추천 습득 소요기간
    recommended_trainings: List[str] = []
    recommended_certifications: List[str] = []


class SkillGapAnalysisResponse(BaseModel):
    target_job: str
    readiness_rate: float
    possessed_skills: List[str]
    missing_skills: List[str]
    skill_breakdown: List[SkillGapItem]
