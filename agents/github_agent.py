from collectors.github_collector import GithubCollector
from services.github_api_service import GithubApiService


class GithubAgent:

    def __init__(self, repository_id: str, owner: str, repository_name: str):

        # ======================================================
        # AGENT INFORMATION
        # ======================================================

        self.repository_id = str(repository_id)

        self.owner = owner

        self.repository_name = repository_name

        self.agent_id = f"github-agent-{self.repository_id}"

        self.status = "ACTIVE"

        # ======================================================
        # SERVICES
        # ======================================================

        self.collector = GithubCollector()

        self.github_api = GithubApiService()

        # Token is stored after initial activation.
        # It is required when a webhook event arrives.
        self.github_token = None

        # Webhook information
        self.webhook_id = None

        self.webhook_url = None

        # ======================================================
        # AGENT CREATION LOG
        # ======================================================

        print("=" * 80)
        print("GITHUB AGENT CREATED")
        print("=" * 80)

        print(f"Agent ID      : " f"{self.agent_id}")

        print(f"Repository ID : " f"{self.repository_id}")

        print(f"Repository    : " f"{self.owner}/{self.repository_name}")

        print("=" * 80)

    # ==========================================================
    # ACTIVATE AGENT
    # ==========================================================

    def activate(self, token: str, webhook_url: str):

        print("=" * 80)
        print("ACTIVATING GITHUB AGENT")
        print("=" * 80)

        if not token:

            raise ValueError("GitHub token is required")

        if not webhook_url:

            raise ValueError("GitHub webhook URL is required")

        # ------------------------------------------------------
        # Store token
        # ------------------------------------------------------

        self.github_token = token

        # ------------------------------------------------------
        # Store webhook URL
        # ------------------------------------------------------

        self.webhook_url = webhook_url

        print(f"Agent ID     : " f"{self.agent_id}")

        print(f"Webhook URL  : " f"{self.webhook_url}")

        # ------------------------------------------------------
        # Register webhook
        #
        # GithubApiService.create_webhook()
        # already checks whether it exists.
        # ------------------------------------------------------

        webhook = self.github_api.create_webhook(
            token=token,
            owner=self.owner,
            repository_name=self.repository_name,
            webhook_url=webhook_url,
        )

        # ------------------------------------------------------
        # Save webhook ID
        # ------------------------------------------------------

        if webhook:

            self.webhook_id = webhook.get("id")

        # ------------------------------------------------------
        # Agent ACTIVE
        # ------------------------------------------------------

        self.status = "ACTIVE"

        print("=" * 80)
        print("GITHUB AGENT ACTIVATED")
        print("=" * 80)

        print(f"Agent ID     : " f"{self.agent_id}")

        print(f"Webhook ID   : " f"{self.webhook_id}")

        print(f"Status       : " f"{self.status}")

        print("=" * 80)

        return {
            "status": "ACTIVE",
            "agentId": self.agent_id,
            "repositoryId": self.repository_id,
            "repository": self.repository_name,
            "webhookId": self.webhook_id,
            "webhookUrl": self.webhook_url,
            "message": "GitHub repository agent activated successfully",
        }

    # ==========================================================
    # INITIAL EXECUTION
    # ==========================================================

    def execute(self, token: str):

        print("=" * 80)
        print("GITHUB AGENT EXECUTION")
        print("=" * 80)

        print(f"Agent ID: " f"{self.agent_id}")

        print(f"Repository: " f"{self.owner}/{self.repository_name}")

        if not token:

            raise ValueError("GitHub token is required")

        # ------------------------------------------------------
        # Save token
        # ------------------------------------------------------

        self.github_token = token

        # ------------------------------------------------------
        # Collect repository
        # ------------------------------------------------------

        result = self.collector.collect(
            token=token, owner=self.owner, repository_name=self.repository_name
        )

        print("=" * 80)
        print("GITHUB AGENT INITIAL EXECUTION COMPLETED")
        print("=" * 80)

        return result

    # ==========================================================
    # WEBHOOK EVENT
    # ==========================================================

    def monitor_event(self, event_type: str, payload: dict):

        print("=" * 80)
        print("GITHUB AGENT MONITOR EVENT")
        print("=" * 80)

        print(f"Agent ID   : " f"{self.agent_id}")

        print(f"Event Type : " f"{event_type}")

        print(f"Repository : " f"{self.owner}/{self.repository_name}")

        # ------------------------------------------------------
        # PUSH
        # ------------------------------------------------------

        if event_type == "push":

            return self.handle_push(payload)

        # ------------------------------------------------------
        # PULL REQUEST
        # ------------------------------------------------------

        if event_type == "pull_request":

            return self.handle_pull_request(payload)

        # ------------------------------------------------------
        # ISSUES
        # ------------------------------------------------------

        if event_type == "issues":

            return self.handle_issue(payload)

        # ------------------------------------------------------
        # UNKNOWN EVENT
        # ------------------------------------------------------

        print(f"Unsupported GitHub event: " f"{event_type}")

        return {
            "status": "IGNORED",
            "agentId": self.agent_id,
            "event": event_type,
            "message": "Unsupported GitHub event",
        }

    # ==========================================================
    # PUSH EVENT
    # ==========================================================

    def handle_push(self, payload: dict):

        print("=" * 80)
        print("GITHUB PUSH EVENT")
        print("=" * 80)

        ref = payload.get("ref")

        commits = payload.get("commits", [])

        repository = payload.get("repository", {})

        print(f"Reference : " f"{ref}")

        print(f"New commits : " f"{len(commits)}")

        # ------------------------------------------------------
        # Process event
        # ------------------------------------------------------

        result = self.process_repository_change(event_type="push", payload=payload)

        return {
            "status": "RECEIVED",
            "agentId": self.agent_id,
            "event": "push",
            "reference": ref,
            "commitCount": len(commits),
            "repository": repository.get("name"),
            "knowledgeUpdate": result,
            "message": "Push event received and processed",
        }

    # ==========================================================
    # PULL REQUEST EVENT
    # ==========================================================

    def handle_pull_request(self, payload: dict):

        print("=" * 80)
        print("GITHUB PULL REQUEST EVENT")
        print("=" * 80)

        action = payload.get("action")

        pull_request = payload.get("pull_request", {})

        pr_number = pull_request.get("number")

        title = pull_request.get("title")

        merged = pull_request.get("merged", False)

        source_branch = pull_request.get("head", {}).get("ref")

        target_branch = pull_request.get("base", {}).get("ref")

        print(f"Pull Request #" f"{pr_number}")

        print(f"Action         : " f"{action}")

        print(f"Title          : " f"{title}")

        print(f"Source Branch  : " f"{source_branch}")

        print(f"Target Branch  : " f"{target_branch}")

        print(f"Merged         : " f"{merged}")

        # ======================================================
        # MERGED PR
        # ======================================================

        if action == "closed" and merged:

            print("=" * 80)
            print("MERGED PULL REQUEST DETECTED")
            print("=" * 80)

            print(f"PR Number : " f"{pr_number}")

            print(f"Source    : " f"{source_branch}")

            print(f"Target    : " f"{target_branch}")

            # --------------------------------------------------
            # Update repository knowledge
            # --------------------------------------------------

            knowledge_result = self.process_repository_change(
                event_type="pull_request_merged", payload=payload
            )

            return {
                "status": "RECEIVED",
                "agentId": self.agent_id,
                "event": "pull_request",
                "action": action,
                "pullRequestNumber": pr_number,
                "title": title,
                "sourceBranch": source_branch,
                "targetBranch": target_branch,
                "merged": True,
                "knowledgeUpdate": knowledge_result,
                "message": "Merged pull request detected and processed",
            }

        # ======================================================
        # NORMAL PR EVENT
        # ======================================================

        knowledge_result = self.process_repository_change(
            event_type="pull_request", payload=payload
        )

        return {
            "status": "RECEIVED",
            "agentId": self.agent_id,
            "event": "pull_request",
            "action": action,
            "pullRequestNumber": pr_number,
            "title": title,
            "sourceBranch": source_branch,
            "targetBranch": target_branch,
            "merged": merged,
            "knowledgeUpdate": knowledge_result,
            "message": "Pull request event received and processed",
        }

    # ==========================================================
    # ISSUE EVENT
    # ==========================================================

    def handle_issue(self, payload: dict):

        print("=" * 80)
        print("GITHUB ISSUE EVENT")
        print("=" * 80)

        action = payload.get("action")

        issue = payload.get("issue", {})

        issue_number = issue.get("number")

        title = issue.get("title")

        print(f"Issue #{issue_number}")

        print(f"Action: {action}")

        print(f"Title: {title}")

        # ------------------------------------------------------
        # Update knowledge
        # ------------------------------------------------------

        knowledge_result = self.process_repository_change(
            event_type="issues", payload=payload
        )

        return {
            "status": "RECEIVED",
            "agentId": self.agent_id,
            "event": "issues",
            "action": action,
            "issueNumber": issue_number,
            "title": title,
            "knowledgeUpdate": knowledge_result,
            "message": "Issue event received and processed",
        }

    # ==========================================================
    # PROCESS REPOSITORY CHANGE
    # ==========================================================

    def process_repository_change(self, event_type: str, payload: dict):

        print("=" * 80)
        print("PROCESSING REPOSITORY CHANGE")
        print("=" * 80)

        print(f"Event       : " f"{event_type}")

        print(f"Repository  : " f"{self.owner}/{self.repository_name}")

        # ------------------------------------------------------
        # Check GitHub token
        # ------------------------------------------------------

        if not self.github_token:

            print("GitHub token is not available.")

            return {"status": "FAILED", "message": "GitHub token is not available"}

        try:

            # --------------------------------------------------
            # Recollect repository knowledge
            #
            # This uses your existing collector.
            # It collects all commits, issues, PRs and README.
            # --------------------------------------------------

            result = self.collector.collect(
                token=self.github_token,
                owner=self.owner,
                repository_name=self.repository_name,
            )

            print("=" * 80)
            print("REPOSITORY KNOWLEDGE UPDATED")
            print("=" * 80)

            return {
                "status": "UPDATED",
                "event": event_type,
                "repository": self.repository_name,
                "result": result,
            }

        except Exception as exception:

            print("=" * 80)
            print("REPOSITORY KNOWLEDGE UPDATE FAILED")
            print("=" * 80)

            print(f"Error: " f"{exception}")

            return {"status": "FAILED", "event": event_type, "message": str(exception)}
