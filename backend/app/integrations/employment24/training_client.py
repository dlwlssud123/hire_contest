from typing import List, Dict, Any, Optional
from app.core.config import settings


class Employment24TrainingClient:
    """
    고용24 직업훈련포털(HRD-Net) 훈련과정 연계 클라이언트 (plan.md 9.4)
    """
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or settings.EMPLOYMENT24_API_KEY

    async def search_courses_by_skill(self, skill_name: str) -> List[Dict[str, Any]]:
        return [
            {
                "course_id": "TR_2024_01",
                "title": f"[K-디지털 트레이닝] {skill_name} 기반 클라우드 백엔드 엔지니어링",
                "institute": "한국소프트웨어산업협회",
                "duration_days": 120,
                "cost_support": "내일배움카드 100% 전액 지원",
                "link": "https://www.hrd.go.kr"
            }
        ]


employment24_training_client = Employment24TrainingClient()
