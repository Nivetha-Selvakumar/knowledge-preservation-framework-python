from agents.github_agent import GithubAgent


class AgentRegistry:

    def __init__(self):

        self._agents = {}

        self._github_agents = {}

    # ==========================================================
    # NORMAL AGENTS
    # ==========================================================

    def register_agent(self, source: str, agent):

        self._agents[source.lower()] = agent

    def get_agent(self, source: str):

        agent = self._agents.get(source.lower())

        if not agent:

            raise ValueError(f"Unsupported source: {source}")

        return agent

    # ==========================================================
    # GET OR CREATE GITHUB AGENT
    # ==========================================================

    def get_or_create_github_agent(
        self, repository_id: str, owner: str, repository_name: str
    ):

        repository_id = str(repository_id)

        # ------------------------------------------------------
        # EXISTING AGENT
        # ------------------------------------------------------

        existing_agent = self._github_agents.get(repository_id)

        if existing_agent:

            print("=" * 80)
            print("EXISTING GITHUB AGENT FOUND")
            print("=" * 80)

            print(f"Agent ID: " f"{existing_agent.agent_id}")

            return existing_agent

        # ------------------------------------------------------
        # CREATE NEW AGENT
        # ------------------------------------------------------

        print("=" * 80)
        print("CREATING GITHUB REPOSITORY AGENT")
        print("=" * 80)

        print(f"Repository ID : " f"{repository_id}")

        print(f"Repository    : " f"{owner}/{repository_name}")

        agent = GithubAgent(
            repository_id=repository_id, owner=owner, repository_name=repository_name
        )

        self._github_agents[repository_id] = agent

        print(f"GitHub Agent created: " f"{agent.agent_id}")

        return agent

    # ==========================================================
    # GET GITHUB AGENT
    # ==========================================================

    def get_github_agent(self, repository_id: str):

        repository_id = str(repository_id)

        agent = self._github_agents.get(repository_id)

        if agent:

            print(f"GitHub Agent found: " f"{agent.agent_id}")

        else:

            print(f"No GitHub Agent found for " f"repository: {repository_id}")

        return agent

    # ==========================================================
    # REMOVE GITHUB AGENT
    # ==========================================================

    def remove_github_agent(self, repository_id: str):

        return self._github_agents.pop(str(repository_id), None)

    # ==========================================================
    # CHECK AGENT
    # ==========================================================

    def has_github_agent(self, repository_id: str):

        return str(repository_id) in self._github_agents


# ==========================================================
# SINGLE SHARED REGISTRY
# ==========================================================

agent_registry = AgentRegistry()
