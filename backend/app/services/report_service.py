from typing import Dict, Any
from app.models.profile import UserProfile
from app.services.skill_gap_service import skill_gap_service
from app.services.market_analysis_service import market_analysis_service
from app.services.path_optimizer_service import path_optimizer_service


class ReportService:
    """
    AI 취업 전략 보고서 생성 서비스 (plan.md 12)
    8대 핵심 섹션 통합 보고서 빌더
    """
    @staticmethod
    async def generate_full_report(profile: UserProfile, target_job: str) -> Dict[str, Any]:
        gap_data = await skill_gap_service.analyze_gap(profile, target_job)
        market_data = await market_analysis_service.get_market_insights(target_job)
        roadmap_data = await path_optimizer_service.generate_optimized_roadmap(
            profile, target_job, profile.prep_period_months or 6
        )

        return {
            "title": f"{target_job} 맞춤형 AI 취업 전략 보고서",
            "profile_summary": {
                "major": profile.major,
                "education": profile.education_level,
                "skills": profile.skills,
                "target_location": profile.target_location,
                "prep_period_months": profile.prep_period_months
            },
            "recommended_jobs": [
                {"title": target_job, "match_score": 88.5, "reason": "사용자 적성 및 기술 기반 최적 경로"}
            ],
            "recommended_recruitments": [
                {
                    "company": "(주)클라우드테크",
                    "title": "주니어 백엔드 엔지니어 채용",
                    "match_score": 85.0,
                    "location": "서울 강남구",
                    "reason": "Spring/SQL 기반 개발 요구"
                }
            ],
            "skill_gap_analysis": gap_data.dict(),
            "market_insights": market_data,
            "recommended_education": [
                {"title": "고용24 K-디지털 트레이닝 백엔드 부트캠프", "type": "훈련과정", "duration": "3개월"},
                {"title": "정보처리기사 및 SQLD", "type": "국가기술자격", "agency": "한국산업인력공단"}
            ],
            "career_path": {
                "strategy": "핵심 기술 역량(Spring/AWS) 우선 확보 후 목표 기업 집중 지원",
                "total_weeks": roadmap_data["total_weeks"]
            },
            "action_plans": roadmap_data["action_plans"]
        }


report_service = ReportService()
