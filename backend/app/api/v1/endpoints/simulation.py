from fastapi import APIRouter
from app.schemas.simulation import SimulationRequest, SimulationResponse
from app.services.simulation_service import simulation_service

router = APIRouter()


@router.post("/simulate", response_model=SimulationResponse)
async def run_simulation(req: SimulationRequest):
    return await simulation_service.simulate(
        user_id=req.user_id,
        target_job=req.target_job,
        selected_activities=req.selected_activities
    )
