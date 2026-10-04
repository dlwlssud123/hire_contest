from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.job import JobRecommendation, JobRecommendationResponse
from app.models.profile import UserProfile


class JobMatchService:
    """
    적성 적합도 & 현재 준비도 기반 AI 직무 추천 서비스 (plan.md 5.2)
    """
    @staticmethod
    async def recommend_jobs(db: AsyncSession, profile: UserProfile) -> JobRecommendationResponse:
        # Mock logic or AI algorithm matching user skills and psych traits to job roles
        mock_recommendations = [
            JobRecommendation(
                job_code="SW_DEV_001",
                title="백엔드 개발자 (Backend Developer)",
                category="IT / 소프트웨어",
                aptitude_match_score=88.5,
                readiness_score=72.0,
                matching_reason="논리적 문제해결 적성 우수 및 Python/SQL 기본 역량 보유. Spring/AWS 보완 시 적합도 극대화.",
                key_skills=["Java", "Spring Boot", "SQL", "AWS", "Docker", "Git"]
            ),
            JobRecommendation(
                job_code="DATA_ENG_002",
                title="데이터 엔지니어 (Data Engineer)",
                category="데이터 / AI",
                aptitude_match_score=82.0,
                readiness_score=65.0,
                matching_reason="데이터 분석 및 파이프라인 관심도 부합, SQL 기초 역량 연계 가능.",
                key_skills=["Python", "SQL", "Spark", "Kafka", "Airflow"]
            ),
            JobRecommendation(
                job_code="DEVOPS_003",
                title="클라우드 데브옵스 엔지니어",
                category="클라우드 / 인프라",
                aptitude_match_score=75.0,
                readiness_score=50.0,
                matching_reason="인프라 자동화에 대한 적성 부합하나 컨테이너 및 CI/CD 추가 역량 학습 필요.",
                key_skills=["Linux", "Docker", "Kubernetes", "AWS", "Terraform"]
            )
        ]
        return JobRecommendationResponse(
            user_id=profile.user_id,
            recommendations=mock_recommendations
        )


job_match_service = JobMatchService()
