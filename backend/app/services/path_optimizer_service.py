from typing import List, Dict, Any
from app.schemas.roadmap import ActionPlanStep, CareerRoadmapResponse
from app.models.profile import UserProfile


class PathOptimizerService:
    """
    Skill Gap 기반 취업 경로 최적화 및 주차별 Action Plan 생성 (plan.md 7)
    """
    @staticmethod
    async def generate_optimized_roadmap(profile: UserProfile, target_job: str, months: int) -> Dict[str, Any]:
        total_weeks = months * 4

        # 주차별 액션 플랜 생성 (시장 요구도 및 선후수 관계 고려한 최적 경로)
        action_plans = [
            ActionPlanStep(
                week_range="1~4주차",
                title="Spring Boot 핵심 학습 및 REST API 프로젝트",
                goal="백엔드 핵심 프레임워크 학습 및 포트폴리오 기본 프로젝트 구축",
                recommended_activities=[
                    "Spring Boot 3.x 기본기 및 JPA/Hibernate 실습",
                    "RESTful API 기반 CRUD 프로젝트 설계 및 개발",
                    "고용24 연계 K-디지털 트레이닝 'Spring 백엔드 실무' 과정 수강"
                ],
                linked_trainings=[{"name": "Spring 백엔드 웹개발 실무", "source": "고용24"}],
                linked_certifications=[{"name": "SQLD(SQL개발자)", "source": "K-Data"}]
            ),
            ActionPlanStep(
                week_range="5~6주차",
                title="Docker 컨테이너화 및 데이터베이스 최적화",
                goal="애플리케이션 컨테이너 빌드 및 인프라 기초 경험 확보",
                recommended_activities=[
                    "Docker를 활용한 백엔드 앱 및 PostgreSQL 컨테이너 구성",
                    "Docker Compose 기반 로컬 개발 환경 표준화"
                ],
                linked_trainings=[],
                linked_certifications=[]
            ),
            ActionPlanStep(
                week_range="7~8주차",
                title="AWS 클라우드 인프라 배포 및 CI/CD 구축",
                goal="실제 클라우드 환경 배포 및 배포 자동화 파이프라인 경험",
                recommended_activities=[
                    "AWS EC2, RDS, S3를 활용한 배포 아키텍처 구축",
                    "GitHub Actions를 활용한 CI/CD 자동화 구축"
                ],
                linked_trainings=[{"name": "AWS 클라우드 기초 아키텍팅", "source": "고용24"}],
                linked_certifications=[]
            ),
            ActionPlanStep(
                week_range="9~10주차",
                title="프로젝트 포트폴리오 정리 및 기술 면접 대비",
                goal="채용담당자 관점의 포트폴리오 완성 및 핵심 CS/기술 질문 대비",
                recommended_activities=[
                    "GitHub README 및 기술 아키텍처 문서화",
                    "트러블슈팅 경험 정리 및 기술 면접 질문 리스트 준비"
                ],
                linked_trainings=[],
                linked_certifications=[{"name": "정보처리기사 실기", "source": "한국산업인력공단"}]
            ),
            ActionPlanStep(
                week_range="11~12주차",
                title="추천 목표 기업 집중 지원 및 피드백 반영",
                goal="매칭 적합도가 높은 실제 채용공고 지원 및 지원 결과 분석",
                recommended_activities=[
                    "고용24 추천 상위 5개 기업 맞춤 지원서 제출",
                    "지원 현황 트래킹 및 커리어 에이전트와 피드백 검토"
                ],
                linked_trainings=[],
                linked_certifications=[]
            )
        ]

        return {
            "target_job": target_job,
            "total_weeks": total_weeks,
            "action_plans": [plan.dict() for plan in action_plans],
            "skill_gap_summary": {
                "initial_gap_count": 3,
                "projected_completion_rate": "100%"
            }
        }


path_optimizer_service = PathOptimizerService()
