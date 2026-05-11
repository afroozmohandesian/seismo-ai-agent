from sklearn.feature_extraction.text import (
    TfidfVectorizer,
)

from sklearn.metrics.pairwise import (
    cosine_similarity,
)


class KeywordRetriever:

    def __init__(self):

        self.vectorizer = (
            TfidfVectorizer()
        )

        self.document_vectors = None

        self.documents = None

    def fit(
        self,
        documents,
    ):

        self.documents = documents

        texts = [
            doc["text"]
            for doc in documents
        ]

        self.document_vectors = (
            self.vectorizer.fit_transform(
                texts
            )
        )

    def retrieve(
        self,
        query,
        top_k=5,
    ):

        query_vector = (
            self.vectorizer.transform(
                [query]
            )
        )

        similarities = cosine_similarity(
            query_vector,
            self.document_vectors,
        )[0]

        ranked_indices = similarities.argsort()[
            ::-1
        ]

        results = []

        for idx in ranked_indices[:top_k]:

            results.append(
                self.documents[idx]
            )

        return results