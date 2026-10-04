from sqlalchemy import Column, Integer, String, ForeignKey, JSON, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base


class UserProfile(Base):
    """
    사용자 프로필 (plan.md 5.1 & 9.3 반영)
    전공, 학력, 경력, 보유기술, 프로젝트 경험, 자격증, 희망직무/지역/기업규모, 심리검사 결과 등
    """
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    
    major = Column(String, nullable=True)                      # 전공
    education_level = Column(String, nullable=True)            # 학력
    career_years = Column(Integer, default=0)                  # 경력(년)
    skills = Column(JSON, default=list)                        # 보유 기술 목록 ["Python", "SQL", ...]
    certifications = Column(JSON, default=list)                # 보유 자격증 목록
    projects = Column(JSON, default=list)                      # 프로젝트 경험 목록
    
    target_job = Column(String, nullable=True)                 # 희망 직무
    target_industry = Column(String, nullable=True)            # 희망 산업
    target_location = Column(String, nullable=True)            # 희망 지역
    target_company_size = Column(String, nullable=True)        # 희망 기업 규모
    prep_period_months = Column(Integer, default=6)            # 취업 준비 가능 기간(개월)
    
    psychological_test_data = Column(JSON, nullable=True)      # 고용24 직업심리검사 결과 (흥미/적성/가치관)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="profile")
