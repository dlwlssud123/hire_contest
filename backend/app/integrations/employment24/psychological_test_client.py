from typing import Dict, Any, Optional
from app.core.config import settings


class Employment24PsychTestClient:
    """
    고용24 직업심리검사(흥미/적성/직업가치관) 연동 클라이언트 (plan.md 9.3)
    """
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or settings.EMPLOYMENT24_API_KEY

    async def get_test_results(self, test_user_id: str) -> Dict[str, Any]:
        return {
            "interest_type": "탐구형(I) / 관습형(C)",
            "top_aptitudes": ["수리력", "공간지각력", "추리력"],
            "core_values": ["전문성 추구", "성취감", "자율성"]
        }


employment24_psych_test_client = Employment24PsychTestClient()
