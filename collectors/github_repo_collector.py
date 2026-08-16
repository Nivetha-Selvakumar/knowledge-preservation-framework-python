from services.github_api_service import GithubApiService


class GithubRepoCollector:

    def __init__(self):

        self.github = GithubApiService()

    def collect(self, token: str):

        print("Collecting repositories...")

        repositories = self.github.get_repositories(token)

        print(f"{len(repositories)} repositories found.")

        return repositories
