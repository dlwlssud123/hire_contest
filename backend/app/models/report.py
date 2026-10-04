from sqlalchemy import Column, Integer, String, ForeignKey, JSON, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base


class CareerReport(Base):
    """
    AI 취업 전략 보고서 (plan.md 12 반영)
    1. 사용자 프로필 요약
    2. 추천 직무
    3. 추천 채용공고 & 기업
    4. Skill Gap 분석
    5. 노동시장 분석
    6. 추천 교육 및 자격
    7. 취업 경로
    8. Action Plan
    """
    __tablename__ = "career_reports"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String, nullable=False)
    
    report_content = Column(JSON, nullable=False) # 8대 섹션 통합 데이터
    version = Column(Integer, default=1)
    
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="reports")
