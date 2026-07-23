from services.github_api_service import GithubApiService


class GithubPRCollector:

    def __init__(self):
        self.github = GithubApiService()

    def collect(self, token: str, owner: str, repo: str):

        return self.github.get_pull_requests(token, owner, repo)
