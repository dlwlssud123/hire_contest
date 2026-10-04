from fastapi import APIRouter, Query
from typing import Optional
from app.schemas.recruitment import RecruitmentResponse, RecruitmentRecommendation

router = APIRouter()


@router.get("/search", response_model=RecruitmentResponse)
async def search_recruitments(
    job_title: str = Query("백엔드 개발자"),
    region: Optional[str] = Query(None),
):
    # Mock recruitment list matched by AI
    items = [
        RecruitmentRecommendation(
            recruitment_id="RECRUIT_2024_01",
            company_name="(주)핀테크랩",
            title="백엔드 서비스 개발자 (Java / Spring)",
            location="서울 강남구",
            company_size="중소기업(성장형)",
            salary_info="연봉 4,000만 ~ 4,800만 원",
            match_score=92.0,
            fit_reasons=["Java 및 SQL 요구조건 충족", "희망 근무지역 일치", "신입 지원 가능"],
            missing_skills=["Spring Cloud", "AWS SAA"],
            detail_url="https://work.go.kr"
        ),
        RecruitmentRecommendation(
            recruitment_id="RECRUIT_2024_02",
            company_name="(주)넥스트커머스",
            title="이커머스 플랫폼 백엔드 개발자",
            location="경기 성남시 분당구",
            company_size="중견기업",
            salary_info="연봉 4,200만 ~ 5,000만 원",
            match_score=85.0,
            fit_reasons=["REST API 개발 역량 부합", "Git 협업 역량 보유"],
            missing_skills=["Kafka", "Redis"],
            detail_url="https://work.go.kr"
        )
    ]
    return RecruitmentResponse(items=items, total=len(items))
