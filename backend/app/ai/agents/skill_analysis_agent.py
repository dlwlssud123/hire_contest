from typing import List, Dict, Any


class SkillAnalysisAgent:
    """
    직무/Skill 분석 전문 에이전트 (plan.md 15.3)
    채용공고 비정형 텍스트에서 기술스택 정규화 및 요구빈도 집계
    """
    async def analyze_skills(self, job_title: str, user_skills: List[str]) -> Dict[str, Any]:
        return {
            "job_title": job_title,
            "core_skills_required": ["Java", "Spring Boot", "SQL", "AWS"],
            "user_possession_rate": 0.65
        }


skill_analysis_agent = SkillAnalysisAgent()
