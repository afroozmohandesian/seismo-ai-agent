from rag.retrieval.keyword_retriever import (
    KeywordRetriever,
)


class HybridRetriever:

    def __init__(
        self,
        vector_store,
    ):

        self.vector_store = vector_store

        self.keyword_retriever = (
            KeywordRetriever()
        )

    def fit(
        self,
        metadata,
    ):

        self.keyword_retriever.fit(
            metadata
        )

    def retrieve(
        self,
        query_embedding,
        query_text,
        top_k=5,
    ):

        # -------------------------
        # Dense retrieval
        # -------------------------

        dense_results = (
            self.vector_store.search(
                query_embedding,
                top_k=top_k,
            )
        )

        # -------------------------
        # Sparse retrieval
        # -------------------------

        keyword_results = (
            self.keyword_retriever.retrieve(
                query_text,
                top_k=top_k,
            )
        )

        # -------------------------
        # Merge results
        # -------------------------

        merged = (
            dense_results
            + keyword_results
        )

        # -------------------------
        # Deduplicate
        # -------------------------

        unique_results = []

        seen_texts = set()

        for result in merged:

            text = result["text"]

            if text not in seen_texts:

                unique_results.append(
                    result
                )

                seen_texts.add(text)

        return unique_results[:top_k]