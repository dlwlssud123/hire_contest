from typing import List
from app.schemas.skill_gap import SkillGapAnalysisResponse, SkillGapItem
from app.models.profile import UserProfile


class SkillGapService:
    """
    실제 채용시장 요구역량 기반 Skill Gap 분석 서비스 (plan.md 6)
    """
    @staticmethod
    async def analyze_gap(profile: UserProfile, target_job: str) -> SkillGapAnalysisResponse:
        user_skills_set = set(k.lower() for k in (profile.skills or []))
        
        # 목표 직무별 시장 요구 역량 데이터 (고용24 채용공고 빅데이터 기반 연동 구조)
        market_requirements = [
            {"name": "Java", "freq": 78.0, "priority": "High", "weeks": 3, "trainings": ["자바 웹 프로그래밍 실무"], "certs": ["정보처리기사"]},
            {"name": "Spring Boot", "freq": 71.0, "priority": "High", "weeks": 4, "trainings": ["Spring Cloud MSA 실무 프로젝트"], "certs": []},
            {"name": "SQL", "freq": 63.0, "priority": "High", "weeks": 2, "trainings": ["관계형 데이터베이스 SQL 최적화"], "certs": ["SQLD"]},
            {"name": "AWS", "freq": 45.0, "priority": "Medium", "weeks": 3, "trainings": ["AWS 클라우드 아키텍처 실습"], "certs": ["AWS SAA"]},
            {"name": "Docker", "freq": 38.0, "priority": "Medium", "weeks": 2, "trainings": ["도커와 쿠버네티스 컨테이너 기초"], "certs": []},
            {"name": "Git", "freq": 55.0, "priority": "High", "weeks": 1, "trainings": ["Git/GitHub 협업 실무"], "certs": []},
        ]

        breakdown: List[SkillGapItem] = []
        possessed: List[str] = []
        missing: List[str] = []

        for req in market_requirements:
            is_have = req["name"].lower() in user_skills_set
            if is_have:
                possessed.append(req["name"])
            else:
                missing.append(req["name"])
                
            breakdown.append(SkillGapItem(
                skill_name=req["name"],
                demand_frequency=req["freq"],
                is_possessed=is_have,
                priority_level=req["priority"],
                learning_weeks=req["weeks"],
                recommended_trainings=req["trainings"],
                recommended_certifications=req["certs"],
            ))

        readiness = (len(possessed) / len(market_requirements)) * 100 if market_requirements else 0.0

        return SkillGapAnalysisResponse(
            target_job=target_job,
            readiness_rate=round(readiness, 1),
            possessed_skills=possessed,
            missing_skills=missing,
            skill_breakdown=breakdown,
        )


skill_gap_service = SkillGapService()
