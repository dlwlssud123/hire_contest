from typing import List, Dict, Any, Optional
from app.core.config import settings


class QnetCertClient:
    """
    한국산업인력공단(Q-Net) 국가기술자격 API 클라이언트 (plan.md 9.5)
    """
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or settings.QNET_API_KEY

    async def get_cert_details(self, cert_name: str) -> Dict[str, Any]:
        return {
            "cert_name": cert_name,
            "issuer": "한국산업인력공단",
            "exam_schedule": "연 3회 (정기 기사 시험)",
            "exam_subjects": ["소프트웨어 구축", "데이터베이스 구축", "서버프로그램 구현"],
            "career_linkage": "IT/SW 직무 지원 시 공통 필수 및 가산점 항목"
        }


qnet_cert_client = QnetCertClient()
