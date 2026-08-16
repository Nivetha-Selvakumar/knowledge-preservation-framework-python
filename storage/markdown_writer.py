from pathlib import Path


class MarkdownWriter:

    BASE_FOLDER = "knowledge"

    def write(self, source: str, repository: str, filename: str, content: str):

        folder = Path(self.BASE_FOLDER) / source / repository

        folder.mkdir(parents=True, exist_ok=True)

        file_path = folder / filename

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

        return str(file_path)
