from pathlib import Path


class MarkdownReader:

    BASE_FOLDER = "knowledge"

    def read(self, source: str, repository: str, filename: str):

        file_path = Path(self.BASE_FOLDER) / source / repository / filename

        if not file_path.exists():
            return ""

        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    def read_repository(self, source: str, repository: str):

        folder = Path(self.BASE_FOLDER) / source / repository

        if not folder.exists():
            return []

        documents = []

        for file in folder.glob("*.md"):

            with open(file, "r", encoding="utf-8") as f:

                documents.append({
                    "fileName": file.name,
                    "content": f.read()
                })

        return documents

    def read_all(self, source: str):

        base = Path(self.BASE_FOLDER) / source

        if not base.exists():
            return []

        repositories = []

        for repository in base.iterdir():

            if repository.is_dir():

                docs = []

                for file in repository.glob("*.md"):

                    with open(file, "r", encoding="utf-8") as f:

                        docs.append({
                            "fileName": file.name,
                            "content": f.read()
                        })

                repositories.append({
                    "repository": repository.name,
                    "documents": docs
                })

        return repositories