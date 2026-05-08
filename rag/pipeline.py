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

from rag.retrieval.bm25_retriever import (
    BM25Retriever,
)

from rag.retrieval.query_expander import (
    QueryExpander,
)

from rag.generation.answer_generator import (
    AnswerGenerator,
)


class RAGPipeline:

    def __init__(self):

        self.loader = DocumentLoader()

        self.chunker = TextChunker()

        self.embedder = SentenceEmbedder()

        self.vector_store = None

        self.retriever = None

        self.hybrid_retriever = None

        self.bm25_retriever = None

        self.documents = None

    def ingest(self, path):

        # -------------------------
        # Load document
        # -------------------------

        document = self.loader.load(path)

        # -------------------------
        # Chunking
        # -------------------------

        chunks = self.chunker.chunk(
            document["content"]
        )

        # -------------------------
        # Embeddings
        # -------------------------

        embeddings = self.embedder.embed(
            chunks
        )

        dimension = len(
            embeddings[0]
        )

        # -------------------------
        # Vector Store
        # -------------------------

        self.vector_store = FAISSStore(
            dimension
        )

        # -------------------------
        # Metadata enrichment
        # -------------------------

        metadata = []

        for chunk in chunks:

            enriched_metadata = (
                MetadataEnricher.enrich(
                    chunk
                )
            )

            metadata.append(
                enriched_metadata
            )

        # -------------------------
        # Store embeddings
        # -------------------------

        self.vector_store.add(
            embeddings,
            metadata,
        )

        # -------------------------
        # Store documents
        # -------------------------

        self.documents = metadata

        # -------------------------
        # BM25 Retriever
        # -------------------------

        self.bm25_retriever = (
            BM25Retriever(
                self.documents
            )
        )

        # -------------------------
        # Hybrid Retriever
        # -------------------------

        self.hybrid_retriever = (
            HybridRetriever(
                self.vector_store,
            )
        )

        self.hybrid_retriever.fit(
            metadata
        )

        # -------------------------
        # Main Retriever
        # -------------------------

        self.retriever = Retriever(
            embedder=self.embedder,
            vector_store=self.vector_store,
            bm25_retriever=self.bm25_retriever,
        )

    def query(
        self,
        query,
        filters=None,
        top_k=5,
    ):

        # -------------------------
        # Query Expansion
        # -------------------------

        expanded_query = (
            QueryExpander.expand(
                query
            )
        )

        print("\nExpanded Query:")
        print(expanded_query)

        # -------------------------
        # Hybrid Retrieval
        # -------------------------

        retrieved_results = (
            self.retriever.retrieve(
                query=expanded_query,
                top_k=top_k,
                filters=filters,
            )
        )

        # -------------------------
        # Answer Generation
        # -------------------------

        generated_answer = (
            AnswerGenerator.generate(
                query=query,
                retrieved_results=retrieved_results,
            )
        )

        return {
            "answer": generated_answer,
            "results": retrieved_results,
        }