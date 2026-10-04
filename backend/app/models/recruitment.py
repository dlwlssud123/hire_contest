from sqlalchemy import Column, Integer, String, Text, JSON, DateTime
from datetime import datetime
from app.core.database import Base


class Recruitment(Base):
    """
    채용공고 정보 (고용24 채용정보 연계)
    """
    __tablename__ = "recruitments"

    id = Column(Integer, primary_key=True, index=True)
    recruitment_id = Column(String, unique=True, index=True, nullable=False) # 고용24 공고 ID
    company_name = Column(String, nullable=False, index=True)
    title = Column(String, nullable=False)
    job_code = Column(String, nullable=True, index=True)
    location = Column(String, nullable=True)
    company_size = Column(String, nullable=True)
    salary_info = Column(String, nullable=True)
    experience_required = Column(String, nullable=True)
    
    extracted_skills = Column(JSON, default=list)        # AI 추출 요구 기술 스택
    requirements = Column(Text, nullable=True)           # 자격요건 원문
    preferred = Column(Text, nullable=True)              # 우대사항 원문
    detail_url = Column(String, nullable=True)
    
    closing_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
