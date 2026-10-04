from typing import List, Dict, Any, Optional
from app.ai.llm.client import llm_client
from app.ai.llm.prompts import CAREER_AGENT_SYSTEM_PROMPT
from app.schemas.agent import AgentChatResponse


class CareerAgent:
    """
    대화형 총괄 AI Career Agent (plan.md 11 & 15.3)
    사용자와 지속적으로 대화하며 취업 전략 수정 및 Dynamic Re-planning 수행
    """
    def __init__(self):
        self.system_prompt = CAREER_AGENT_SYSTEM_PROMPT

    async def handle_message(
        self,
        user_id: int,
        message: str,
        history: List[Dict[str, str]],
        current_roadmap_id: Optional[int] = None
    ) -> AgentChatResponse:
        # Example dynamic response logic
        if "3개월" in message or "기간" in message:
            reply_text = (
                "준비 가능 기간(3개월)에 맞춰 로드맵을 재구성했습니다. "
                "우선순위가 비교적 낮은 일반 자격증 대비를 제외하고, "
                "채용공고 출현 빈도가 높은 Spring Boot 실전 프로젝트와 AWS 클라우드 배포에 집중하도록 Action Plan을 업데이트했습니다."
            )
            suggested_actions = ["3개월 압축 로드맵 확인하기", "고용24 단기 부트캠프 보기", "맞춤형 모의 면접 질문 보기"]
        elif "서울" in message or "지역" in message:
            reply_text = (
                "희망 근무 지역을 '서울 전체'로 확대하여 최신 고용24 채용공고를 재탐색했습니다. "
                "강남/판교권 테크 기업 공고 15건이 추가 추천 목록에 반영되었습니다."
            )
            suggested_actions = ["추천 채용공고 리스트 확인", "지역별 평균 임금 비교", "취업 전략 보고서 다시 받기"]
        else:
            reply_text = (
                f"문의하신 내용('{message}')을 바탕으로 노동시장 데이터와 사용자의 Skill Gap을 분석했습니다. "
                "목표 직무 달성을 위해 현재 가장 효율적인 액션 플랜을 제시해 드립니다."
            )
            suggested_actions = ["Skill Gap 상세 분석", "추천 국비 훈련과정 확인", "What-if 시뮬레이션 실행"]

        return AgentChatResponse(
            reply=reply_text,
            suggested_actions=suggested_actions,
            data_sources_used=["고용24 채용정보", "고용24 직무정보", "K-디지털 훈련과정 DB"]
        )


career_agent = CareerAgent()
