from fastapi import APIRouter, HTTPException, Request
import traceback

from agents.registry import agent_registry

router = APIRouter(prefix="/github", tags=["GitHub"])


# ==========================================================
# CREATE / EXECUTE GITHUB REPOSITORY AGENT
# ==========================================================


@router.post("/repositories/{repository_id}/sync")
async def sync_github_repository(repository_id: str, request: Request):

    print("=" * 80)
    print("GITHUB REPOSITORY AGENT REQUEST")
    print("=" * 80)

    print(f"Repository ID: " f"{repository_id}")

    try:

        # ======================================================
        # READ REQUEST BODY
        # ======================================================

        body = await request.json()

        print(f"Request body: " f"{body}")

        # ======================================================
        # READ REQUIRED VALUES
        # ======================================================

        token = body.get("token")

        owner = body.get("owner")

        repository_name = body.get("repositoryName")

        # ------------------------------------------------------
        # Webhook URL
        #
        # Java can send this value.
        # Example:
        #
        # https://xxxxx-8001.app.github.dev/github/webhook
        # ------------------------------------------------------

        webhook_url = body.get("webhookUrl")

        # ======================================================
        # VALIDATION
        # ======================================================

        if not token:

            raise HTTPException(status_code=400, detail="GitHub token is required")

        if not owner:

            raise HTTPException(status_code=400, detail="Repository owner is required")

        if not repository_name:

            raise HTTPException(status_code=400, detail="Repository name is required")

        if not webhook_url:

            raise HTTPException(status_code=400, detail="Webhook URL is required")

        print(f"Repository: " f"{owner}/{repository_name}")

        print(f"Webhook URL: " f"{webhook_url}")

        # ======================================================
        # GET OR CREATE AGENT
        # ======================================================

        print("=" * 80)
        print("GETTING / CREATING GITHUB AGENT")
        print("=" * 80)

        agent = agent_registry.get_or_create_github_agent(
            repository_id=str(repository_id),
            owner=owner,
            repository_name=repository_name,
        )

        if not agent:

            raise HTTPException(status_code=500, detail="Failed to create GitHub agent")

        print(f"Agent ID: " f"{agent.agent_id}")

        # ======================================================
        # ACTIVATE AGENT
        #
        # This registers the GitHub webhook.
        #
        # It is safe to call repeatedly because
        # create_webhook() checks whether the webhook
        # already exists.
        # ======================================================

        print("=" * 80)
        print("ACTIVATING GITHUB AGENT")
        print("=" * 80)

        activation_response = agent.activate(token=token, webhook_url=webhook_url)

        print(f"Activation response: " f"{activation_response}")

        # ======================================================
        # INITIAL EXECUTION
        #
        # This happens only during the initial Sync.
        # After this, GitHub webhook events will trigger
        # monitor_event().
        # ======================================================

        print("=" * 80)
        print("RUNNING INITIAL GITHUB COLLECTION")
        print("=" * 80)

        result = agent.execute(token)

        # ======================================================
        # RESPONSE
        # ======================================================

        print("=" * 80)
        print("GITHUB AGENT EXECUTION COMPLETED")
        print("=" * 80)

        return {
            "status": "ACTIVE",
            "agentId": agent.agent_id,
            "repositoryId": str(repository_id),
            "repository": f"{owner}/{repository_name}",
            "webhookId": agent.webhook_id,
            "webhookUrl": webhook_url,
            "initialCollection": result,
            "message": "GitHub repository agent activated and initial synchronization completed",
        }

    except HTTPException:

        raise

    except Exception as exception:

        print("=" * 80)
        print("GITHUB AGENT EXECUTION FAILED")
        print("=" * 80)

        print(f"Error: " f"{exception}")

        traceback.print_exc()

        raise HTTPException(status_code=500, detail=str(exception))


# ==========================================================
# GITHUB WEBHOOK
# ==========================================================


@router.post("/webhook")
async def github_webhook(request: Request):

    print("=" * 80)
    print("GITHUB WEBHOOK RECEIVED")
    print("=" * 80)

    try:

        # ======================================================
        # GITHUB HEADERS
        # ======================================================

        event_type = request.headers.get("X-GitHub-Event")

        delivery_id = request.headers.get("X-GitHub-Delivery")

        print(f"Event Type : " f"{event_type}")

        print(f"Delivery ID: " f"{delivery_id}")

        # ======================================================
        # READ PAYLOAD
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

        print(f"Repository ID: " f"{repository_id}")

        print(f"Repository: " f"{owner}/{repository_name}")

        # ======================================================
        # FIND AGENT
        # ======================================================

        agent = agent_registry.get_github_agent(repository_id)

        if not agent:

            print(f"No active agent found for " f"repository {repository_id}")

            return {
                "status": "IGNORED",
                "repositoryId": repository_id,
                "message": "No active repository agent found",
            }

        # ======================================================
        # SEND EVENT TO AGENT
        # ======================================================

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

        print(f"Error: " f"{exception}")

        traceback.print_exc()

        raise HTTPException(status_code=500, detail=str(exception))
