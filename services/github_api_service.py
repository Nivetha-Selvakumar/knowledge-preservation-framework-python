import requests


class GithubApiService:

    BASE_URL = "https://api.github.com"

    def get_repositories(self, token: str):

        headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
        }

        response = requests.get(f"{self.BASE_URL}/user/repos", headers=headers)

        response.raise_for_status()

        return response.json()

    def get_commits(self, token, owner, repo):
        pass

    def get_issues(self, token, owner, repo):
        pass

    def get_pull_requests(self, token, owner, repo):
        pass
        