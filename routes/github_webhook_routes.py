from fastapi import APIRouter, Request, HTTPException

import traceback

from agents.registry import agent_registry

router = APIRouter(prefix="/github", tags=["GitHub Webhook"])


@router.post("/webhook")
async def github_webhook(request: Request):

    try:

        # ======================================================
        # HEADERS
        # ======================================================

        event_type = request.headers.get("X-GitHub-Event")

        delivery_id = request.headers.get("X-GitHub-Delivery")

        print("=" * 80)
        print("GITHUB WEBHOOK RECEIVED")
        print("=" * 80)

        print(f"Event Type : {event_type}")

        print(f"Delivery ID: {delivery_id}")

        # ======================================================
        # PAYLOAD
        # ======================================================

        payload = await request.json()

        # ======================================================
        # REPOSITORY
        # ======================================================

        repository = payload.get("repository")

        if not repository:

            raise HTTPException(
                status_code=400, detail="Repository information not found"
            )

        repository_id = str(repository.get("id"))

        repository_name = repository.get("name")

        owner = repository.get("owner", {}).get("login")

        print(f"Repository ID : " f"{repository_id}")

        print(f"Repository    : " f"{owner}/{repository_name}")

        # ======================================================
        # GET EXISTING AGENT
        # ======================================================

        print("Searching for GitHub Agent...")

        agent = agent_registry.get_github_agent(repository_id)

        if not agent:

            print(f"No active agent found for " f"repository {repository_id}")

            return {
                "status": "IGNORED",
                "message": "No active repository agent found",
                "repositoryId": repository_id,
            }

        # ======================================================
        # SEND EVENT TO AGENT
        # ======================================================

        print(f"Agent found: " f"{agent.agent_id}")

        result = agent.monitor_event(event_type=event_type, payload=payload)

        print("=" * 80)
        print("WEBHOOK PROCESSED")
        print("=" * 80)

        return result

    except HTTPException:

        raise

    except Exception as exception:

        print("=" * 80)
        print("WEBHOOK PROCESSING FAILED")
        print("=" * 80)

        print(f"Error: {exception}")

        traceback.print_exc()

        raise HTTPException(status_code=500, detail=str(exception))
