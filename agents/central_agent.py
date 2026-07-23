from agents.github_agent import GithubAgent


class CentralAgent:

    def activate_github(self, request):

        github = GithubAgent()

        return github.activate(request)
