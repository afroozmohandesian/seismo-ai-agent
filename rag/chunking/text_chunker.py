from rag.chunking.base_chunker import BaseChunker


class TextChunker(BaseChunker):

    def __init__(self, chunk_size: int = 500):
        self.chunk_size = chunk_size

    def chunk(self, text: str):

        chunks = []

        current_chunk = ""

        paragraphs = text.split("\n")

        for paragraph in paragraphs:

            if len(current_chunk) + len(paragraph) < self.chunk_size:
                current_chunk += paragraph + "\n"

            else:
                chunks.append(current_chunk.strip())
                current_chunk = paragraph + "\n"

        if current_chunk:
            chunks.append(current_chunk.strip())

        return chunks