from typing import List, Optional
from pydantic import BaseModel


class JobRecommendation(BaseModel):
    job_code: str
    title: str
    category: Optional[str] = None
    aptitude_match_score: float   # 적성 적합도 (%)
    readiness_score: float        # 현재 준비도 (%)
    matching_reason: str          # 추천 사유
    key_skills: List[str] = []


class JobRecommendationResponse(BaseModel):
    user_id: int
    recommendations: List[JobRecommendation]
