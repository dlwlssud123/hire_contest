from typing import List
from app.schemas.simulation import SimulationActivity, SimulationResponse


class SimulationService:
    """
    What-if 취업 시뮬레이션 서비스 (plan.md 8)
    특정 학습/자격/프로젝트 활동 시 취업 준비도 점수 변화 예측
    """
    @staticmethod
    async def simulate(user_id: int, target_job: str, selected_activities: List[str]) -> SimulationResponse:
        current_readiness = 58.0
        
        activity_database = {
            "Spring 프로젝트 추가": {"duration": 4, "delta": 18.0, "desc": "채용 시장 핵심 요구 스킬(71%) 확보로 준비도 대폭 상승"},
            "정보처리기사 취득": {"duration": 8, "delta": 6.0, "desc": "공공/금융 및 SI 기업 지원 필수 기본 요건 충족"},
            "Docker 학습": {"duration": 2, "delta": 8.0, "desc": "컨테이너 가상화 기초 이해로 기술 적합도 개선"},
            "AWS 프로젝트 배포": {"duration": 5, "delta": 12.0, "desc": "클라우드 실무 배포 역량 확보로 중견/스타트업 우대요건 충족"},
        }

        results: List[SimulationActivity] = []
        running_score = current_readiness
        total_weeks = 0

        for act in selected_activities:
            info = activity_database.get(act, {"duration": 2, "delta": 5.0, "desc": "추가 역량 획득"})
            before = running_score
            running_score = min(100.0, running_score + info["delta"])
            total_weeks += info["duration"]
            
            results.append(SimulationActivity(
                activity_name=act,
                duration_weeks=info["duration"],
                readiness_before=before,
                readiness_after=running_score,
                score_delta=info["delta"],
                description=info["desc"]
            ))

        return SimulationResponse(
            current_readiness=current_readiness,
            projected_readiness=running_score,
            total_duration_weeks=total_weeks,
            simulation_results=results
        )


simulation_service = SimulationService()
