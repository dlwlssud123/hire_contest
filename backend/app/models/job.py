from sqlalchemy import Column, Integer, String, Text, JSON, DateTime
from datetime import datetime
from app.core.database import Base


class JobRole(Base):
    """
    직무 및 직업 정보 (고용24 직업/직무 연계)
    """
    __tablename__ = "job_roles"

    id = Column(Integer, primary_key=True, index=True)
    job_code = Column(String, unique=True, index=True, nullable=False) # 고용24 직무 코드
    title = Column(String, nullable=False)                             # 직무명 (예: 백엔드 개발자)
    category = Column(String, nullable=True)                          # 직무 카테고리
    description = Column(Text, nullable=True)                         # 직무 설명
    required_skills = Column(JSON, default=list)                      # 주요 요구 역량
    aptitude_traits = Column(JSON, default=list)                      # 적합 적성/성향 특성
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
