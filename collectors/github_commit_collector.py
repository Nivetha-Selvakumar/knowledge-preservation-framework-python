from services.github_api_service import GithubApiService


class GithubCommitCollector:

    def __init__(self):
        self.github = GithubApiService()

    def collect(self, token: str, owner: str, repo: str):

        return self.github.get_commits(token, owner, repo)
