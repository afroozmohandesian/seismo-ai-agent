class RetrievalCompleteness:

    @staticmethod
    def score(
        query,
        results,
    ):

        if not results:
            return 0.0

        query_terms = set(
            query.lower().split()
        )

        matched_terms = set()

        for result in results:

            text = result["text"].lower()

            for term in query_terms:

                if term in text:

                    matched_terms.add(term)

        score = (
            len(matched_terms)
            / len(query_terms)
        )

        return round(score, 2)