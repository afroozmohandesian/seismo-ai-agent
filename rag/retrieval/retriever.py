from rag.filtering.metadata_filter import (
    MetadataFilter,
)

from rag.evaluation.completeness import (
    RetrievalCompleteness,
)


class Retriever:

    def __init__(
        self,
        embedder,
        vector_store,
        bm25_retriever,
    ):

        self.embedder = embedder

        self.vector_store = vector_store

        self.bm25_retriever = bm25_retriever

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

            # -------------------------
            # Dense Retrieval
            # -------------------------

            dense_results = self.vector_store.search(
                query_embedding,
                top_k=top_k,
            )

            # -------------------------
            # BM25 Retrieval
            # -------------------------

            bm25_results = self.bm25_retriever.retrieve(
                query=query,
                top_k=top_k,
            )

            # -------------------------
            # Normalize Dense Scores
            # -------------------------

            for idx, result in enumerate(
                dense_results
            ):

                result["dense_score"] = max(
                    0.0,
                    1.0 - (idx * 0.1)
                )
            # -------------------------
            # Normalize BM25 Scores
            # -------------------------

            max_bm25 = max(
                result["bm25_score"]
                for result in bm25_results
            ) or 1.0

            for result in bm25_results:

                result[
                    "bm25_score_normalized"
                ] = (
                    result["bm25_score"]
                    / max_bm25
                )

            # -------------------------
            # Merge Results
            # -------------------------

            combined = {}

            # Dense results

            for result in dense_results:

                text = result["text"]

                combined[text] = {
                    **result,
                    "dense_score": result[
                        "dense_score"
                    ],
                    "bm25_score": 0.0,
                }

            # BM25 results

            for result in bm25_results:

                text = result["text"]

                if text not in combined:

                    combined[text] = {
                        **result,
                        "dense_score": 0.0,
                        "bm25_score": result[
                            "bm25_score_normalized"
                        ],
                    }

                else:

                    combined[text][
                        "bm25_score"
                    ] = result[
                        "bm25_score_normalized"
                    ]

            # -------------------------
            # Hybrid Score Fusion
            # -------------------------

            for result in combined.values():

                result["hybrid_score"] = (
                    0.7
                    * result["dense_score"]
                    + 0.3
                    * result["bm25_score"]
                )

            # -------------------------
            # Final Ranking
            # -------------------------

            results = sorted(
                combined.values(),
                key=lambda x: x[
                    "hybrid_score"
                ],
                reverse=True,
            )

            # -------------------------
            # Top-K Selection
            # -------------------------

            results = results[:top_k]

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