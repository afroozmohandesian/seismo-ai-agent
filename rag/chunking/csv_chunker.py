from rag.chunking.base_chunker import BaseChunker


class CSVChunker(BaseChunker):

    def __init__(self, rows_per_chunk: int = 5):
        self.rows_per_chunk = rows_per_chunk

    def chunk(self, rows):

        chunks = []

        for i in range(0, len(rows), self.rows_per_chunk):

            chunk = rows[i:i + self.rows_per_chunk]

            chunks.append(chunk)

        return chunks