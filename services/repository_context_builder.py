from datetime import datetime


class RepositoryContextBuilder:

    def build(self, repository, commits, issues, pull_requests, readme):

        context = {
            "repository": {
                "id": repository.get("id"),
                "name": repository.get("name"),
                "full_name": repository.get("full_name"),
                "description": repository.get("description"),
                "homepage": repository.get("homepage"),
                "language": repository.get("language"),
                "default_branch": repository.get("default_branch"),
                "visibility": repository.get("visibility"),
                "topics": repository.get("topics", []),
                "stars": repository.get("stargazers_count"),
                "forks": repository.get("forks_count"),
                "watchers": repository.get("watchers_count"),
                "open_issues": repository.get("open_issues_count"),
                "created_at": repository.get("created_at"),
                "updated_at": repository.get("updated_at"),
                "pushed_at": repository.get("pushed_at"),
                "clone_url": repository.get("clone_url"),
                "html_url": repository.get("html_url"),
            },
            "summary": {
                "total_commits": len(commits),
                "total_issues": len(issues),
                "total_pull_requests": len(pull_requests),
                "generated_on": datetime.now().isoformat(),
            },
            "readme": readme,
            "commits": [],
            "issues": [],
            "pull_requests": [],
        }

        # ======================================================
        # ALL COMMITS
        # ======================================================

        for commit in commits:

            commit_data = {
                "sha": commit.get("sha"),
                "message": commit.get("commit", {}).get("message"),
                "author": commit.get("commit", {}).get("author", {}).get("name"),
                "date": commit.get("commit", {}).get("author", {}).get("date"),
                "stats": commit.get("stats", {}),
                "files": [],
            }

            # ==================================================
            # ALL FILES FROM COMMIT
            # ==================================================

            for file in commit.get("files", []):

                commit_data["files"].append(
                    {
                        "filename": file.get("filename"),
                        "status": file.get("status"),
                        "additions": file.get("additions"),
                        "deletions": file.get("deletions"),
                        "changes": file.get("changes"),
                    }
                )

            context["commits"].append(commit_data)

        # ======================================================
        # ALL ISSUES
        # ======================================================

        for issue in issues:

            context["issues"].append(
                {
                    "id": issue.get("id"),
                    "number": issue.get("number"),
                    "title": issue.get("title"),
                    "body": issue.get("body"),
                    "state": issue.get("state"),
                    "created_at": issue.get("created_at"),
                    "updated_at": issue.get("updated_at"),
                    "closed_at": issue.get("closed_at"),
                    "labels": [label.get("name") for label in issue.get("labels", [])],
                    "assignee": (
                        issue.get("assignee", {}).get("login")
                        if issue.get("assignee")
                        else None
                    ),
                }
            )

        # ======================================================
        # ALL PULL REQUESTS
        # ======================================================

        for pr in pull_requests:

            context["pull_requests"].append(
                {
                    "id": pr.get("id"),
                    "number": pr.get("number"),
                    "title": pr.get("title"),
                    "body": pr.get("body"),
                    "state": pr.get("state"),
                    "created_at": pr.get("created_at"),
                    "updated_at": pr.get("updated_at"),
                    "merged_at": pr.get("merged_at"),
                    "source_branch": pr.get("head", {}).get("ref"),
                    "target_branch": pr.get("base", {}).get("ref"),
                    "author": pr.get("user", {}).get("login"),
                }
            )

        return context
