from rag.ingestion.base_loader import BaseLoader


class DocumentLoader(BaseLoader):

    def load(self, path: str):

        with open(path, "r", encoding="utf-8") as file:
            content = file.read()

        return {
            "type": "document",
            "content": content,
            "source": path,
        }