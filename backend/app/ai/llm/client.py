from typing import Optional
from app.core.config import settings


class LLMClient:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or settings.OPENAI_API_KEY
        self.default_model = settings.DEFAULT_LLM_MODEL

    async def generate_response(self, system_prompt: str, user_prompt: str) -> str:
        # LLM client implementation placeholder (OpenAI / Anthropic)
        if not self.api_key:
            return "AI 응답 생성기: API 키가 설정되지 않은 개발 모드 응답입니다."
        
        # In real execution, call LangChain or OpenAI client
        return f"AI 분석 결과: {user_prompt}에 대한 맞춤형 조언을 제공합니다."


llm_client = LLMClient()
