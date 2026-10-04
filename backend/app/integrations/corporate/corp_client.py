from typing import Dict, Any, Optional
from app.core.config import settings


class CorporateDataClient:
    """
    기업 공공데이터 (기업개요, 업종, 기업규모 등) API 연계 (plan.md 9.6)
    """
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or settings.PUBLIC_DATA_PORTAL_KEY

    async def get_company_profile(self, company_name: str) -> Dict[str, Any]:
        return {
            "company_name": company_name,
            "business_number": "123-45-67890",
            "company_type": "중소벤처기업 / 이노비즈 인증",
            "employees_count": 45,
            "sales_amount": "50억 원",
            "main_business": "클라우드 SaaS 솔루션 개발"
        }


corporate_data_client = CorporateDataClient()
