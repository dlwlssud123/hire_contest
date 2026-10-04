from fastapi import APIRouter
from app.schemas.agent import AgentChatRequest, AgentChatResponse
from app.ai.agents.career_agent import career_agent

router = APIRouter()


@router.post("/chat", response_model=AgentChatResponse)
async def chat_with_agent(req: AgentChatRequest):
    return await career_agent.handle_message(
        user_id=req.user_id,
        message=req.message,
        history=[msg.dict() for msg in req.conversation_history],
        current_roadmap_id=req.current_roadmap_id
    )
