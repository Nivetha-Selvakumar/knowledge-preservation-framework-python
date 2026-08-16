from services.github_api_service import GithubApiService


class GithubCommitCollector:

    def __init__(self):

        self.github = GithubApiService()

    def collect(self, token: str, owner: str, repo: str):

        print(f"Collecting commits for " f"{owner}/{repo}")

        commits = self.github.get_commits(token, owner, repo)

        commit_details = []

        for commit in commits:

            sha = commit.get("sha")

            if not sha:
                continue

            try:

                details = self.github.get_commit_details(token, owner, repo, sha)

                commit_details.append(details)

            except Exception as exception:

                print(f"Failed to fetch commit " f"{sha}: {exception}")

        print(f"{len(commit_details)} " f"commits collected.")

        return commit_details
