from rag.filtering.metadata_filter import (
    MetadataFilter,
)

from rag.retrieval.completeness import (
    RetrievalCompleteness,
)


class Retriever:

    def __init__(
        self,
        embedder,
        vector_store,
    ):

        self.embedder = embedder

        self.vector_store = vector_store

    def retrieve(
        self,
        query,
        top_k=5,
        filters=None,
        initial_results=None,
    ):

        # -------------------------
        # Query embedding
        # -------------------------

        query_embedding = self.embedder.embed(
            [query]
        )[0]

        # -------------------------
        # Retrieval
        # -------------------------

        if initial_results is not None:

            results = initial_results

        else:

            results = self.vector_store.search(
                query_embedding,
                top_k=top_k,
            )

        # -------------------------
        # Retrieval deduplication
        # -------------------------

        unique_results = []

        seen_texts = set()

        for result in results:

            text = result["text"]

            if text not in seen_texts:

                unique_results.append(
                    result
                )

                seen_texts.add(text)

        results = unique_results

        # -------------------------
        # Metadata filtering
        # -------------------------

        if filters:

            results = MetadataFilter.apply(
                results,
                filters,
            )

        # -------------------------
        # Completeness scoring
        # -------------------------

        completeness_score = (
            RetrievalCompleteness.score(
                query,
                results,
            )
        )

        print("\nRetrieval Completeness Score:")
        print(completeness_score)

        return results