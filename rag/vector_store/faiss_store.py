import faiss
import numpy as np

from rag.vector_store.base_vector_store import (
    BaseVectorStore,
)


class FAISSStore(BaseVectorStore):

    def __init__(self, dimension: int):

        self.dimension = dimension

        self.index = faiss.IndexFlatL2(
            dimension
        )

        self.metadata = []

    def add(self, embeddings, metadata):

        vectors = np.array(
            embeddings
        ).astype("float32")

        self.index.add(vectors)

        self.metadata.extend(metadata)

    def search(self, embedding, top_k=5):

        query_vector = np.array(
            [embedding]
        ).astype("float32")

        distances, indices = self.index.search(
            query_vector,
            top_k
        )

        results = []

        for idx in indices[0]:

            if idx < len(self.metadata):

                results.append(
                    self.metadata[idx]
                )

        return results