from services.github_api_service import GithubApiService


class GithubReadmeCollector:

    def __init__(self):
        self.github = GithubApiService()

    def collect(self, token: str, owner: str, repo: str):
        try:

            return self.github.get_readme(token, owner, repo)
        
        except Exception as exception:

            print(f"README collection failed " f"for {owner}/{repo}: " f"{exception}")

            return None
