from fastapi import APIRouter
from app.api.v1.endpoints import (
    auth,
    profile,
    job_recommend,
    recruitments,
    skill_gap,
    path_optimization,
    simulation,
    market_analysis,
    agent,
    reports,
)

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
api_router.include_router(profile.router, prefix="/profile", tags=["User Profile"])
api_router.include_router(job_recommend.router, prefix="/jobs", tags=["AI Job Recommendation"])
api_router.include_router(recruitments.router, prefix="/recruitments", tags=["Recruitments & Companies"])
api_router.include_router(skill_gap.router, prefix="/skill-gap", tags=["Skill Gap Analysis"])
api_router.include_router(path_optimization.router, prefix="/path", tags=["Career Path Optimization"])
api_router.include_router(simulation.router, prefix="/simulation", tags=["What-if Simulation"])
api_router.include_router(market_analysis.router, prefix="/market", tags=["Labor Market Analytics"])
api_router.include_router(agent.router, prefix="/agent", tags=["AI Career Agent"])
api_router.include_router(reports.router, prefix="/reports", tags=["AI Career Report"])
