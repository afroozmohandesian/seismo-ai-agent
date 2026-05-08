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

from rag.filtering.metadata_enricher import (
    MetadataEnricher,
)

from rag.retrieval.hybrid_retriever import (
    HybridRetriever,
)
from rag.retrieval.query_expander import (
    QueryExpander,
)

class RAGPipeline:

    def __init__(self):

        self.loader = DocumentLoader()

        self.chunker = TextChunker()

        self.embedder = SentenceEmbedder()

        self.vector_store = None

        self.retriever = None

        self.hybrid_retriever = None

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

           enriched_metadata = (
                MetadataEnricher.enrich(chunk)
                )
           metadata.append(
               enriched_metadata
               )

        self.vector_store.add(
            embeddings,
            metadata,
        )

        self.hybrid_retriever = (
            HybridRetriever(
                self.vector_store,
            )
        )

        self.hybrid_retriever.fit(
            metadata
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

        expanded_query = (
            QueryExpander.expand(
                query
            )
        )

        print("\nExpanded Query:")
        print(expanded_query)

        query_embedding = (
            self.embedder.embed(
                [expanded_query]
            )[0]
        )

        results = (
            self.hybrid_retriever.retrieve(
                query_embedding=query_embedding,
                query_text=expanded_query,
                top_k=top_k,
            )
        )

        return self.retriever.retrieve(
            query=query,
            top_k=top_k,
            filters=filters,
            initial_results=results,
        )