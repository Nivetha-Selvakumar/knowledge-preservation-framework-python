from datetime import datetime


class KnowledgeChunker:

    def __init__(self, chunk_size=5):

        self.chunk_size = chunk_size

    # ==========================================================
    # Split a list into chunks
    # ==========================================================

    def chunk_list(self, items):

        if not items:

            return []

        return [
            items[i : i + self.chunk_size]
            for i in range(0, len(items), self.chunk_size)
        ]

    # ==========================================================
    # Create LLM chunks
    # ==========================================================

    def create_activity_chunks(self, context):

        chunks = []

        repository = context.get("repository", {})

        readme = context.get("readme")

        # ======================================================
        # ALL COMMITS
        # ======================================================

        commits = context.get("commits", [])

        commit_chunks = self.chunk_list(commits)

        for index, commit_chunk in enumerate(commit_chunks):

            chunks.append(
                {
                    "repository": repository,
                    "summary": {
                        "total_commits": len(commit_chunk),
                        "total_issues": 0,
                        "total_pull_requests": 0,
                    },
                    "readme": readme if index == 0 else None,
                    "commits": commit_chunk,
                    "issues": [],
                    "pull_requests": [],
                    "activity_type": "commits",
                    "chunk_number": index + 1,
                }
            )

        # ======================================================
        # ALL ISSUES
        # ======================================================

        issues = context.get("issues", [])

        issue_chunks = self.chunk_list(issues)

        for index, issue_chunk in enumerate(issue_chunks):

            chunks.append(
                {
                    "repository": repository,
                    "summary": {
                        "total_commits": 0,
                        "total_issues": len(issue_chunk),
                        "total_pull_requests": 0,
                    },
                    "readme": None,
                    "commits": [],
                    "issues": issue_chunk,
                    "pull_requests": [],
                    "activity_type": "issues",
                    "chunk_number": index + 1,
                }
            )

        # ======================================================
        # ALL PULL REQUESTS
        # ======================================================

        pull_requests = context.get("pull_requests", [])

        pr_chunks = self.chunk_list(pull_requests)

        for index, pr_chunk in enumerate(pr_chunks):

            chunks.append(
                {
                    "repository": repository,
                    "summary": {
                        "total_commits": 0,
                        "total_issues": 0,
                        "total_pull_requests": len(pr_chunk),
                    },
                    "readme": None,
                    "commits": [],
                    "issues": [],
                    "pull_requests": pr_chunk,
                    "activity_type": "pull_requests",
                    "chunk_number": index + 1,
                }
            )

        # ======================================================
        # Add total chunk information
        # ======================================================

        total_chunks = len(chunks)

        for index, chunk in enumerate(chunks):

            chunk["chunk_number"] = index + 1

            chunk["total_chunks"] = total_chunks

        return chunks
