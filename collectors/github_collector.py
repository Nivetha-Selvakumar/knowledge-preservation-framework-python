from collectors.github_repo_collector import GithubRepoCollector
from collectors.github_commit_collector import GithubCommitCollector
from collectors.github_issue_collector import GithubIssueCollector
from collectors.github_pr_collector import GithubPRCollector


class GithubCollector:

    def __init__(self):

        self.repo_collector = GithubRepoCollector()
        self.commit_collector = GithubCommitCollector()
        self.issue_collector = GithubIssueCollector()
        self.pr_collector = GithubPRCollector()

    def collect(self, request):

        print("GitHub Agent Activated")

        token = request.githubToken

        repositories = self.repo_collector.collect(token)

        return {
            "status": "SUCCESS",
            "repositoryCount": len(repositories),
            "repositories": repositories,
        }
