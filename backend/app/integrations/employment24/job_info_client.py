from typing import Dict, Any, Optional
from app.core.config import settings


class Employment24JobInfoClient:
    """
    고용24 직업정보 및 직무정보 API 클라이언트 (plan.md 9.2)
    """
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or settings.EMPLOYMENT24_API_KEY

    async def get_job_details(self, job_code: str) -> Dict[str, Any]:
        return {
            "job_code": job_code,
            "job_title": "응용 소프트웨어 개발자",
            "summary": "컴퓨터 알고리즘 및 프로그래밍 언어를 사용하여 시스템/응용 프로그램을 설계·구현",
            "required_aptitudes": ["수리·논리력", "추리력", "집중력"],
            "core_skills": ["Java", "Python", "SQL", "Spring", "Database"]
        }


employment24_job_info_client = Employment24JobInfoClient()
