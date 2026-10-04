from typing import List, Dict, Any


class EducationAgent:
    """
    교육·자격 탐색 전문 에이전트 (plan.md 15.3)
    부족 역량과 고용24 훈련과정 및 한국산업인력공단 국가기술자격 연계
    """
    async def match_courses_and_certs(self, missing_skills: List[str]) -> Dict[str, Any]:
        return {
            "recommended_trainings": [
                {"course_name": f"{skill} 실무 프로젝트 과정", "provider": "고용24"} for skill in missing_skills
            ],
            "recommended_certifications": [
                {"cert_name": "정보처리기사", "issuer": "한국산업인력공단"}
            ]
        }


education_agent = EducationAgent()
