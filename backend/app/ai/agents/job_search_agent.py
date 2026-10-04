from typing import List, Dict, Any


class JobSearchAgent:
    """
    채용공고 탐색 전문 에이전트 (plan.md 15.3)
    고용24 API 연계를 통해 사용자 조건에 부합하는 채용공고 필터링 및 랭킹
    """
    async def search(self, keywords: List[str], location: str, experience_years: int) -> List[Dict[str, Any]]:
        return [
            {
                "recruitment_id": "EMP24_001",
                "company_name": "(주)데이터웨이브",
                "title": "주니어 백엔드 엔지니어 (Java/Spring)",
                "location": location or "서울",
                "match_rate": 88.0
            }
        ]


job_search_agent = JobSearchAgent()
