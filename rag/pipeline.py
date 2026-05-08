from rag.ingestion.document_loader import (
    DocumentLoader,
)

from rag.chunking.text_chunker import (
    TextChunker,
)

from rag.embeddings.sentence_embedder import (
    SentenceEmbedder,
)

from rag.vector_store.faiss_store import (
    FAISSStore,
)

from rag.retrieval.retriever import (
    Retriever,
)


class RAGPipeline:

    def __init__(self):

        self.loader = DocumentLoader()

        self.chunker = TextChunker()

        self.embedder = SentenceEmbedder()

        self.vector_store = None

        self.retriever = None

    def ingest(self, path):

        document = self.loader.load(path)

        chunks = self.chunker.chunk(
            document["content"]
        )

        embeddings = self.embedder.embed(
            chunks
        )

        dimension = len(embeddings[0])

        self.vector_store = FAISSStore(
            dimension
        )

        metadata = []

        for chunk in chunks:

            metadata.append(
                {
                    "text": chunk,
                    "source": path,
                    "category": "seismic",
                }
            )

        self.vector_store.add(
            embeddings,
            metadata,
        )

        self.retriever = Retriever(
            self.embedder,
            self.vector_store,
        )

    def query(
        self,
        query,
        filters=None,
        top_k=5,
    ):

        return self.retriever.retrieve(
            query=query,
            top_k=top_k,
            filters=filters,
        )