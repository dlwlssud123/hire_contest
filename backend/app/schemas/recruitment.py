from typing import List, Optional
from pydantic import BaseModel


class RecruitmentRecommendation(BaseModel):
    recruitment_id: str
    company_name: str
    title: str
    location: Optional[str] = None
    company_size: Optional[str] = None
    salary_info: Optional[str] = None
    match_score: float
    fit_reasons: List[str] = []
    missing_skills: List[str] = []
    detail_url: Optional[str] = None


class RecruitmentResponse(BaseModel):
    items: List[RecruitmentRecommendation]
    total: int
