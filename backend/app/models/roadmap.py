from sqlalchemy import Column, Integer, String, ForeignKey, JSON, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base


class CareerRoadmap(Base):
    """
    취업 경로 최적화 및 주차별 Action Plan (plan.md 7 반영)
    """
    __tablename__ = "career_roadmaps"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    target_job = Column(String, nullable=False)
    total_weeks = Column(Integer, default=12)
    
    # 주차별 액션 플랜: [{"week_range": "1~4주차", "title": "Spring Boot 학습", "details": "..."}]
    action_plans = Column(JSON, default=list)
    skill_gap_summary = Column(JSON, default=dict)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="roadmaps")
