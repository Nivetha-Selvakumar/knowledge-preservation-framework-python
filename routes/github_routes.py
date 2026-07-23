from fastapi import APIRouter

from agents.central_agent import CentralAgent
from models.github_request import GithubRequest

router = APIRouter(prefix="/github", tags=["GitHub"])


@router.post("/sync")
def sync(request: GithubRequest):

    central = CentralAgent()

    return central.activate_github(request)
