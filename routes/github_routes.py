from fastapi import APIRouter

from agents.central_agent import CentralAgent

router = APIRouter(
    prefix="/github",
    tags=["GitHub"]
)

central_agent = CentralAgent()

@router.post("/sync")
def sync():

    return central_agent.sync_github()