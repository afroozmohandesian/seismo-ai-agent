class AnswerGenerator:

    @staticmethod
    def generate(
        query,
        retrieved_results,
    ):

        if not retrieved_results:

            return (
                "No relevant information "
                "was retrieved."
            )

        answer_parts = []

        answer_parts.append(
            f"Query: {query}\n"
        )

        answer_parts.append(
            "Retrieved Insights:\n"
        )

        for idx, result in enumerate(
            retrieved_results,
            start=1,
        ):

            text = result["text"]

            shortened_text = (
                text[:250]
            )

            answer_parts.append(
                f"{idx}. {shortened_text}"
            )

        return "\n\n".join(
            answer_parts
        )