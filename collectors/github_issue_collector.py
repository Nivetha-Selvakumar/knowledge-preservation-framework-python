from services.github_api_service import GithubApiService


class GithubIssueCollector:

    def __init__(self):

        self.github = GithubApiService()

    def collect(self, token: str, owner: str, repo: str):

        print(f"Collecting issues for " f"{owner}/{repo}")

        issues = self.github.get_issues(token, owner, repo)

        # GitHub's issues API can include
        # Pull Requests.
        #
        # Remove PRs from actual issue collection.

        actual_issues = [issue for issue in issues if "pull_request" not in issue]

        print(f"{len(actual_issues)} " f"issues collected.")

        return actual_issues
