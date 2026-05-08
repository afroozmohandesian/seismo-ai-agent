from rag.filtering.metadata_filter import (
    MetadataFilter,
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
    ):

        query_embedding = self.embedder.embed(
            [query]
        )[0]

        results = self.vector_store.search(
            query_embedding,
            top_k=top_k,
        )

        if filters:
            results = MetadataFilter.apply(
                results,
                filters,
            )

        return results