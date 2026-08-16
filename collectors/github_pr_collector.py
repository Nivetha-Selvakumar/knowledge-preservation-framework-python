from services.github_api_service import GithubApiService


class GithubPRCollector:

    def __init__(self):

        self.github = GithubApiService()

    def collect(self, token: str, owner: str, repo: str):

        print(f"Collecting pull requests for " f"{owner}/{repo}")

        pull_requests = self.github.get_pull_requests(token, owner, repo)

        print(f"{len(pull_requests)} " f"pull requests collected.")

        return pull_requests
