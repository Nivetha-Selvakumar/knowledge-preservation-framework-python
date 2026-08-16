from services.prompt_builder import PromptBuilder
from services.knowledge_analyzer import KnowledgeAnalyzer
from services.response_parser import ResponseParser
from services.knowledge_formatter import KnowledgeFormatter
from services.markdown_generator import MarkdownGenerator

from storage.markdown_writer import MarkdownWriter


class CentralAgent:

    def __init__(self):

        self.prompt_builder = PromptBuilder()

        self.knowledge_analyzer = KnowledgeAnalyzer()

        self.response_parser = ResponseParser()

        self.knowledge_formatter = KnowledgeFormatter()

        self.markdown_generator = MarkdownGenerator()

        self.markdown_writer = MarkdownWriter()

    # ==========================================================
    # PROCESS ONE CHUNK
    # ==========================================================

    def process_chunk(self, source, repository_name, repository_context):

        print("=" * 80)

        print("CENTRAL AGENT")

        print(f"Repository: " f"{repository_name}")

        print(f"Activity Type: " f"{repository_context.get('activity_type')}")

        print(
            f"Chunk: "
            f"{repository_context.get('chunk_number')}/"
            f"{repository_context.get('total_chunks')}"
        )

        print("=" * 80)

        # ======================================================
        # 1. BUILD PROMPT
        # ======================================================

        prompt = self.prompt_builder.build_prompt(repository_context)

        # ======================================================
        # 2. LLM ANALYSIS
        # ======================================================

        llm_response = self.knowledge_analyzer.analyze(prompt)

        # ======================================================
        # 3. PARSE RESPONSE
        # ======================================================

        knowledge = self.response_parser.parse(llm_response)

        # ======================================================
        # 4. FORMAT
        # ======================================================

        formatted = self.knowledge_formatter.format(knowledge)

        # ======================================================
        # 5. GENERATE MARKDOWN
        # ======================================================

        markdown = self.markdown_generator.generate(formatted)

        return {
            "status": "SUCCESS",
            "repository": repository_name,
            "activityType": repository_context.get("activity_type"),
            "chunkNumber": repository_context.get("chunk_number"),
            "knowledge": knowledge,
            "markdown": markdown,
        }

    # ==========================================================
    # MERGE RESULTS
    # ==========================================================

    def merge_results(self, knowledge_results):

        print("=" * 80)

        print("CENTRAL AGENT - MERGING RESULTS")

        print("=" * 80)

        sections = []

        for index, result in enumerate(knowledge_results):

            if not result:

                continue

            markdown = result.get("markdown", "")

            if not markdown:

                continue

            sections.append(markdown)

        # ======================================================
        # Final Knowledge Document
        # ======================================================

        final_knowledge = "# Enterprise Knowledge Base\n\n"

        final_knowledge += "\n\n".join(sections)

        print(f"Merged " f"{len(sections)} " f"knowledge sections.")

        return final_knowledge

    # ==========================================================
    # OPTIONAL: ORIGINAL PROCESS
    # ==========================================================

    def process(self, source, repository_name, repository_context):

        result = self.process_chunk(source, repository_name, repository_context)

        markdown = result.get("markdown", "")

        file_path = self.markdown_writer.write(
            source=source,
            repository=repository_name,
            filename="knowledge.md",
            content=markdown,
        )

        return {
            "status": "SUCCESS",
            "repository": repository_name,
            "knowledge_file": file_path,
        }
