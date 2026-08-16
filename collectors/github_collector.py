from collectors.github_repo_collector import GithubRepoCollector
from collectors.github_commit_collector import GithubCommitCollector
from collectors.github_issue_collector import GithubIssueCollector
from collectors.github_pr_collector import GithubPRCollector
from collectors.github_readme_collector import GithubReadmeCollector

from services.repository_context_builder import RepositoryContextBuilder
from services.knowledge_chunker import KnowledgeChunker

from agents.central_agent import CentralAgent

from storage.markdown_writer import MarkdownWriter


class GithubCollector:

    def __init__(self):

        # ======================================================
        # Collectors
        # ======================================================

        self.repo_collector = GithubRepoCollector()

        self.commit_collector = GithubCommitCollector()

        self.issue_collector = GithubIssueCollector()

        self.pr_collector = GithubPRCollector()

        self.readme_collector = GithubReadmeCollector()

        # ======================================================
        # Context Builder
        # ======================================================

        self.context_builder = RepositoryContextBuilder()

        # ======================================================
        # Central Agent
        # ======================================================

        self.central_agent = CentralAgent()

        # ======================================================
        # Knowledge Chunker
        # ======================================================

        self.chunker = KnowledgeChunker(chunk_size=5)

        # ======================================================
        # Markdown Writer
        # ======================================================

        self.markdown_writer = MarkdownWriter()

    # ==========================================================
    # COLLECT ONE REPOSITORY
    # ==========================================================

    def collect(self, token: str, owner: str, repository_name: str):

        print("=" * 80)
        print("GITHUB REPOSITORY COLLECTOR")
        print("=" * 80)

        # ======================================================
        # Validation
        # ======================================================

        if not token:

            raise ValueError("GitHub token is required")

        if not owner:

            raise ValueError("Repository owner is required")

        if not repository_name:

            raise ValueError("Repository name is required")

        print(f"Repository: " f"{owner}/{repository_name}")

        # ======================================================
        # 1. REPOSITORY
        # ======================================================

        print("-" * 80)
        print("1. Collecting Repository Details")
        print("-" * 80)

        repository = self.repo_collector.collect_repository(
            token, owner, repository_name
        )

        if not repository:

            raise ValueError("Repository details not found")

        # ======================================================
        # 2. ALL COMMITS
        # ======================================================

        print("-" * 80)
        print("2. Collecting ALL Commits")
        print("-" * 80)

        commits = self.commit_collector.collect(token, owner, repository_name)

        print(f"Total commits collected: " f"{len(commits)}")

        # ======================================================
        # 3. ALL ISSUES
        # ======================================================

        print("-" * 80)
        print("3. Collecting ALL Issues")
        print("-" * 80)

        issues = self.issue_collector.collect(token, owner, repository_name)

        print(f"Total issues collected: " f"{len(issues)}")

        # ======================================================
        # 4. ALL PULL REQUESTS
        # ======================================================

        print("-" * 80)
        print("4. Collecting ALL Pull Requests")
        print("-" * 80)

        pull_requests = self.pr_collector.collect(token, owner, repository_name)

        print(f"Total pull requests collected: " f"{len(pull_requests)}")

        # ======================================================
        # 5. README
        # ======================================================

        print("-" * 80)
        print("5. Collecting README")
        print("-" * 80)

        try:

            readme = self.readme_collector.collect(token, owner, repository_name)

        except Exception as exception:

            print("README collection failed: " f"{exception}")

            readme = None

        print(f"README collected: " f"{bool(readme)}")

        # ======================================================
        # 6. BUILD COMPLETE CONTEXT
        # ======================================================

        print("-" * 80)
        print("6. Building Complete Repository Context")
        print("-" * 80)

        repository_context = self.context_builder.build(
            repository, commits, issues, pull_requests, readme
        )

        # ======================================================
        # 7. CREATE CHUNKS
        # ======================================================

        print("-" * 80)
        print("7. Creating Knowledge Chunks")
        print("-" * 80)

        chunks = self.chunker.create_activity_chunks(repository_context)

        print(f"Total LLM chunks created: " f"{len(chunks)}")

        # ======================================================
        # 8. PROCESS EVERY CHUNK
        # ======================================================

        print("-" * 80)
        print("8. Processing Knowledge Chunks")
        print("-" * 80)

        knowledge_results = []

        failed_chunks = []

        for index, chunk in enumerate(chunks):

            chunk_number = index + 1

            print(f"Processing chunk " f"{chunk_number}/" f"{len(chunks)}")

            try:

                result = self.central_agent.process_chunk(
                    source="github",
                    repository_name=repository_name,
                    repository_context=chunk,
                )

                if result:

                    knowledge_results.append(result)

                    print(f"Chunk " f"{chunk_number} " f"completed.")

                else:

                    failed_chunks.append(chunk_number)

                    print(f"Chunk " f"{chunk_number} " f"returned empty result.")

            except Exception as exception:

                failed_chunks.append(chunk_number)

                print(f"Chunk " f"{chunk_number} " f"failed: " f"{exception}")

        # ======================================================
        # 9. PROCESSING SUMMARY
        # ======================================================

        print("-" * 80)
        print("9. Knowledge Processing Summary")
        print("-" * 80)

        print(f"Total chunks      : " f"{len(chunks)}")

        print(f"Successful chunks : " f"{len(knowledge_results)}")

        print(f"Failed chunks     : " f"{len(failed_chunks)}")

        if failed_chunks:

            print(f"Failed chunks: " f"{failed_chunks}")

        # ======================================================
        # 10. MERGE ALL KNOWLEDGE
        # ======================================================

        print("-" * 80)
        print("10. Merging Knowledge")
        print("-" * 80)

        if not knowledge_results:

            raise RuntimeError("No knowledge was generated " "from GitHub activities.")

        final_knowledge = self.central_agent.merge_results(knowledge_results)
        
        
        knowledge_file = self.markdown_writer.write(
            source="github",
            repository=repository_name,
            filename="knowledge.md",
            content=final_knowledge
        )

        print(
            f"Knowledge file created: {knowledge_file}"
        )

        # ======================================================
        # 11. CREATE knowledge.md
        # ======================================================

        print("-" * 80)
        print("11. Creating knowledge.md")
        print("-" * 80)

        if not final_knowledge:

            raise RuntimeError("Final knowledge content is empty.")

        knowledge_file = self.markdown_writer.write(
            source="github",
            repository=repository_name,
            filename="knowledge.md",
            content=final_knowledge,
        )

        print("Knowledge Markdown file created:")

        print(knowledge_file)

        # ======================================================
        # 12. FINAL RESULT
        # ======================================================

        print("=" * 80)
        print("GITHUB REPOSITORY COLLECTION COMPLETED")
        print("=" * 80)

        return {
            "status": "SUCCESS",
            "repository": repository,
            "commitCount": len(commits),
            "issueCount": len(issues),
            "pullRequestCount": len(pull_requests),
            "readmeCollected": bool(readme),
            "chunkCount": len(chunks),
            "successfulChunkCount": len(knowledge_results),
            "failedChunkCount": len(failed_chunks),
            "failedChunks": failed_chunks,
            "knowledgeFile": knowledge_file,
            "knowledge": final_knowledge,
        }
