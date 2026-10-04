from sqlalchemy import Column, Integer, String, Float, JSON, DateTime
from datetime import datetime
from app.core.database import Base


class Skill(Base):
    """
    기술 스택 및 역량 마스터 정보 (출현 빈도, 연계 교육/자격)
    """
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False) # e.g. "Spring Boot", "AWS"
    category = Column(String, nullable=True)                      # Backend, Cloud, Data 등
    demand_frequency = Column(Float, default=0.0)                 # 채용시장 출현 빈도 (%)
    avg_learning_weeks = Column(Integer, default=4)               # 평균 습득 소요기간(주)
    related_trainings = Column(JSON, default=list)                # 고용24 훈련과정 목록
    related_certifications = Column(JSON, default=list)           # Q-Net 자격증 목록
    
    created_at = Column(DateTime, default=datetime.utcnow)
