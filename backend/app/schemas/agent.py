from typing import List, Optional, Dict, Any
from pydantic import BaseModel


class ChatMessage(BaseModel):
    role: str   # "user" | "assistant" | "system"
    content: str


class AgentChatRequest(BaseModel):
    user_id: int
    message: str
    conversation_history: List[ChatMessage] = []
    current_roadmap_id: Optional[int] = None


class AgentChatResponse(BaseModel):
    reply: str
    suggested_actions: List[str] = []
    updated_roadmap: Optional[Dict[str, Any]] = None
    data_sources_used: List[str] = []
