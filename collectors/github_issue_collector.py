from services.github_api_service import GithubApiService


class GithubIssueCollector:

    def __init__(self):
        self.github = GithubApiService()

    def collect(self, token: str, owner: str, repo: str):

        return self.github.get_issues(token, owner, repo)
