from typing import List, Optional, Dict, Any
from pydantic import BaseModel


class ProjectItem(BaseModel):
    title: str
    description: str
    skills: List[str] = []


class ProfileBase(BaseModel):
    major: Optional[str] = None
    education_level: Optional[str] = None
    career_years: int = 0
    skills: List[str] = []
    certifications: List[str] = []
    projects: List[ProjectItem] = []
    
    target_job: Optional[str] = None
    target_industry: Optional[str] = None
    target_location: Optional[str] = None
    target_company_size: Optional[str] = None
    prep_period_months: int = 6
    
    psychological_test_data: Optional[Dict[str, Any]] = None


class ProfileCreate(ProfileBase):
    pass


class ProfileUpdate(ProfileBase):
    pass


class ProfileResponse(ProfileBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
