from fastapi import APIRouter, Query
from app.services.market_analysis_service import market_analysis_service

router = APIRouter()


@router.get("/insights")
async def get_market_insights(job_title: str = Query("백엔드 개발자")):
    return await market_analysis_service.get_market_insights(job_title)
