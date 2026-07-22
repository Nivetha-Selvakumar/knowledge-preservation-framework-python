from agents.github_agent import GithubAgent

class CentralAgent:

    def __init__(self):

        self.github = GithubAgent()

    def sync_github(self):

        return self.github.collect()